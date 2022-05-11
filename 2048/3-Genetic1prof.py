from Game import Game
import random

def produitHadamard(grille, PONDERATION):
    val = 0
    for i in range(4):
        for j in range(4):
            val += PONDERATION[i][j]*grille[i][j]
    return val

def prof1(PONDERATION):
    game = Game()
    jeux_possible, possibilite, score = game.info()
    while jeux_possible:
        def eval_prof(x):
            game_x = game.variante()
            game_x.deplacement(x)
            return produitHadamard(game_x.grille, PONDERATION)

        possibilite.sort(key=eval_prof)
        x = possibilite[0]
        jeux_possible, possibilite, score = game.jeux(x)
    return score

# Genetique

# Creation
def creation():
    return [[random.random() for _ in range(4)] for _ in range(4)]

# Selection
def selection(population, m=30):
    n = len(population)
    for i in range(n):
        score, indiv = population[i]
        if score == -1:
            scores = []
            for _ in range(10):
                scores.append(prof1(indiv))
            population[i] = (sum(scores)/len(scores), indiv)
    population.sort(key=lambda x: x[0], reverse=True)
    return population[:m]

# Mutation
def cross(x1, x2):
    return [[random.choice([x1[i][j], x2[i][j]]) for j in range(4)] for i in range(4)]

def mutation(population, m=30):
    n = len(population)
    for _ in range(m):
        x1 = population[random.randint(0, n-1)][1]
        x2 = population[random.randint(0, n-1)][1]
        population.append((-1, cross(x1, x2)))
    return population

# Ajout
def ajout(population, m=40):
    for _ in range(m):
        population.append((-1, creation()))
    return population

# Execution
population = ajout([], 100)

for i in range(50):
    population = selection(population)
    print(f"{i} : {population[0][0]}")
    population = mutation(population)
    population = ajout(population)

population = selection(population)
for x in population:
    print(x)


