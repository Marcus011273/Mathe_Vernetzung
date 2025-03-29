import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Titel der App
st.title('Vernetzung mit Alltag und Lebenswelt (Mittelschule)')

# Einführung
st.markdown('''
Diese App zeigt Ihnen, wie Sie den Mathematikunterricht durch Vernetzung mit Alltag und Lebenswelt lebensnah gestalten können.

### Zielsetzungen:
- Mathematik durch Alltagsbezüge verständlich machen
- Förderung von Anwendungsorientierung und Relevanz im Mathematikunterricht
''')

# Algebra – Lineare Funktionen und Handyverträge
st.header('1. Algebra – Handyverträge vergleichen (lineare Funktionen)')

st.markdown('''
Tarif A: Grundgebühr 5 € pro Monat, 0,10 € pro Minute

Tarif B: Keine Grundgebühr, 0,20 € pro Minute
''')

telefon_minuten = st.slider('Minuten pro Monat auswählen:', 0, 500, 100)
tarif_a = 5 + 0.10 * telefon_minuten
tarif_b = 0.20 * telefon_minuten

st.write(f'Kosten Tarif A: {tarif_a:.2f} Euro')
st.write(f'Kosten Tarif B: {tarif_b:.2f} Euro')

# Dynamische Visualisierung je nach gewählten Minuten
data_minuten = np.arange(0, telefon_minuten+1, 10)
kosten_a = 5 + 0.10 * data_minuten
kosten_b = 0.20 * data_minuten

fig, ax = plt.subplots()
ax.plot(data_minuten, kosten_a, label='Tarif A')
ax.plot(data_minuten, kosten_b, label='Tarif B')
ax.set_xlabel('Minuten')
ax.set_ylabel('Kosten in Euro')
ax.legend()
st.pyplot(fig)

st.markdown('''
**Aufgabe für Sie:**
- Entwickeln Sie ähnliche Aufgaben zu linearen Funktionen mit anderen Alltagsbeispielen.
''')

# Geometrie – Dachneigungen berechnen
st.header('2. Geometrie – Dachneigungen berechnen (Trigonometrie)')

st.markdown('''
Berechnen Sie die Dachhöhe anhand der Dachneigung. Es gibt zwei gängige Methoden:

**Wortgleichung für Methode 1:**
Die Höhe ergibt sich, indem man die halbe Dachbreite mit dem Tangens des Neigungswinkels multipliziert.

**Wortgleichung für Methode 2:**
Die Höhe ergibt sich, indem man die Länge der schrägen Dachfläche (Hypotenuse) mit dem Sinus des Neigungswinkels multipliziert.

**Methode 1 (Tangens):**
Höhe = tan(Neigungswinkel) × (Dachbreite ÷ 2)

**Methode 2 (Sinus):**
Höhe = sin(Neigungswinkel) × Hypotenuse (Länge der Dachschräge)

Wir setzen hier beide Varianten um:
''')

dachbreite = st.slider('Dachbreite in Metern:', 1, 20, 10)
neigungswinkel = st.slider('Neigungswinkel in Grad:', 0, 60, 30)

# Methode 1: Tangens
hoehe_tan = (dachbreite / 2) * np.tan(np.radians(neigungswinkel))
# Methode 2: Sinus
hypotenuse = np.sqrt((dachbreite / 2)**2 + hoehe_tan**2)
hoehe_sin = np.sin(np.radians(neigungswinkel)) * hypotenuse

st.write(f"**Höhe mit Tangens (Methode 1):** {hoehe_tan:.2f} m")
st.write(f"**Höhe mit Sinus (Methode 2):** {hoehe_sin:.2f} m")

# Dynamische Visualisierung der Dachneigung mit Beschriftung
fig, ax = plt.subplots()

# Dreieckspunkte
x = [0, dachbreite / 2, dachbreite]
y = [0, hoehe_tan, 0]

# Dachlinie
ax.plot(x, y, color='brown', label='Dachfläche')
# Dachgrundlinie
ax.plot([0, dachbreite], [0, 0], color='black', linestyle='--', label='Grundlinie')
# Höhenlinie
ax.plot([dachbreite / 2, dachbreite / 2], [0, hoehe_tan], color='blue', linestyle=':', label='Höhe')

# Winkelbeschriftung links
ax.text(0.5, 0.2, f'{neigungswinkel}°', rotation=0, fontsize=10, color='green')

# Füllung des Daches
ax.fill_between(x, y, color='orange', alpha=0.5)

ax.set_xlim(0, dachbreite)
ax.set_ylim(0, max(hoehe_tan, 1))
ax.set_aspect('equal', 'box')
ax.set_xlabel('Breite (m)')
ax.set_ylabel('Höhe (m)')
ax.legend()
ax.grid(True)
st.pyplot(fig)

st.markdown('''
**Aufgabe für Sie:**
- Erstellen Sie weitere Aufgaben zur Trigonometrie mit Bezügen zur Architektur oder anderen praktischen Situationen.
''')

# Statistik – Klasseneigene Umfragen
st.header('3. Statistik – Klasseneigene Umfragen auswerten')

st.markdown('''
Beispiel: Lieblingsfächer der Klasse
''')

faecher = ['Mathematik', 'Deutsch', 'Englisch', 'Sport', 'Kunst']
stimmen = [12, 8, 5, 15, 7]

fig, ax = plt.subplots()
ax.bar(faecher, stimmen, color='skyblue')
ax.set_xlabel('Fächer')
ax.set_ylabel('Stimmenanzahl')
st.pyplot(fig)

st.markdown('''
**Aufgabe für Sie:**
- Führen Sie eine eigene kleine Umfrage durch und bereiten Sie die Ergebnisse visuell auf.
''')

# Weitere Aufgaben für Referendare
st.header('Zusätzliche Aufgaben für Referendare')
st.markdown('''
- Entwickeln Sie weitere lebensweltbezogene Aufgaben aus unterschiedlichen mathematischen Themenbereichen.
- Überlegen Sie, wie Sie Schülerinnen und Schüler motivieren können, Mathematik in ihrem Alltag zu erkennen und anzuwenden.
- Planen Sie eine Unterrichtsstunde, die Mathematik mit konkreten Alltagserfahrungen Ihrer Schülerinnen und Schüler vernetzt.
''')

