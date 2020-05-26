import random
def interpretation_poly(degres_f_polynomial, points):
	"""if isinstance(systeme, list) == False:
		return None
	for x in points:
		if isinstance(x, list) == False:
			return None
		if len(x) != 2:
			return None
	if len(points) < degres_f_polynomial + 1:
		return None"""

	systeme = []

	for i in range(degres_f_polynomial + 1):
		ligne = []
		for j in range(degres_f_polynomial + 1):
			ligne.append(points[i][0] ** (degres_f_polynomial - j))
		ligne.append(points[i][1])
		print(ligne)
		systeme.append(ligne)

	from ClassesEtFonctions import pivotdegauss

	systeme = pivotdegauss(systeme)

	return systeme[degres_f_polynomial][degres_f_polynomial + 1]

def generepoints(nombrecaché, degres_f_polynomial, nombredepointgenere):
	scalaires = []

	for x in range(degres_f_polynomial):
		scalaires.append(random.randint(-5,5))

	scalaires.append(nombrecaché)

	print(scalaires)

	"""print(scalaires)"""

	points = []

	for p in range(nombredepointgenere):
		point = []

		x=0
		while x==0:
			x = random.randint(-4,5)
		point.append(x)

		y = 0
		for j in range(degres_f_polynomial+1):
			y += scalaires[j] * (x ** (degres_f_polynomial - j))
		point.append(y)

		points.append(point)

	return points

x = generepoints(21, 2, 4)

print(x)

print(interpretation_poly(2, x))