# -*- coding: utf-8 -*-


def VerifTypeM(système):
#permet de verifier si système est bien un liste de liste
#il faudrait aussi verifier si le éléments sont bien des float
	if isinstance(système, list) == False:
		return False
	elif isinstance(système[0], list) == False:
		return False
	else:
		nbvariablem1 = len(système[0])
		for x in système:
			if isinstance(x, list) == False:
				return False
			if len(x) != nbvariablem1:
				return False
		return True


def reduireunecolone(système, index_valeurs, indexColoneOuReduir):
	if VerifTypeM(système) == False:
		return None

	a = système[index_valeurs][indexColoneOuReduir]

	for i in range(len(système)):
		if i != index_valeurs:
			b = système[i][indexColoneOuReduir]
			for j in range(len(système[0])):
				système[i][j] += -système[index_valeurs][j]*b/a

	return système
		

def trouverUneValeurNnNulSurUneLigne(système, indexColonne, lignesUtilisé = []):
	if VerifTypeM(système) == False:
		return None
	for x in range(len(système)):
		if système[x][indexColonne] != 0 and (x in lignesUtilisé) == False:
			return x;
	return -1

def NettoyageSystème(système):
	if VerifTypeM(système) == False:
		return None

	for i in range(len(système)):
		scalaire = 0
		for j in range(len(système[i])):
			if scalaire != 0:
				système[i][j] = système[i][j]*scalaire
			else:
				if système[i][j] != 0:
					scalaire = 1/système[i][j]
					système[i][j] = système[i][j]*scalaire

	return système


def pivotdegauss(système, nettoyé = True):
	if VerifTypeM(système) == False:
		return None

	taillei = len(système)
	taillej = len(système[0])

	lignesUtilisé = []
	colonnesNuls = []

	for js in range(taillej):
		
		if (js + len(colonnesNuls)) >= taillej:
			break

		while True:

			j = js + len(colonnesNuls)

			if j >= taillej:
				break

			i = trouverUneValeurNnNulSurUneLigne(système, j, lignesUtilisé)
			if i != -1:
				système = reduireunecolone(système, i, j)

				lignesUtilisé.append(i)
				break

			else:
				colonnesNuls.append(j)

	if nettoyé == False:
		return système
	else:
		return NettoyageSystème(système)

def AfficherMatrice(matrice):
	for ligne in matrice:
		print(ligne)

AfficherMatrice(pivotdegauss([[-9,-3,-3,1],[6,2,2,-1],[26,7,9,-2],[0,0,0,1]]))