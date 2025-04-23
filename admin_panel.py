#example
from sqladmin import ModelView, Admin
from fastapi_app.models import Patient
from fastapi_app.database import engine

class PatientAdmin(ModelView, model=Patient):
    column_list = [Patient.id, Patient.name, Patient.age, Patient.sex, Patient.created_at]
    form_columns = [Patient.name, Patient.age, Patient.sex]
    column_searchable_list = [Patient.name, Patient.age] #filter example

def setup_admin(app):
    admin = Admin(app, engine)
    admin.add_view(PatientAdmin)
