# -*- coding: utf-8 -*-
import json
import sys
global verbose

def main():
    res = RACC_RICC_Criteres()
    # On sauvegarde le resultat
    try:
        with open("parameters.json", "w") as file:
            json.dump(res, file, indent=4)
            if verbose:
                print("Le fichier parameters.json contient tous les jeux de tests qui ont été trouvé pour couvrir les "
                      "critères RACC et RICC en fonction des prédicats S1 et S2, ainsi que pour chaque Clause majeure")
    except IOError:
        pass

    # VNS pour S2
    S2_VNS()
    return res

############################################
##          Fonctions à tester            ##
############################################

def S1(P, H, T1, T2, T3):
    return (P and ((H and T1) or T2)) or (H and T2 and not T3)


def S2(P, T3, T2):
    return P or (not T3 and T2)


#####################################################
##          Génération des jeux de test            ##
##          pour les critères RACC & RICC          ##
#####################################################

def RACC_RICC_Criteres() -> dict:
    # RACC & RICC
    res = {
        "S1": {
            "RACC": {},
            "RICC": {}
        },
        "S2": {
            "RACC": {},
            "RICC": {}
        }
    }
    # On test les critères RACC & RICC pour chaque clause majeure respective
    for majorClause in ['P', 'H', 'T1', 'T2', 'T3']: # Pour le prédicat S1
        RACCParameters = S1_RACCParameters(majorClause)
        res["S1"]["RACC"][majorClause] = RACCParameters
        RICCParameters = S1_RICCParameters(majorClause)
        res["S1"]["RICC"][majorClause] = RICCParameters
        if majorClause in ['P', 'T3', 'T2']: # Pour le prédicat S2
            RACCParameters = S2_RACCParameters(majorClause)
            res["S2"]["RACC"][majorClause] = RACCParameters
            RICCParameters = S2_RICCParameters(majorClause)
            res["S2"]["RICC"][majorClause] = RICCParameters
    return res


def S1_RACCParameters(majorClause: str):
    """
    Cette fonction test chaque combinaisons de paramètres d'entrée et test si le jeu de paramètre défini un
    jeu de test pour le critère RACC, i.e le changent de la clause majeure entraine un changement du prédicat,
    avec les mêmes clauses mineures
    :param majorClause: La clause majeure
    :return: Les jeux de paramètres dans un tableau
    """
    assert majorClause in ['P', 'H', 'T1', 'T2', 'T3']
    if verbose:
        print(f"Test du critère RACC pour le prédicat S1, avec la clause majeure {majorClause}")
    jeux_de_parametres = []
    for P in [True, False]:
        for H in [True, False]:
            for T1 in [True, False]:
                for T2 in [True, False]:
                    for T3 in [True, False]:
                        if T1 is True and T3 is True:
                            # T1 et T3 ne peuvent être vrai en même temps
                            pass
                        else:
                            dict = {"P": P, "H": H, "T1": T1, "T2": T2, "T3": T3}
                            dict[majorClause] = True  # On test si la clause majeure est vraie
                            test1 = S1(dict['P'], dict['H'], dict['T1'], dict['T2'], dict['T3'])
                            dict[majorClause] = False  # On test si la clause majeure est fausse
                            test2 = S1(dict['P'], dict['H'], dict['T1'], dict['T2'], dict['T3'])
                            if not test1 == test2:  # On vérifie que le prédicat a été une fois vrai et une fois faux
                                dict.pop(majorClause)  # On enlève la clause majeure du jeu de paramètres
                                jeux_de_parametres.append(dict)
    if verbose:
        percentage_of_matched_tests = round(len(jeux_de_parametres) / (2 ** 6) * 100, 2)
        print(f'{percentage_of_matched_tests} % des tests fonctionnent')
    return jeux_de_parametres

def S1_RICCParameters(majorClause: str):
    """
    Cette fonction test chaque combinaisons de paramètres d'entrée et test si le jeu de paramètre défini un
    jeu de test pour le critère RICC, i.e le changent de la clause majeure n'entraine pas un changement du prédicat,
    avec les mêmes clauses mineures
    :param majorClause: La clause majeure
    :return: Les jeux de paramètres dans un tableau
    """
    if verbose:
        print(f"Test du critère RICC pour le prédicat S1, avec la clause majeure {majorClause}")
    jeux_de_parametres = []
    for P in [True, False]:
        for H in [True, False]:
            for T1 in [True, False]:
                for T2 in [True, False]:
                    for T3 in [True, False]:
                        if T1 is True and T3 is True:
                            # T1 et T3 ne peuvent être vrai en même temps
                            pass
                        else:
                            dict = {"P": P, "H": H, "T1": T1, "T2": T2, "T3": T3}
                            dict[majorClause] = True  # On test si la clause majeure est vraie
                            test1 = S1(dict['P'], dict['H'], dict['T1'], dict['T2'], dict['T3'])
                            dict[majorClause] = False  # On test si la clause majeure est fausse
                            test2 = S1(dict['P'], dict['H'], dict['T1'], dict['T2'], dict['T3'])
                            if test1 == test2: # On vérifie que le prédicat ne dépende pas de la clause majeure
                                dict.pop(majorClause) # on l'enlève du jeu de paramètre
                                jeux_de_parametres.append(dict)
    if verbose:
        percentage_of_matched_tests = round(len(jeux_de_parametres) / (2 ** 6) * 100, 2)
        print(f'{percentage_of_matched_tests} % des tests fonctionnent')
    return jeux_de_parametres

