class EightQueensGA:
     def initialize_population(self):
        """ایجاد جمعیت اولیه به صورت تصادفی."""
        return [self.random_solution() for _ in range(self.population_size)]
