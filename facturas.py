from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# Función para crear un documento PDF con formato de factura
def crear_factura():
    # Obtener la fecha y el número de factura del usuario
    fecha = input("Fecha (DD/MM/AAAA): ")
    numero_factura = input("Número de factura: ")

    # Obtener información del cliente
    nombre_cliente = input("Nombre del cliente: ")
    direccion_cliente = input("Dirección del cliente: ")

    # Obtener información de la empresa
    cif_empresa = input("CIF de la empresa: ")

    # Obtener detalles de la factura
    concepto = input("Concepto de la factura: ")
    valor_factura = float(input("Valor de la factura: "))

    # Calcular impuestos
    iva = valor_factura * 0.21  # 21% de IVA
    irpf = valor_factura * 0.15  # 15% de IRPF
    total_factura = valor_factura + iva - irpf

    # Obtener forma de pago
    forma_pago = input("Forma de pago: ")

    # Crear el documento PDF
    pdf_filename = f"factura_{numero_factura}.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    styles = getSampleStyleSheet()

    # Configurar el contenido del PDF
    contenido = []

    # Encabezado de la factura
    encabezado = Paragraph("Factura", styles['Heading1'])
    contenido.append(encabezado)

    contenido.append(Spacer(1, 12))

    # Fecha y número de factura
    contenido.append(Paragraph(f"Fecha: {fecha}", styles['Normal']))
    contenido.append(Paragraph(f"Número de Factura: {numero_factura}", styles['Normal']))

    contenido.append(Spacer(1, 12))

    # Información del cliente
    contenido.append(Paragraph(f"Cliente: {nombre_cliente}", styles['Normal']))
    contenido.append(Paragraph(f"Dirección: {direccion_cliente}", styles['Normal']))

    contenido.append(Spacer(1, 12))

    # Información de la empresa
    contenido.append(Paragraph(f"CIF de la Empresa: {cif_empresa}", styles['Normal']))

    contenido.append(Spacer(1, 12))

    # Detalles de la factura
    contenido.append(Paragraph("Detalles:", styles['Heading2']))
    tabla_datos = []
    tabla_datos.append(["Concepto", "Valor", "IVA (21%)", "IRPF (15%)", "Total"])

    tabla_datos.append([concepto, f"${valor_factura:.2f}", f"${iva:.2f}", f"${irpf:.2f}", f"${total_factura:.2f}"])

    tabla = Table(tabla_datos)
    tabla.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

    contenido.append(tabla)

    contenido.append(Spacer(1, 12))

    # Forma de pago
    contenido.append(Paragraph(f"Forma de Pago: {forma_pago}", styles['Normal']))

    # Construir el PDF
    doc.build(contenido)

    print(f"Se ha creado la factura en '{pdf_filename}'")

# Llamar a la función para crear la factura
crear_factura()