def S2_RACCParameters(majorClause: str):
    """
    Cette fonction test chaque combinaisons de paramètres d'entrée et test si le jeu de paramètre défini un
    jeu de test pour le critère RACC, i.e le changent de la clause majeure entraine un changement du prédicat,
    avec les mêmes clauses mineures
    :param majorClause: La clause majeure
    :return: Les jeux de paramètres dans un tableau
    """
    assert majorClause in ['P', 'T2', 'T3']
    if verbose:
        print(f"Test du critère RACC pour le prédicat S2, avec la clause majeure {majorClause}")
    jeux_de_parametres = []
    for P in [True, False]:
        for T2 in [True, False]:
            for T3 in [True, False]:
                dict = {"P": P, "T2": T2, "T3": T3}
                dict[majorClause] = True  # On test si la clause majeure est vraie
                test1 = S2(dict['P'], dict['T2'], dict['T3'])
                dict[majorClause] = False  # On test si la clause majeure est fausse
                test2 = S2(dict['P'], dict['T2'], dict['T3'])
                if not test1 == test2:  # On vérifie que le prédicat a été une fois vrai et une fois faux
                    dict.pop(majorClause)  # On enlève la clause majeure du jeu de paramètres
                    jeux_de_parametres.append(dict)
    if verbose:
        percentage_of_matched_tests = round(len(jeux_de_parametres)/(2**6)*100, 2)
        print(f'{percentage_of_matched_tests} % des tests fonctionnent')
    return jeux_de_parametres

def S2_RICCParameters(majorClause: str):
    """
    Cette fonction test chaque combinaisons de paramètres d'entrée et test si le jeu de paramètre défini un
    jeu de test pour le critère RACC, i.e le changent de la clause majeure entraine un changement du prédicat,
    avec les mêmes clauses mineures
    :param majorClause: La clause majeure
    :return: Les jeux de paramètres dans un tableau
    """
    assert majorClause in ['P', 'T2', 'T3']
    if verbose:
        print(f"Test du critère RICC pour le prédicat S2, avec la clause majeure {majorClause}")
    jeux_de_parametres = []
    for P in [True, False]:
        for T2 in [True, False]:
            for T3 in [True, False]:
                dict = {"P": P, "T2": T2, "T3": T3}
                dict[majorClause] = True  # On test si la clause majeure est vraie
                test1 = S2(dict['P'], dict['T2'], dict['T3'])
                dict[majorClause] = False  # On test si la clause majeure est fausse
                test2 = S2(dict['P'], dict['T2'], dict['T3'])
                if test1 == test2:  # On vérifie que le prédicat a été 2 fois identique
                    dict.pop(majorClause)  # On enlève la clause majeure du jeu de paramètres
                    jeux_de_parametres.append(dict)
    if verbose:
        percentage_of_matched_tests = round(len(jeux_de_parametres) / (2 ** 6) * 100, 2)
        print(f'{percentage_of_matched_tests} % des tests fonctionnent')
    return jeux_de_parametres


#######################################################
##          Génération du jeu de test                ##
##          pour le critère VNS du prédicat S2       ##
#######################################################
def S2_VNS():
    """
    S2 est dans sa forme DNF.
    """
    if verbose:
        print("----------------------------------------------------------")
        print("Test du critère VNS pour le prédicat S2=P + ~T3*T2, qui est dans sa forme DNF")
    # On calcule d'abord tous les jeux de tests possibles :
    tests = [[P, T3, T2, S2(P, T3, T2)] for P in [True, False] for T3 in [True, False] for T2 in [True, False]]

    # L'implicant I1 est P, on récupère les tests PUV de cet implicant
    tests_PUV_I1 = list(filter(lambda x: x[0] and not (not x[1] and x[2]), tests)) # On veut I1, et pas I2

    # L'implicant I2 est ~T3 * T2, on récupère les tests PUV de cet implicant
    tests_PUV_I2 = list(filter(lambda x: (not x[1] and x[2]) and not x[0], tests)) # On veut I2, et pas I1

    # P est seul dans son implicat, donc il ne peut pas avoir de PPF pour la clause P
    tests_PPF_P = []
    # On cherche les PPF de T3, I.E les tests ou P les 2 implicants sont faux
    # Mais que lorsqu'on enlève T3, l'impliquant 2 passe à vrai (ivi T2 doit être vrai)
    tests_PPF_T3 = list(filter(lambda x: not x[0] and not x[3] and x[2], tests))

    tests_PPF_T2 = list(filter(lambda x: not x[0] and not x[3] and not x[1], tests))

    # On essaie donc de récupérer le moins de tests possibles :
    # Dans notre cas, on a qu'un seul test qui correspond aux tests PUV I2, PPF T3 et PPF T2.
    # On récupère donc un test dans PUV I1 qui a possiblement été déjà pris pour les autres tests
    tests_needed = [tests_PUV_I2[0], tests_PPF_T3[0], tests_PPF_T2[0]]
    used = False
    for test in tests_PUV_I1:
        if test in tests_needed:
            used = True
    if used is False:
        tests_needed.append(tests_PUV_I1[0]) # Si on n'a pas de test correspondant, on ajoute le premier

    if verbose:
        print(f'{len(tests_needed)} tests utilisés :')
        print("{:<8} {:<8} {:<8} {:<10}".format('P', 'T3', 'T2', 'Résultat S2'))
        for test in tests_needed:
            print("{:<8} {:<8} {:<8} {:<10}".format(*test))


if __name__ == '__main__':
    if "verbose" in sys.argv:
        verbose = True
    else:
        verbose = False
    main()
