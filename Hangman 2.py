import random
from typing import Set, List

class Hangman:
    """Jeu du pendu en Python"""
    
    WORDS = {
        "animaux": ["ELEPHANT", "GIRAFE", "CROCODILE", "PAPILLON", "KANGOUROU", 
                   "HERISSON", "DAUPHIN", "PERROQUET", "TORTUE", "ECUREUIL"],
        "pays": ["FRANCE", "BRESIL", "JAPON", "CANADA", "ESPAGNE", "EGYPTE", 
                "ARGENTINE", "NORVEGE", "MEXIQUE", "PORTUGAL"],
        "fruits": ["ABRICOT", "BANANE", "FRAMBOISE", "CITRON", "ARTICHAUT", 
                  "COURGETTE", "GRENADE", "MANGUE", "POTIRON", "RADIS"],
        "metiers": ["BOULANGER", "POMPIER", "AVOCAT", "PLOMBIER", "JARDINIER", 
                   "MENUISIER", "DENTISTE", "FACTEUR", "PECHEUR", "MUSICIEN"]
    }
    
    HANGMAN_DRAWING = [
        """
           ------
           |    |
           |
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   \\|
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   \\|/
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |   / \\
        --------
        """
    ]
    
    def __init__(self):
        self.word = ""
        self.guessed_letters: Set[str] = set()
        self.errors = 0
        self.max_errors = 6
        self.game_over = False
        self.won = False
        
    def start_game(self, category: str = None) -> None:
        """Démarre une nouvelle partie"""
        if category is None:
            category = self._choose_category()
        
        words = self.WORDS.get(category, self.WORDS["animaux"])
        self.word = random.choice(words)
        self.guessed_letters = set()
        self.errors = 0
        self.game_over = False
        self.won = False
        
    def _choose_category(self) -> str:
        """Permet à l'utilisateur de choisir une catégorie"""
        print("\n🎮 Bienvenue au jeu du Pendu !\n")
        print("Catégories disponibles:")
        categories = list(self.WORDS.keys())
        for i, cat in enumerate(categories, 1):
            print(f"  {i}. {cat.capitalize()}")
        
        while True:
            try:
                choice = int(input("\nChoisir une catégorie (1-4): "))
                if 1 <= choice <= len(categories):
                    return categories[choice - 1]
                print("❌ Choix invalide!")
            except ValueError:
                print("❌ Veuillez entrer un numéro!")
    
    def display_word(self) -> str:
        """Affiche le mot avec les lettres devinées"""
        return " ".join([letter if letter in self.guessed_letters else "_" 
                        for letter in self.word])
    
    def display_game_state(self) -> None:
        """Affiche l'état actuel du jeu"""
        print("\n" + "="*40)
        print(self.HANGMAN_DRAWING[self.errors])
        print("="*40)
        print(f"Mot: {self.display_word()}")
        print(f"Erreurs: {self.errors}/{self.max_errors}")
        print(f"Lettres essayées: {', '.join(sorted(self.guessed_letters)) or 'Aucune'}")
        print("="*40)
    
    def guess_letter(self, letter: str) -> bool:
        """
        Traite une tentative de lettre
        Retourne True si la lettre est correcte, False sinon
        """
        letter = letter.upper()
        
        # Validation
        if len(letter) != 1 or not letter.isalpha():
            print("❌ Entrez une seule lettre!")
            return None
        
        if letter in self.guessed_letters:
            print("⚠️  Vous avez déjà essayé cette lettre!")
            return None
        
        self.guessed_letters.add(letter)
        
        if letter in self.word:
            print(f"✅ Bien ! La lettre '{letter}' est dans le mot !")
            return True
        else:
            self.errors += 1
            print(f"❌ La lettre '{letter}' n'est pas dans le mot !")
            return False
    
    def is_word_guessed(self) -> bool:
        """Vérifie si le mot est entièrement deviné"""
        return all(letter in self.guessed_letters for letter in self.word)
    
    def is_game_over(self) -> bool:
        """Vérifie si la partie est terminée"""
        if self.is_word_guessed():
            self.game_over = True
            self.won = True
            return True
        
        if self.errors >= self.max_errors:
            self.game_over = True
            self.won = False
            return True
        
        return False
    
    def play(self) -> None:
        """Boucle principale du jeu"""
        self.start_game()
        
        while not self.is_game_over():
            self.display_game_state()
            
            guess = input("\nDevinez une lettre: ")
            self.guess_letter(guess)
        
        # Affichage final
        self.display_game_state()
        
        if self.won:
            print("\n🎉 BRAVO ! Vous avez gagné !")
            print(f"Le mot était: {self.word}")
        else:
            print("\n💀 PERDU ! C'est dommage...")
            print(f"Le mot était: {self.word}")
        
        # Demander si rejouer
        if input("\nVoulez-vous rejouer? (o/n): ").lower() == 'o':
            self.play()
        else:
            print("\n👋 Merci d'avoir joué !")


def main():
    """Point d'entrée du jeu"""
    game = Hangman()
    game.play()


if __name__ == "__main__":
    main()