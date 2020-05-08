from django.contrib import admin

# Register your models here.
from .models import Data
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class DataResource(resources.ModelResource):
    class Meta:
        model = Data
        import_id_fields = ('CdPat',)
        fields = ('CdPat','NomPren', 'DatEnrol', 'DatDernVisit','DatProchRdv', 'TelPat', 'PersSout','TelPerSout','Cohorte','Feedback')
class DataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = DataResource

    fieldsets = [
        ('Code Patient', {'fields': ['CdPat']}),
        ('Caracteristique ',
         {'fields': ['NomPren', 'DatEnrol', 'DatDernVisit', 'DatProchRdv', 'TelPat', 'PersSout','TelPerSout','Cohorte','Feedback']})
    ]
    list_display = ('CdPat','NomPren', 'DatEnrol', 'DatDernVisit', 'DatProchRdv', 'TelPat', 'PersSout','TelPerSout','Cohorte','Feedback')
    search_fields = ['CdPat']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if search_term != '':  # This chek needed if you additionaly use SimpleListFilter, otherwise SimpleListFilter would be broken
            search_term = map(str, search_term.split(','))  # not integers in search_term will result in an error
            queryset |= self.model.objects.filter(CdPat__in=search_term)
        return queryset.distinct(), use_distinct  # adding distinct() or objects duplicates could appear

admin.site.register(Data, DataAdmin)
