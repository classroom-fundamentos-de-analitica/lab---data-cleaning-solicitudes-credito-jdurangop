"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.
"""
import pandas


def clean_data():
    #
    # Inserte su código aquí
    #

    df = pandas.read_csv("solicitudes_credito.csv", sep=";", index_col=0, encoding='utf-8')
    df = df.dropna()

    df.sexo = df.sexo.str.lower()

    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()

    df.idea_negocio = df.idea_negocio.apply(
        lambda x: x.replace('-', ' ').replace('_', ' ').strip().lower())

    df.barrio = df.barrio.apply(
        lambda x: x.replace('-', ' ').replace('_', ' ').replace('.', '').lower())
    
    df.comuna_ciudadano = df.comuna_ciudadano.astype(str).apply(
        lambda x: x.replace('.0', ''))

    df.fecha_de_beneficio = pandas.to_datetime(
        df.fecha_de_beneficio,
        infer_datetime_format=True,
        errors='ignore',
        dayfirst=True
    )

    df.fecha_de_beneficio = pandas.to_datetime(
        df.fecha_de_beneficio,
        infer_datetime_format=True,
        errors='ignore',
        yearfirst=True
    )

    df.fecha_de_beneficio = df.fecha_de_beneficio.dt.strftime('%d-%m-%Y')

    df.monto_del_credito = df.monto_del_credito.apply(
        lambda x: int(x.replace(',', '').replace('$ ', '').replace('.00', '')))
    
    df.línea_credito = df.línea_credito.apply(
        lambda x: x.replace('-', ' ').replace('_', ' ').strip().lower())

    df = df.drop_duplicates()

    return df