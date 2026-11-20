import csv, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

base = sys.argv[1]
linhas = [
    ("Jardim Pantanal", "Muito Alto", "Risco de alagamento forte. Saia de áreas baixas e vá para local seguro.", "2026-11-03"),
    ("Itaim Paulista", "Alto", "Chuva forte nas próximas horas. Não atravesse ruas alagadas.", "2026-11-03"),
    ("Vila Prudente", "Médio", "Pode alagar perto do córrego. Fique atento e evite a região.", "2026-11-05"),
    ("São Miguel Paulista", "Alto", "Rio Tietê subindo. Tire objetos do chão e guarde documentos.", "2026-11-07"),
    ("Parelheiros", "Baixo", "Chuva fraca prevista. Sem risco no momento.", "2026-11-08"),
    ("Mooca", "Médio", "Calor forte à tarde. Beba água e evite sol das 11h às 16h.", "2026-11-10"),
    ("Capão Redondo", "Alto", "Risco de deslizamento em encostas. Veja se há rachaduras nas paredes.", "2026-11-12"),
    ("Penha", "Muito Alto", "Onda de calor com 37°C. Cuide de idosos, crianças e animais.", "2026-11-14"),
    ("Jardim Helena", "Alto", "Alagamento previsto à noite. Saia mais cedo e evite áreas baixas.", "2026-11-17"),
    ("Brasilândia", "Médio", "Ventos fortes e chuva. Fique longe de árvores e fios.", "2026-11-19"),
]
cab = ("Regiao", "NivelRisco", "Mensagem", "Data")

wb = Workbook()
ws = wb.active
ws.title = "Alertas"
ws.append(cab)
for l in linhas:
    ws.append(l)  # Data como texto ISO (yyyy-MM-dd) para leitura estável no Read Range
for c in ws[1]:
    c.font = Font(bold=True, color="FFFFFF")
    c.fill = PatternFill("solid", fgColor="0B3D5C")
for col, w in zip("ABCD", (22, 14, 75, 12)):
    ws.column_dimensions[col].width = w
for p in (base + r"\alertas_defesa_civil.xlsx", base + r"\UiPath\AlertaAquiRPA\alertas_defesa_civil.xlsx"):
    wb.save(p)
with open(base + r"\alertas_defesa_civil.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f, delimiter=";")
    w.writerow(cab); w.writerows(linhas)
print("ok")