"""
(1116, [[0.0031360273723379795, 0.0038036840396924454, 0.8362047496381709, 0.5005115699652146], [0.08378046404531869, 0.2821458711732301, 0.14593797463021096, 0.9637586117538086], [0.12669434687602033, 0.31450380062594985, 0.35894420863442555, 0.5769721117206498], [0.17426886386158935, 0.2859546307937846, 0.23916389252379333, 0.5818037482702322]])
(1110, [[0.32316273339269386, 0.7768783712674424, 0.843065098896815, 0.5499279837992633], [0.27902548846106556, 0.2821458711732301, 0.8030004672818518, 0.9436234660668364], [0.10343101264553878, 0.15423213406615965, 0.5087835010673643, 0.7061905331922921], [0.08437891451749813, 0.17269554788498587, 0.6333179087612547, 0.5204092707878138]])
(1080, [[0.913004147154441, 0.7768783712674424, 0.843065098896815, 0.4742151146453767], [0.08378046404531869, 0.2821458711732301, 0.34808185994441865, 0.9637586117538086], [0.09361495786291951, 0.31450380062594985, 0.5087835010673643, 0.7061905331922921], [0.08437891451749813, 0.25238813990820685, 0.21834949572452889, 0.8668282540890733]])
(998, [[0.9295935634014837, 0.7523189401568207, 0.2810458390178331, 0.6413238741651223], [0.33250689681887025, 0.3432751875530968, 0.34808185994441865, 0.9637586117538086], [0.12669434687602033, 0.31450380062594985, 0.35894420863442555, 0.8073799187252859], [0.08437891451749813, 0.17269554788498587, 0.21834949572452889, 0.765816986982538]])
(972, [[0.913004147154441, 0.7768783712674424, 0.843065098896815, 0.4742151146453767], [0.27902548846106556, 0.2821458711732301, 0.34808185994441865, 0.9637586117538086], [0.12669434687602033, 0.31450380062594985, 0.5087835010673643, 0.7061905331922921], [0.08437891451749813, 0.44795600543433955, 0.11466317045539243, 0.5204092707878138]])
(960, [[0.913004147154441, 0.7523189401568207, 0.9709528773680715, 0.5005115699652146], [0.33250689681887025, 0.2821458711732301, 0.34808185994441865, 0.9637586117538086], [0.09361495786291951, 0.15423213406615965, 0.35894420863442555, 0.7061905331922921], [0.08437891451749813, 0.17269554788498587, 0.11466317045539243, 0.5204092707878138]])
(920, [[0.0031360273723379795, 0.0038036840396924454, 0.9709528773680715, 0.525319811941164], [0.08378046404531869, 0.4758976299778578, 0.14593797463021096, 0.706855566607136], [0.09361495786291951, 0.5304366293657483, 0.35894420863442555, 0.5769721117206498], [0.17426886386158935, 0.2859546307937846, 0.23916389252379333, 0.5818037482702322]])
(910, [[0.913004147154441, 0.7768783712674424, 0.843065098896815, 0.4742151146453767], [0.33250689681887025, 0.2821458711732301, 0.34808185994441865, 0.9637586117538086], [0.12669434687602033, 0.31450380062594985, 0.5087835010673643, 0.7061905331922921], [0.08437891451749813, 0.25238813990820685, 0.11466317045539243, 0.5204092707878138]])
(904, [[0.32316273339269386, 0.7523189401568207, 0.8362047496381709, 0.5005115699652146], [0.08378046404531869, 0.2821458711732301, 0.34808185994441865, 0.9436234660668364], [0.12669434687602033, 0.31450380062594985, 0.5087835010673643, 0.7061905331922921], [0.08437891451749813, 0.25238813990820685, 0.21834949572452889, 0.765816986982538]])
(872, [[0.913004147154441, 0.7523189401568207, 0.9709528773680715, 0.5005115699652146], [0.33250689681887025, 0.2821458711732301, 0.34808185994441865, 0.9637586117538086], [0.12669434687602033, 0.15423213406615965, 0.5087835010673643, 0.7061905331922921], [0.08437891451749813, 0.25238813990820685, 0.11466317045539243, 0.5204092707878138]])
(870, [[0.9295935634014837, 0.06112516523437439, 0.2810458390178331, 0.5005115699652146], [0.33250689681887025, 0.3432751875530968, 0.34808185994441865, 0.9689465542809006], [0.12669434687602033, 0.31450380062594985, 0.2943524678595283, 0.8073799187252859], [0.08437891451749813, 0.25238813990820685, 0.21834949572452889, 0.8668282540890733]])
(836, [[0.913004147154441, 0.7980436354744505, 0.8362047496381709, 0.5005115699652146], [0.010917623890870365, 0.599790366551723, 0.9527591365178582, 0.33839061081309485], [0.12669434687602033, 0.15423213406615965, 0.44706261501131817, 0.8073799187252859], [0.08437891451749813, 0.44917668016105505, 0.892010537182074, 0.033160524512034883]])
(834, [[0.913004147154441, 0.7523189401568207, 0.6643966856750206, 0.6413238741651223], [0.08378046404531869, 0.3432751875530968, 0.22337796513519537, 0.9436234660668364], [0.12669434687602033, 0.31450380062594985, 0.5087835010673643, 0.7061905331922921], [0.08437891451749813, 0.17269554788498587, 0.11466317045539243, 0.5204092707878138]])
(828, [[0.5363638079149828, 0.29237197786176816, 0.06098032093466532, 0.07776204086589367], [0.010912037213370196, 0.4180977577770004, 0.19612009428450727, 0.33356855238827887], [0.3769572915483135, 0.8409444193024971, 0.7030676255333301, 0.02793879793292564], [0.6498421872553308, 0.7493263749546701, 0.740066227461256, 0.06157814174657772]])
(820, [[0.0031360273723379795, 0.0038036840396924454, 0.8362047496381709, 0.5005115699652146], [0.08378046404531869, 0.2821458711732301, 0.14593797463021096, 0.9637586117538086], [0.12669434687602033, 0.31450380062594985, 0.35894420863442555, 0.5769721117206498], [0.17426886386158935, 0.2859546307937846, 0.21834949572452889, 0.8668282540890733]])
(806, [[0.913004147154441, 0.7980436354744505, 0.8362047496381709, 0.5005115699652146], [0.010917623890870365, 0.599790366551723, 0.34808185994441865, 0.33839061081309485], [0.12669434687602033, 0.15423213406615965, 0.44706261501131817, 0.8073799187252859], [0.08437891451749813, 0.44917668016105505, 0.21834949572452889, 0.8668282540890733]])
(806, [[0.913004147154441, 0.7523189401568207, 0.9709528773680715, 0.5005115699652146], [0.33250689681887025, 0.3432751875530968, 0.34808185994441865, 0.9637586117538086], [0.09361495786291951, 0.15423213406615965, 0.35894420863442555, 0.7061905331922921], [0.08437891451749813, 0.17269554788498587, 0.11466317045539243, 0.765816986982538]])
(804, [[0.32316273339269386, 0.7523189401568207, 0.6643966856750206, 0.6413238741651223], [0.08378046404531869, 0.2821458711732301, 0.22337796513519537, 0.9436234660668364], [0.12669434687602033, 0.31450380062594985, 0.5087835010673643, 0.7061905331922921], [0.08437891451749813, 0.25238813990820685, 0.21834949572452889, 0.5204092707878138]])
(800, [[0.913004147154441, 0.7523189401568207, 0.6643966856750206, 0.6413238741651223], [0.08378046404531869, 0.2821458711732301, 0.22337796513519537, 0.9436234660668364], [0.12669434687602033, 0.31450380062594985, 0.5087835010673643, 0.7061905331922921], [0.08437891451749813, 0.25238813990820685, 0.11466317045539243, 0.5204092707878138]])
(790, [[0.913004147154441, 0.7523189401568207, 0.9709528773680715, 0.6413238741651223], [0.33250689681887025, 0.3432751875530968, 0.34808185994441865, 0.9637586117538086], [0.09361495786291951, 0.31450380062594985, 0.35894420863442555, 0.7061905331922921], [0.08437891451749813, 0.17269554788498587, 0.11466317045539243, 0.765816986982538]])
(782, [[0.9295935634014837, 0.7523189401568207, 0.2810458390178331, 0.5005115699652146], [0.08378046404531869, 0.2821458711732301, 0.22337796513519537, 0.9436234660668364], [0.12669434687602033, 0.31450380062594985, 0.5087835010673643, 0.7061905331922921], [0.08437891451749813, 0.25238813990820685, 0.11466317045539243, 0.5204092707878138]])
(774, [[0.913004147154441, 0.7523189401568207, 0.9709528773680715, 0.6413238741651223], [0.08378046404531869, 0.2821458711732301, 0.34808185994441865, 0.9637586117538086], [0.09361495786291951, 0.31450380062594985, 0.5087835010673643, 0.7061905331922921], [0.08437891451749813, 0.25238813990820685, 0.21834949572452889, 0.8668282540890733]])
(772, [[0.9295935634014837, 0.7523189401568207, 0.8362047496381709, 0.5005115699652146], [0.33250689681887025, 0.7011348792831975, 0.34808185994441865, 0.9689465542809006], [0.12669434687602033, 0.31450380062594985, 0.2943524678595283, 0.8073799187252859], [0.08437891451749813, 0.25238813990820685, 0.21834949572452889, 0.8668282540890733]])
(772, [[0.913004147154441, 0.7768783712674424, 0.843065098896815, 0.4742151146453767], [0.27902548846106556, 0.2821458711732301, 0.34808185994441865, 0.9436234660668364], [0.12669434687602033, 0.31450380062594985, 0.5087835010673643, 0.7061905331922921], [0.08437891451749813, 0.25238813990820685, 0.11466317045539243, 0.5204092707878138]])
(768, [[0.9295935634014837, 0.7523189401568207, 0.9709528773680715, 0.5005115699652146], [0.33250689681887025, 0.3432751875530968, 0.34808185994441865, 0.4360627441385726], [0.12669434687602033, 0.31450380062594985, 0.2943524678595283, 0.1641729126261564], [0.7697847901761211, 0.25238813990820685, 0.21834949572452889, 0.04565517726722779]])
(754, [[0.32316273339269386, 0.7768783712674424, 0.843065098896815, 0.5499279837992633], [0.27902548846106556, 0.2821458711732301, 0.22337796513519537, 0.9436234660668364], [0.10343101264553878, 0.31450380062594985, 0.5087835010673643, 0.7061905331922921], [0.08437891451749813, 0.17269554788498587, 0.11466317045539243, 0.5204092707878138]])
(754, [[0.913004147154441, 0.7768783712674424, 0.843065098896815, 0.4742151146453767], [0.33250689681887025, 0.2821458711732301, 0.34808185994441865, 0.9637586117538086], [0.12669434687602033, 0.31450380062594985, 0.5087835010673643, 0.7061905331922921], [0.08437891451749813, 0.25238813990820685, 0.11466317045539243, 0.5204092707878138]])
(752, [[0.32316273339269386, 0.7768783712674424, 0.843065098896815, 0.5499279837992633], [0.27902548846106556, 0.2821458711732301, 0.8030004672818518, 0.9436234660668364], [0.10343101264553878, 0.15423213406615965, 0.5087835010673643, 0.7061905331922921], [0.08437891451749813, 0.17269554788498587, 0.11466317045539243, 0.5204092707878138]])
(748, [[0.32316273339269386, 0.7523189401568207, 0.843065098896815, 0.5499279837992633], [0.27902548846106556, 0.7011348792831975, 0.34808185994441865, 0.9436234660668364], [0.10343101264553878, 0.31450380062594985, 0.2943524678595283, 0.7061905331922921], [0.08437891451749813, 0.17269554788498587, 0.21834949572452889, 0.8668282540890733]])
(734, [[0.913004147154441, 0.7523189401568207, 0.8362047496381709, 0.5005115699652146], [0.33250689681887025, 0.2821458711732301, 0.34808185994441865, 0.9637586117538086], [0.09361495786291951, 0.31450380062594985, 0.5087835010673643, 0.8073799187252859], [0.08437891451749813, 0.25238813990820685, 0.21834949572452889, 0.765816986982538]])

"""