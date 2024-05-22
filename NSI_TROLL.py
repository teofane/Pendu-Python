import pygame
from pygame import mixer
import random
pygame.init()
mixer.init()
screen = pygame.display.set_mode((1000, 680))
screen.fill((255, 255, 255))
font = pygame.font.Font('font/comici.ttf',40)
josh = pygame.image.load('graphics/josh.png')
josh = pygame.transform.smoothscale(josh, (60, 60))
musicJosh = pygame.mixer.Sound('audio/josh.mp3')
bad = pygame.mixer.Sound('audio/bad.mp3')
good = pygame.mixer.Sound('audio/good.mp3')
bravo = pygame.mixer.Sound('audio/bravo.mp3')
false = True
mots = ["zeppelin", "Beau", "Boxe", "Brun", "Cerf", "Chez", "Cire", "Dame", "Dent", "Dock", "Dodo", "Drap", "Dune", "Faux", "Jazz", "Joli", "Joue", "Kaki", "Logo", "Loin", "Long", "Lune", "Lynx", "Mine", "Mure", "Ours", "Pion", "Rhum", "Ride", "Rock", "Seau", "Test", "Thym", "Trou", "Truc", "User", "Vert", "Watt", "Acces", "Aimer", "Assez", "Avion", "Awale", "Balai", "Banjo", "Barbe", "Bonne", "Bruit", "Buche", "Cache", "Capot", "Carte", "Chien", "Cycle", "Essai", "Gifle", "Jambe", "Koala", "Livre", "Lourd", "Maman", "Noeud", "Ortie", "Pêche", "Poire", "Pomme", "Poste", "Prune", "Radar", "Radis", "Robot", "Route", "Rugby", "Seuil", "Taupe", "Tenue", "Texte", "Tyran", "Usuel", "Valse", "Acajou", "Agneau", "Alarme", "Ananas", "Angora", "Animal", "Arcade", "Aviron", "Azimut", "Babine", "Balade", "Basson", "Billet", "Bouche", "Boucle", "Bronze", "Cabane", "Cloche", "Cheque", "Cirage", "Coccyx", "Crayon", "Garage", "Gospel", "Goulot", "Gramme", "Grelot", "Guenon", "Hochet", "Hormis", "Humour", "Hurler", "Jargon", "Limite", "Lionne", "Menthe", "Oiseau", "Podium", "Poulpe", "Poumon", "Puzzle", "Quartz", "Rapide", "Seisme", "Tetine", "Tomate", "Whisky", "Zipper", "Abriter", "Ballast", "Baryton", "Bassine", "Batavia", "Billard", "Bretzel", "Cithare", "Chariot", "Clairon", "Corbeau", "Cortege", "Crapaud", "Cymbale", "Dentier", "Drapeau", "Exemple", "Fourmis", "Grandir", "Iceberg", "Javelot", "Jockey", "Journal", "Journee", "Jouxter", "Losange", "Macadam", "Mondial", "Notable", "Oxygene", "Panique", "Petrole", "Poterie", "Pouvoir", "Renegat", "Scooter", "Senteur", "Sifflet", "Spirale", "Sucette", "Strophe", "Tonneau", "Trousse", "Tunique", "Ukulele", "Vautour", "Zozoter", "Aquarium", "Araignee", "Arbalete", "Archipel", "Banquise", "Batterie", "Brocante", "Brouhaha", "Capeline", "Clavecin", "Cloporte", "Debutant", "Diapason", "Gangster", "Gothique", "Hautbois", "Herisson", "Logiciel", "Objectif", "Parcours", "Pastiche", "Question", "Scarabee", "Scorpion", "Tabouret", "Toujours", "Tourisme", "Triangle", "Utopique", "Accordeon", "Ascenseur", "Ascension", "Aseptiser", "Autoroute", "Avalanche", "Bilboquet", "Bourricot", "Brillance", "Cabriolet", "Contrario", "Cornemuse", "Dangereux",  "Feodalite", "Forteresse", "Gondolier", "Graphique", "Horoscope", "Intrepide", "Klaxonner", "Mascarade", "Metaphore", "Narrateur", "Peripetie", "Populaire", "Printemps", "Demander", "Tambourin", "Vestiaire", "Xylophone",  "Apocalypse", "Attraction", "Aventurier", "Bouillotte", "Citrouille", "Controverse", "Coquelicot", "Dissimuler", "Forestiere", "Grenouille", "Impossible", "Labyrinthe", "Prudemment", "Quadriceps", "Subjective", "Baccalaureat", "Abracadabra", "Francophile", "Pandemonium", "Chlorophylle", "Metallurgie", "Metamorphose", "Montgolfiere",  "Conquistador", "Conspirateur",  "Qualification",  "Sorcellerie"]
mot = mots[random.randint(0,len(mots))].lower()
mauvaisesLettres = []
phrase = font.render('Entrez une lettre', True, (0, 0, 0))
phrase1 = font.render('Le mot en contient '+str(len(mot)), True, (0, 0, 0))
lose = False
end = False
motActuel = '-'*len(mot)
def remplace(reference, actuel, lettre):
    position = []
    actuel = list(actuel)
    if lettre in reference:
        for i in range(len(reference)):
            if  lettre == reference[i]:
                position.append(i)
        for i in range(len(position)):
            actuel[position[i]] = lettre
        actuel = ''.join(actuel)
        return actuel

