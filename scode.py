
class EightQueensGA:
     
      def random_solution(self):    #لیستی از موقعیت وزیرها    
        """ایجاد یک راه‌حل تصادفی."""
        return random.sample(range(self.n), self.n)


      def initialize_population(self):
        """ایجاد جمعیت اولیه به صورت تصادفpp."""
        return [self.random_solution() for _ in range(self.population_size)]
      
      def calculate_fitness(self, solution):
        """محاسبه برازندگی یک راه‌حل."""
        clashes = 0      #شمارش تداخل ها
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if solution[i] == solution[j] or abs(solution[i] - solution[j]) == j - i: #بررسی تداخل
                    clashes += 1
        return 28 - clashes  # برازندگی حداکثر 28 برای 8 وزیر

     def select_parents(self):
        """ انتخاب والدین برای تولیدنسل بعد  ."""
        fitness_scores = [(self.calculate_fitness(sol), sol) for sol in self.population]
        fitness_scores.sort(key=lambda x: x[0], reverse=True)
        selected = [sol for _, sol in fitness_scores[:self.population_size // 2]]
        return selected
