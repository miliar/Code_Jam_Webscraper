#include <iostream>
#include <string>
#include <vector>

typedef unsigned long long ull;

using namespace std;

void bathroom_problem()
{
   ull num_tests, num_persons, num_stalls;
   cin >> num_tests;
   for (size_t i = 0; i < num_tests; ++i)
   {
      cin >> num_stalls >> num_persons;
      cout << "Case #" << i + 1 << ": ";
      ull count_high, min, max, pow2, current;
      pow2 = 1;
      current = 1;
      min = (num_stalls - 1) / 2;
      max = num_stalls / 2;
      if (num_persons == 1)
      {
         cout << max << " " << min << endl;
      }
      else
      {
         count_high = min < max ? 1 : 0;
         bool done;
         while (not done)
         {
            pow2 *= 2;
            if (num_persons <= current + count_high)
            {
               cout << max / 2 << " " << (max - 1) / 2 << endl;
               break;
            } else if (num_persons <= current + pow2)
            {
               cout << min / 2 << " " << (min - 1) / 2 << endl;
               break;
            } else
            {
               ull tmp = 0;
               if ((min - 1) / 2 < min / 2) //min even
               {
                  tmp += 2 * count_high + (pow2 - count_high);
               } else if ((max - 1) / 2 < max / 2)
               {
                  tmp += count_high;
               }
               count_high = tmp;
               min = (min - 1) / 2;
               max = max / 2;
               current += pow2;
            }
         }
      }
   }
}

int main()
{
   bathroom_problem();
   return 0;
}