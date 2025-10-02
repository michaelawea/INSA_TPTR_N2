# Rapport d'expérience CEM

# Première partie : Diaphonie entre pistes

## A/ Effet du blindage des pistes et de leur connexion à la masse

### 1. Objectif de l'expérience

Étudier l'influence du mode de mise à la masse du blindage des pistes sur la diaphonie entre pistes à différentes fréquences, et vérifier les caractéristiques théoriques de la diaphonie capacitive et inductive en fonction de la fréquence.

### 2. Configuration expérimentale

**Matériel utilisé :**

- Carte CEM1/I/1
- Générateur de signaux sinusoïdaux 0-20 MHz
- Oscilloscope (impédance d'entrée réglée à 50Ω)
- Câble BNC

**Configuration de test :**

- Le signal d'entrée est appliqué à la piste "sa" (piste agresseur)
- Le signal de sortie est mesuré sur la piste victime
- Trois états de mise à la masse : non relié, relié à une extrémité, relié aux deux extrémités

### 3. Données expérimentales

### Tableau de mesures brutes

| Fréquence | Tension d'entrée Uin (V) | Non relié Uout (mV) | Masse à une extrémité Uout (mV) | Masse aux deux extrémités Uout (mV) |
| --- | --- | --- | --- | --- |
| 7 kHz | 1,79 | 5,0 | 6,3 | 6,3 |
| 100 kHz | 1,78 | 5,4 | 5,4 | 3,5 |
| 1 MHz | 1,80 | 25,0 | ~24,0 | 6,0 |
| 5 MHz | 1,81 | 124,0 | ~123,0 | 22,2 |
| 10 MHz | 1,80 | 180,0 | ~160,0 | 45,0 |
| 15 MHz | 1,80 | 275,0 | ~265,0 | 60,0 |
| 20 MHz | 1,80 | 350,0 | ~330,0 | 74,0 |

*Remarque : Les valeurs pour la masse à une extrémité à certaines fréquences sont des estimations, basées sur une variation de 1-2 mV par rapport à la masse aux deux extrémités.*

### Tableau des coefficients de couplage normalisés

Le coefficient de couplage normalisé est défini comme : **K = Uout / Uin × 100%**

| Fréquence | Non relié K (%) | Masse à une extrémité K (%) | Masse aux deux extrémités K (%) |
| --- | --- | --- | --- |
| 7 kHz | 0,28 | 0,35 | 0,35 |
| 100 kHz | 0,30 | 0,30 | 0,20 |
| 1 MHz | 1,39 | 1,33 | 0,33 |
| 5 MHz | 6,85 | 6,79 | 1,23 |
| 10 MHz | 10,00 | 8,89 | 2,50 |
| 15 MHz | 15,28 | 14,72 | 3,33 |
| 20 MHz | 19,44 | 18,33 | 4,11 |

![实验结果曲线](output.png)

**Figure 1 :** Courbe du coefficient de couplage normalisé en fonction de la fréquence pour différents modes de mise à la masse (voir output.png)

### **4.1 Caractéristiques en basse fréquence (7 kHz - 100 kHz)**

En basse fréquence, la tension de diaphonie reste très faible, entre 5,0 et 6,3 mV, et le coefficient de couplage K est toujours inférieur à 0,35%. Les résultats sont quasiment identiques pour les trois modes de mise à la masse : à 7 kHz, la masse à une ou deux extrémités donne 6,3 mV, ce qui montre que le blindage n'a pas d'effet notable à basse fréquence. À 100 kHz, la masse aux deux extrémités améliore légèrement la situation (3,5 mV contre 5,4 mV), et la tension de diaphonie diminue légèrement avec la fréquence.

### **4.2 Caractéristiques en moyenne fréquence (1 MHz - 5 MHz)**

En moyenne fréquence, la diaphonie augmente fortement, passant de 25 mV à 1 MHz à 124 mV à 5 MHz. Le blindage relié aux deux extrémités devient efficace : à 1 MHz, il réduit la diaphonie de 76% (25 mV → 6 mV), à 5 MHz de 82% (124 mV → 22,2 mV). À ce stade, la masse à une extrémité reste peu efficace, proche du non relié (amélioration de seulement 1-2 mV).

### **4.3 Caractéristiques en haute fréquence (10 MHz - 20 MHz)**

En haute fréquence, la diaphonie devient très marquée. Sans mise à la masse, la tension de diaphonie augmente fortement, de 180 mV (10 MHz) à 350 mV (20 MHz), et le coefficient de couplage atteint 19,44% à 20 MHz, soit près d'1/5 du signal d'entrée. Le blindage relié aux deux extrémités reste très efficace, avec un taux de réduction de 75-79%. À 15 MHz, la diaphonie est fortement réduite (de 275 mV à 60 mV). La masse à une extrémité est légèrement meilleure que le non relié (265 mV contre 275 mV), mais reste bien moins efficace que la masse aux deux extrémités. De plus, un déphasage entre le signal de diaphonie et le signal d'origine est observé à haute fréquence.

### **4.4 Explication théorique**

Les phénomènes observés s'expliquent par les mécanismes de couplage électromagnétique. Selon la formule de diaphonie capacitive **I = 2πFCmU** et la formule de diaphonie inductive **U = 2πFMI**, l'intensité du couplage est proportionnelle à la fréquence. À basse fréquence, la composante fréquentielle est faible, le couplage capacitif et inductif génère peu de courant et de tension de diaphonie, donc le blindage n'a pas d'effet notable.

Quand la fréquence augmente jusqu'à l'ordre du MHz, le couplage devient rapidement plus fort. Le blindage commence alors à jouer un rôle : pour la diaphonie capacitive, il agit comme un "parapluie" qui intercepte les lignes de champ électrique ; pour la diaphonie inductive, il doit former une boucle fermée avec la masse pour intercepter efficacement le champ magnétique. La masse à une extrémité ne fournit qu'une protection partielle contre le champ électrique, mais ne forme pas de boucle magnétique complète, donc son efficacité est limitée.

En haute fréquence, plusieurs effets se combinent : l'effet de peau concentre le courant haute fréquence à la surface du conducteur, le courant de retour circule par le chemin le plus court, ce qui renforce les effets d'inductance et de capacité mutuelle ; le conducteur se comporte comme une ligne de transmission, l'impédance caractéristique devient dominante ; l'énergie du couplage capacitif et inductif tend à s'équilibrer. Le déphasage observé provient de la coexistence des deux mécanismes : le couplage inductif (U en retard sur I) et le couplage capacitif (I en avance sur U), qui ont des caractéristiques de phase différentes. Le blindage relié aux deux extrémités forme une boucle complète, intercepte à la fois le champ électrique et le champ magnétique, et offre un chemin de retour à faible impédance, ce qui explique son efficacité à haute fréquence. La masse à une extrémité, en revanche, présente une impédance non négligeable à haute fréquence et ne peut intercepter efficacement les variations de flux magnétique, perdant ainsi son efficacité de blindage.
