#include <climits>
#include <cmath>
#include <iostream>
#include <string>

using namespace std;

std::string tidy(std::string s)
{
   int n = s.length();
   for (int i = n - 2; i >= 0; i--) {
      if (s[i] > s[i + 1] || s[0] > s[i]) {
         s[i + 1] = '9';
         s[i] -= 1;
      }
   }
   s.erase(0, s.find_first_not_of('0'));
   return s;
}

int main()
{
   int t;
   std::string s;
   cin >> t;

   for (int i = 1; i <= t; ++i) {
      cin >> s;
      cout << "Case #" << i << ": " << tidy(s) << endl;
   }
}
