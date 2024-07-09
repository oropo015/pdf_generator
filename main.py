from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

filepaths = glob.glob("xls/*.xlsx")
for filepath in filepaths:
    df = pd.read_excel(filepath)
    pdf = FPDF(orientation="p", unit="mm", format="A4")
    pdf.add_page()
    file = Path(filepath).stem.split("-")
    name = file[0]
    pdf.set_font(family="Helvetica", style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice-{name}", ln=1)
    for index, row in df.iterrows():
        pdf.set_font(family="Helvetica")
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)


    pdf.output(f"pdfs/{name}.pdf")
