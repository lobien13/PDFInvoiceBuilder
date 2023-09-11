from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# Function to create the PDF
def crear_factura():
    # Get the data
    fecha = input("Fecha (DD/MM/AAAA): ")
    numero_factura = input("Número de factura: ")
    nombre_cliente = input("Nombre del cliente: ")
    direccion_cliente = input("Dirección del cliente: ")
    cif_empresa = input("CIF de la empresa: ")
    concepto = input("Concepto de la factura: ")
    valor_factura = float(input("Valor de la factura: "))
    nombre_emisor = input("Nombre del emisor: ")  # Agregado
    nif_emisor = input("NIF del emisor: ")  # Agregado

    # calculate taxes
    iva = valor_factura * 0.21  # 21% de IVA
    irpf = valor_factura * 0.15  # 15% de IRPF
    total_factura = valor_factura + iva - irpf

    forma_pago = input("Forma de pago: ")

    # PDF 
    pdf_filename = f"factura_{numero_factura}.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    styles = getSampleStyleSheet()

    # Config PDF
    contenido = []

    # Head
    encabezado = Paragraph("Factura", styles['Heading1'])
    contenido.append(encabezado)

    contenido.append(Spacer(1, 12))

    # Date
    contenido.append(Paragraph(f"Fecha: {fecha}", styles['Normal']))
    contenido.append(Paragraph(f"Número de Factura: {numero_factura}", styles['Normal']))

    contenido.append(Spacer(1, 12))

    # Info
    contenido.append(Paragraph(f"Cliente: {nombre_cliente}", styles['Normal']))
    contenido.append(Paragraph(f"Dirección: {direccion_cliente}", styles['Normal']))

    contenido.append(Spacer(1, 12))

    # Info
    contenido.append(Paragraph(f"CIF de la Empresa: {cif_empresa}", styles['Normal']))

    contenido.append(Spacer(1, 12))

    # Emisor
    contenido.append(Paragraph(f"Emisor: {nombre_emisor}", styles['Normal']))  # Agregado
    contenido.append(Paragraph(f"NIF del Emisor: {nif_emisor}", styles['Normal']))  # Agregado

    contenido.append(Spacer(1, 12))

    # Details
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

    
    contenido.append(Paragraph(f"Forma de Pago: {forma_pago}", styles['Normal']))

    # build the PDF
    doc.build(contenido)

    print(f"Se ha creado la factura en '{pdf_filename}'")


crear_factura()
