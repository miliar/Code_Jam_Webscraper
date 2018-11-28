#include <iostream>
#include <string>
#include <vector>


using namespace std;

bool is_sorted(string & number)
{
   for (size_t i = 0; i < number.size() - 1; ++i)
   {
      if (number[i] > number[i+1])
      {
         return false;
      }
   }
   return true;
}

void numbers_problem()
{
   size_t num_tests;
   cin >> num_tests;
   for (size_t i = 0; i < num_tests; ++i)
   {
      string number;
      cin >> number;
      cout << "Case #" << i + 1 << ": ";
      while (not is_sorted(number))
      {
         size_t j = 0;
         while (j < number.size() - 1 and number[j] <= number[j+1])
         {
            ++j;
         }
         --number[j];
         for (size_t k = j + 1; k < number.size(); ++k)
         {
            number[k] = '9';
         }
      }
      size_t j = 0;
      for (; number[j] == '0'; ++j);
      {
      }
      cout << number.substr(j) << endl;
   }
}

int main()
{
   numbers_problem();
   return 0;
}