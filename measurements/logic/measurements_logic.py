from ..models import Measurement

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(meas_pk):
    measurement = Measurement.objects.get(pk=meas_pk)
    return measurement

def update_measurement(meas_pk,new_meas):
    measurement=get_measurement(meas_pk)
    measurement.variable = new_meas["variable"]
    measurement.value = new_meas["value"]
    measurement.unit = new_meas["unit"]
    measurement.place= new_meas["place"]
    
    measurement.save()
    return measurement

def create_variable(new_meas):
    measurement= Measurement(variable = new_meas["variable"],
                             value = new_meas["value"],
                             unit = new_meas["unit"],
                             place= new_meas["place"])
                             
    measurement.save()
    return measurement

def delete_measurement(meas_pk):
    measurement = get_measurement(meas_pk)
    measurement.delete()
    return 'Se elimino la medida con la pk = '+ str(meas_pk)
    

