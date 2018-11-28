#include <iostream>
#include <string>

using namespace std;

void update(std::string& s, int start, int end)
{
   for (int i = start; i < end; i++) {
      if (s[i] == '-') {
         s[i] = '+';
      } else if (s[i] == '+') {
         s[i] = '-';
      }
   }
}

std::string flip(std::string& s, int k)
{
   int flips = 0;
   int i = 0;

   while (i < s.length() - k + 1) {
      if (s[i] == '-') {
         update(s, i, i + k);
         flips += 1;
      }
      i += 1;
   }
   for (int i = 0; i < s.length(); i++) {
      if (s[i] == '-') {
         return "IMPOSSIBLE";
      }
   }
   return std::to_string(flips);
}

int main()
{
   int t, k;
   std::string s;
   cin >> t;

   for (int i = 1; i <= t; ++i) {
      cin >> s >> k;
      cout << "Case #" << i << ": " << flip(s, k) << endl;
   }
}
