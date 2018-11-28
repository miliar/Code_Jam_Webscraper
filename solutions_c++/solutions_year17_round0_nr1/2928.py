#include <iostream>
#include <vector>
#include <string>

using namespace std;

void pancake_problem()
{
   size_t num_tests;
   cin >> num_tests;
   cerr << "Read tests" << endl;
   for (size_t i = 0; i < num_tests; ++i)
   {
      string pancakes;
      cin >> pancakes;
      cerr << "Read string" << endl;
      size_t flipper_size;
      cin >> flipper_size;
      cerr << "Read size" << endl;
      cout << "Case #" << i + 1 << ": ";
      size_t num_flips = 0;
      for (size_t j = 0; j < pancakes.size() - flipper_size + 1; ++j)
      {
         if (pancakes[j] == '-')
         {
            ++num_flips;
            for (size_t k = j; k < j + flipper_size; ++k)
            {
               pancakes[k] = pancakes[k] == '-' ? '+' : '-';
            }
         }
      }
      bool okay = true;
      for (size_t j = 0; j < pancakes.size(); ++j)
      {
         if (pancakes[j] == '-')
         {
            okay = false;
            break;
         }
      }
      if (okay)
      {
         cout << num_flips << endl;
      }
      else
      {
         cout << "IMPOSSIBLE" << endl;
      }
   }
}

int main()
{
   pancake_problem();
   return 0;
}