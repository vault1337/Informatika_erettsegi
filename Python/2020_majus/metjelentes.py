"""4. Meteorológiai jelentés
Emelt szintű informatika érettségi megoldás.
Videó: https://youtu.be/3T_BGg9GOWw
Tanfolyamok, még több infó: https://vault1337.hu/

Az ország területén néhány városból rendszeres időközönként időjárás táviratokat küldenek.
A távirat egy rövid szöveges üzenet, amely a főbb időjárási információkat tartalmazza.
Rendelkezésünkre áll az ország területéről egy adott nap összes távirata.
A tavirathu13.txt szövegállomány egy adott hónap 13. napjának időjárás adatait tartalmazza.
Egy távirat adatai egy sorban találhatóak egymástól szóközzel elválasztva.
Egy sorban 4 adat szerepel a következőképpen.
	település
		szöveg (2 karakter)
		A település kétbetűs kódja
	idő
		szöveg (óópp formátumban)
		A mérés időpontja
	szélirány és -erősség
		szöveg (5 karakter)
		szélirány 3 karakter,
		-erősség 2 karakter
		A szél iránya fokban vagy szöveggel és sebessége csomóban megadva
	hőmérséklet
		egész szám (2 karakter)
		Mért hőmérséklet (nem negatív)
A sorok száma legfeljebb 500.
Az adatok idő szerint rendezettek.

Például:
BP 0300 32007 21
PA 0315 35010 19
PR 0315 32009 19
SM 0315 01015 20
DC 0315 VRB01 21
SN 0315 00000 21

A példában látható, hogy
	03:15-kor
	PR településen
	320 fokos irányból
	9 csomós szél fújt.
	A hőmérséklet 19 °C volt.
Ugyanekkor
	DC településen
	változó (VRB) szélirány volt
	1 csomós szélsebességgel,
	a hőmérséklet 21 °C volt.

Készítsen programot, amely a tavirathu13.txt állomány adatait felhasználva az alábbi kérdésekre válaszol!
A program forráskódját mentse metjelentes néven!
(A program megírásakor a felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie,
feltételezheti, hogy a rendelkezésre álló adatok a leírtaknak megfelelnek.)
A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt
írja a képernyőre a feladat sorszámát (például: 3. feladat)!
Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, hogy milyen értéket vár!
Az ékezetmentes kiírás is elfogadott.
Az eredmény megjelenítését és a felhasználóval való kommunikációt a feladatot követő minta alapján valósítsa meg!
"""

# 1. Olvassa be és tárolja el a tavirathu13.txt állomány adatait!
reports = []
with open("tavirathu13.txt", "rt", encoding="utf-8") as file:
    #DC 0415 VRB02 21
    for line in file:
        parts = line.strip().split(" ")
        report = {"city": parts[0],
                  "hour": parts[1][:2],
                  "minute": parts[1][2:],
                  "deg": parts[2][:3],
                  "speed": int(parts[2][3:]),
                  "temperature": int(parts[3])}
        reports.append(report)

# 2. Kérje be a felhasználótól egy város kódját!
#	Adja meg, hogy az adott városból mikor érkezett az utolsó mérési adat!
#	A kiírásban az időpontot óó:pp formátumban jelenítse meg!
# Minta:
# Adja meg egy település kódját! Település: SM
# Az utolsó mérési adat a megadott településről 23:45-kor érkezett.
print("2. feladat")
city = input("Adja meg egy település kódját! Település: ")
last_report = None
for report in reports:
    if report["city"] == city:
        last_report = report
reports_from_city = [report for report in reports if report["city"] == city]
print(f"Az utolsó mérési adat a megadott településről {reports_from_city[-1]['hour']}:{reports_from_city[-1]['minute']}-kor érkezett.")
print(f"Az utolsó mérési adat a megadott településről {last_report['hour']}:{last_report['minute']}-kor érkezett.")

# 3. Határozza meg, hogy a nap során mikor mérték a legalacsonyabb és a legmagasabb hőmérsékletet!
#	Jelenítse meg a méréshez kapcsolódó település nevét, az időpontot és a hőmérsékletet!
#	Amennyiben több legnagyobb vagy legkisebb érték van, akkor elég az egyiket kiírnia.
# Minta:
# A legalacsonyabb hőmérséklet: SM 23:45 16 fok.
# A legmagasabb hőmérséklet: DC 13:15 35 fok.
print("3. feladat")
min_report = reports[0]
max_report = reports[0]
for report in reports:
    if report["temperature"] > max_report["temperature"]:
        max_report = report
    if report["temperature"] < min_report["temperature"]:
        min_report = report
print(f"A legalacsonyabb hőmérséklet: {min_report['city']} {min_report['hour']}:{min_report['minute']} {min_report['temperature']} fok.")
print(f"A legmagasabb hőmérséklet: {max_report['city']} {max_report['hour']}:{max_report['minute']} {max_report['temperature']} fok.")

