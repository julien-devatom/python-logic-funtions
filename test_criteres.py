from unittest import TestCase

from criteres import S1_RACCParameters, S1, S1_RICCParameters, S2, S2_RACCParameters, S2_RICCParameters

"""
Ce script de test permet d'essayer les jeux de paramètres générés par les fonctions du fichier criteres.py, 
Et de voir si cela correspond bien au critère demandé : RACC ou RICC
Ceci est fait pour chaque prédicat S1 et S2.
"""
class TestCriteres(TestCase):
    def setUp(self) -> None:
        global verbose
        verbose = False
        self.P = True
        self.H = True
        self.T1 = True
        self.T2 = True
        self.T3 = True

    def testRACCParametersForPredicatS1AndMajorClauseP(self):
        """
        Test qui vérifie si, les jeux de paramètres générés correspondent à un
        critère RACC
        """
        parameters = S1_RACCParameters("P")
        index_of_clause_p = 0
        for parameter in parameters:
            self._testRACC(parameter, index_of_clause_p, S1)

    def testRACCParametersForPredicatS1AndMajorClauseH(self):
        """
        Test qui vérifie si, les jeux de paramètres générés correspondent à un
        critère RACC
        """
        parameters = S1_RACCParameters("H")
        index_of_clause_p = 1
        for parameter in parameters:
            self._testRACC(parameter, index_of_clause_p, S1)

    def testRACCParametersForPredicatS1AndMajorClauseT1(self):
        """
        Test qui vérifie si, les jeux de paramètres générés correspondent à un
        critère RACC
        """
        parameters = S1_RACCParameters("T1")
        index_of_clause_p = 2
        for parameter in parameters:
            self._testRACC(parameter, index_of_clause_p, S1)

    def testRACCParametersForPredicatS1AndMajorClauseT2(self):
        """
        Test qui vérifie si, les jeux de paramètres générés correspondent à un
        critère RACC
        """
        parameters = S1_RACCParameters("T2")
        index_of_clause_p = 3
        for parameter in parameters:
            self._testRACC(parameter, index_of_clause_p, S1)

    def testRACCParametersForPredicatS1AndMajorClauseT3(self):
        """
        Test qui vérifie si, les jeux de paramètres générés correspondent à un
        critère RACC
        """
        parameters = S1_RACCParameters("T3")
        index_of_clause_p = 4
        for parameter in parameters:
            self._testRACC(parameter, index_of_clause_p, S1)

    def testRICCParametersForPredicatS1AndMajorClauseP(self):
        """
        Test qui vérifie si, les jeux de paramètres générés correspondent à un
        critère RACC
        """
        parameters = S1_RICCParameters("P")
        index_of_clause_p = 0
        for parameter in parameters:
            self._testRICC(parameter, index_of_clause_p, S1)

    def testRICCParametersForPredicatS1AndMajorClauseH(self):
        """
        Test qui vérifie si, les jeux de paramètres générés correspondent à un
        critère RACC
        """
        parameters = S1_RICCParameters("H")
        index_of_clause_p = 1
        for parameter in parameters:
            self._testRICC(parameter, index_of_clause_p, S1)

    def testRICCParametersForPredicatS1AndMajorClauseT1(self):
        """
        Test qui vérifie si, les jeux de paramètres générés correspondent à un
        critère RACC
        """
        parameters = S1_RICCParameters("T1")
        index_of_clause_p = 2
        for parameter in parameters:
            self._testRICC(parameter, index_of_clause_p, S1)

    def testRICCParametersForPredicatS1AndMajorClauseT2(self):
        """
        Test qui vérifie si, les jeux de paramètres générés correspondent à un
        critère RACC
        """
        parameters = S1_RICCParameters("T2")
        index_of_clause_p = 3
        for parameter in parameters:
            self._testRICC(parameter, index_of_clause_p, S1)

    def testRICCParametersForPredicatS1AndMajorClauseT3(self):
        """
        Test qui vérifie si, les jeux de paramètres générés correspondent à un
        critère RACC
        """
        parameters = S1_RICCParameters("T3")
        index_of_clause_p = 4
        for parameter in parameters:
            self._testRICC(parameter, index_of_clause_p, S1)



    def testRACCParametersForPredicatS2AndMajorClauseP(self):
        """
        Test qui vérifie si, les jeux de paramètres générés correspondent à un
        critère RACC
        """
        parameters = S2_RACCParameters("P")
        index_of_clause_p = 0
        for parameter in parameters:
            self._testRACC(parameter, index_of_clause_p, S2)

    def testRACCParametersForPredicatS2AndMajorClauseT2(self):
        """
        Test qui vérifie si, les jeux de paramètres générés correspondent à un
        critère RACC
        """
        parameters = S2_RACCParameters("T2")
        index_of_clause_p = 1
        for parameter in parameters:
            self._testRACC(parameter, index_of_clause_p, S2)

    def testRACCParametersForPredicatS2AndMajorClauseT3(self):
        """
        Test qui vérifie si, les jeux de paramètres générés correspondent à un
        critère RACC
        """
        parameters = S2_RACCParameters("T3")
        index_of_clause_p = 2
        for parameter in parameters:
            self._testRACC(parameter, index_of_clause_p, S2)

    def testRICCParametersForPredicatS2AndMajorClauseP(self):
        """
        Test qui vérifie si, les jeux de paramètres générés correspondent à un
        critère RACC
        """
        parameters = S2_RICCParameters("P")
        index_of_clause_p = 0
        for parameter in parameters:
            self._testRICC(parameter, index_of_clause_p, S2)

    def testRICCParametersForPredicatS2AndMajorClauseT2(self):
        """
        Test qui vérifie si, les jeux de paramètres générés correspondent à un
        critère RACC
        """
        parameters = S2_RICCParameters("T2")
        index_of_clause_p = 1
        for parameter in parameters:
            self._testRICC(parameter, index_of_clause_p, S2)

    def testRICCParametersForPredicatS2AndMajorClauseT3(self):
        """
        Test qui vérifie si, les jeux de paramètres générés correspondent à un
        critère RACC
        """
        parameters = S2_RICCParameters("T3")
        index_of_clause_p = 2
        for parameter in parameters:
            self._testRICC(parameter, index_of_clause_p, S2)

    def _testRACC(self, parameters, index_of_major_clause, predicat):
        parameters.insert(index_of_major_clause, True)
        test1 = predicat(*parameters)
        parameters[index_of_major_clause] = False
        test2 = predicat(*parameters)
        self.assertNotEqual(test1, test2)

    def _testRICC(self, parameters: [], index_of_major_clause, predicat):
        parameters.insert(index_of_major_clause, True)
        test1 = predicat(*parameters)
        parameters[index_of_major_clause] = False
        test2 = predicat(*parameters)
        self.assertEqual(test1, test2)