while false:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            false = False
        elif event.type == pygame.KEYDOWN :
            if event.key >= pygame.K_a and event.key <= pygame.K_z :
                print(event.key)
                lettre = chr(event.key)
                if lettre not in mauvaisesLettres and lettre not in motActuel and lose == False:
                    if lettre in mot:
                        motActuel = remplace(mot,motActuel,lettre)
                        good.play()
                    else:
                        mauvaisesLettres.append(lettre)
                        phrase = font.render('Les lettres ' + ' '.join(mauvaisesLettres) + ' ne sont pas dans le mot.', True, (0, 0, 0))
                        if len(mot) <= 7:
                            phrase1 = font.render(' Il vous reste '+str(11-len(mauvaisesLettres))+' essais.', True, (0, 0, 0))
                        else :
                            phrase1 = font.render(' Il vous reste '+str(14-len(mauvaisesLettres))+' essais.', True, (0, 0, 0))
                        bad.play()
                    if  motActuel == mot:
                        phrase = font.render('BRAVO, vous avez trouvé le mot.', True, (0, 0, 0))
                        phrase1 = font.render('appuyez sur a pour recommencer', True, (0, 0, 0))
                        lose = True
                        bravo.play()
                elif lose == False :
                    phrase = font.render("La lettre a déjà été essayée", True, (0, 0, 0))
                    phrase1 = font.render('', True, (0, 0, 0))
                    bad.play()
                if len(mot) <= 7:
                    if len(mauvaisesLettres) >= 11:
                        phrase = font.render('Dommage, vous avez perdu. Le mot était '+mot, True, (0, 0, 0))
                        phrase1 = font.render('Appuyez sur a pour recommencer', True, (0, 0, 0))
                        lose = True
                        end = True
                        musicJosh.play()
                else:
                    if len(mauvaisesLettres) >= 14:
                        phrase = font.render('Dommage, vous avez perdu. Le mot était '+mot, True, (0, 0, 0))
                        phrase1 = font.render('Appuyez sur a pour recommencer', True, (0, 0, 0))
                        lose = True
                        end = True
                        musicJosh.play()
                if lose == True and lettre == 'a':
                    mauvaisesLettres = []
                    mot = mots[random.randint(0,len(mots))].lower()
                    motActuel = '-'*len(mot)
                    phrase = font.render('Entrez une lettre', True, (0, 0, 0))
                    phrase1 = font.render('Le mot en contient '+str(len(mot)), True, (0, 0, 0))
                    lose = False
                screen.fill((255, 255, 255))
    if len(mot) <= 7 :
        if len(mauvaisesLettres) >= 1:
            pygame.draw.lines(screen, (0,0,0), True, [(50,550),(390,550)], 5)
        if len(mauvaisesLettres) >= 2 :
            pygame.draw.lines(screen, (0,0,0), True, [(220,550),(220,130)], 5)
        if len(mauvaisesLettres) >= 3 :
            pygame.draw.lines(screen, (0,0,0), True, [(220,130),(500,130)], 5)
        if len(mauvaisesLettres) >= 4 :
            pygame.draw.lines(screen, (0,0,0), True, [(220,180),(260,130)], 5)
        if len(mauvaisesLettres) >= 5 :
            pygame.draw.lines(screen, (0,0,0), True, [(500,130),(500,180)], 5)
        if len(mauvaisesLettres) >= 6 :
            pygame.draw.circle(screen, (0,0,0), (500,205), 25,5)
        if len(mauvaisesLettres) >= 7 :
            pygame.draw.lines(screen, (0,0,0), True, [(500,230),(500,310)], 5)
        if len(mauvaisesLettres) >= 8 :
            pygame.draw.lines(screen, (0,0,0), True, [(500,250),(460,290)], 5)
        if len(mauvaisesLettres) >= 9 :
            pygame.draw.lines(screen, (0,0,0), True, [(500,250),(540,290)], 5)
        if len(mauvaisesLettres) >= 10 :
            pygame.draw.lines(screen, (0,0,0), True, [(500,310),(460,350)], 5)
        if len(mauvaisesLettres) >= 11 :
            pygame.draw.lines(screen, (0,0,0), True, [(500,310),(540,350)], 5) 
            josh1 = josh.get_rect(center = (500,205)) 
            screen.blit(josh, josh1)
    else :
        if len(mauvaisesLettres) >= 1:
            pygame.draw.lines(screen, (0,0,0), True, [(50,550),(390,550)], 5)
        if len(mauvaisesLettres) >= 2 :
            pygame.draw.lines(screen, (0,0,0), True, [(220,550),(220,130)], 5)
        if len(mauvaisesLettres) >= 3 :
            pygame.draw.lines(screen, (0,0,0), True, [(190,550),(220,500)], 5)
        if len(mauvaisesLettres) >= 4 :
            pygame.draw.lines(screen, (0,0,0), True, [(250,550),(220,510)], 5)
        if len(mauvaisesLettres) >= 5 :
            pygame.draw.lines(screen, (0,0,0), True, [(220,130),(360,130)], 5)
        if len(mauvaisesLettres) >= 6 :
            pygame.draw.lines(screen, (0,0,0), True, [(360,130),(500,130)], 5)
        if len(mauvaisesLettres) >= 7 :
            pygame.draw.lines(screen, (0,0,0), True, [(220,180),(260,130)], 5)
        if len(mauvaisesLettres) >= 8 :
            pygame.draw.lines(screen, (0,0,0), True, [(500,130),(500,180)], 5)
        if len(mauvaisesLettres) >= 9 :
            pygame.draw.circle(screen, (0,0,0), (500,205), 25,5)
        if len(mauvaisesLettres) >= 10 :
            pygame.draw.lines(screen, (0,0,0), True, [(500,230),(500,310)], 5)
        if len(mauvaisesLettres) >= 11 :
            pygame.draw.lines(screen, (0,0,0), True, [(500,250),(460,290)], 5)
        if len(mauvaisesLettres) >= 12 :
            pygame.draw.lines(screen, (0,0,0), True, [(500,250),(540,290)], 5)
        if len(mauvaisesLettres) >= 13 :
            pygame.draw.lines(screen, (0,0,0), True, [(500,310),(460,350)], 5)
        if len(mauvaisesLettres) >= 14 :
            pygame.draw.lines(screen, (0,0,0), True, [(500,310),(540,350)], 5) 
            josh1 = josh.get_rect(center = (500,205)) 
            screen.blit(josh, josh1)
    screen.blit(phrase, (0, 0))
    screen.blit(phrase1, (0, 50))
    screen.blit( font.render('Le mot est '+ motActuel, True, (0, 0, 0)),(600,600))
    pygame.display.update()