# 4. Határozza meg, azokat a településeket és időpontokat, ahol és amikor a mérések idején szélcsend volt!
#	(A szélcsendet a táviratban 00000 kóddal jelölik.)
#	Ha nem volt ilyen, akkor a „Nem volt szélcsend a mérések idején.” szöveget írja ki!
#	A kiírásnál a település kódját és az időpontot jelenítse meg.
# Minta:
# BP 01:00
print("4. feladat")
lull_reports = []
for report in reports:
    if report["speed"] == 0:
        lull_reports.append(report)
if lull_reports.__len__() == 0:
    print("Nem volt szélcsend a mérések idején.")
else:
    for report in lull_reports:
        print(f"{report['city']} {report['hour']}:{report['minute']}")


# 5. Határozza meg a települések napi középhőmérsékleti adatát és a hőmérséklet-ingadozását!
#	A kiírásnál a település kódja szerepeljen a sor elején a minta szerint!
#	A kiírásnál csak a megoldott feladatrészre vonatkozó szöveget és értékeket írja ki!
#	a.	A középhőmérséklet azon hőmérsékleti adatok átlaga,
#		amikor a méréshez tartozó óra értéke 1., 7., 13., 19.
#		Ha egy településen a felsorolt órák valamelyikén nem volt mérés,
#		akkor a kiírásnál az „NA” szót jelenítse meg!
#		Az adott órákhoz tartozó összes adat átlagaként határozza meg a középhőmérsékletet,
#		azaz minden értéket azonos súllyal vegyen figyelembe!
#		A középhőmérsékletet egészre kerekítve jelenítse meg!
#	b.	A hőmérséklet-ingadozás számításhoz az adott településen
#		a napi legmagasabb
#		és legalacsonyabb hőmérséklet különbségét kell kiszámítania!
#		(Feltételezheti, hogy minden település esetén volt legalább két mérési adat.)
# Minta:
# BP Középhőmérséklet: 23; Hőmérséklet-ingadozás: 8
# BC NA; Hőmérséklet-ingadozás: 14
print("5. feladat")
cities = set()
for report in reports:
    cities.add(report["city"])
for city in cities:
    reports_from_city = [report for report in reports if report["city"] == city]
    temperatures_from_city = [report["temperature"] for report in reports_from_city]
    mean_temperature_measurements = [report["temperature"] for report in reports_from_city
                                     if report["hour"] == "01"
                                     or report["hour"] == "07"
                                     or report["hour"] == "13"
                                     or report["hour"] == "19"]
    mean_temp_01 = [report["temperature"] for report in reports_from_city if report["hour"] == "01"]
    mean_temp_07 = [report["temperature"] for report in reports_from_city if report["hour"] == "07"]
    mean_temp_13 = [report["temperature"] for report in reports_from_city if report["hour"] == "13"]
    mean_temp_19 = [report["temperature"] for report in reports_from_city if report["hour"] == "19"]
    min_temp = min(temperatures_from_city)
    max_temp = max(temperatures_from_city)
    mean_temperature = 0
    mean_count = 0
    for temperature in mean_temperature_measurements:
        mean_temperature += temperature
        mean_count += 1
    if mean_temp_01.__len__() > 0 and mean_temp_07.__len__() > 0 and mean_temp_13.__len__() > 0 and mean_temp_19.__len__() > 0:
        mean_temperature /= mean_count
        print(f"{city} Középhőmérséklet: {int(mean_temperature.__round__(0))}; Hőmérséklet-ingadozás: {max_temp - min_temp}")
    else:
        print(f"{city} NA; Hőmérséklet-ingadozás: {max_temp - min_temp}")


# 6. Hozzon létre településenként egy szöveges állományt,
#	amely első sorában a település kódját tartalmazza!
#	A további sorokban a mérési időpontok
#	és a hozzá tartozó szélerősségek jelenjenek meg!
#	A szélerősséget a minta szerint a számértéknek megfelelő számú kettőskereszttel (#) adja meg!
#	A fájlban az időpontokat és a szélerősséget megjelenítő kettőskereszteket szóközzel válassza el egymástól!
#	A fájl neve X.txt legyen, ahol az X helyére a település kódja kerüljön!
# Minta:
# A fájlok elkészültek.
# A BC.txt fájl tartalma:
# BC
# 00:45 ###

print("6.feladat")
for city in cities:
    with open(f"{city}.txt", "wt", encoding="utf-8") as file:
        file.write(f"{city}\n")
        reports_from_city = [report for report in reports if report["city"] == city]
        for report in reports_from_city:
            file.write(f"{report['hour']}:{report['minute']} {report['speed'] * '#'}\n")
print("A fájlok elkészültek.")
