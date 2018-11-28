#include <string>
#include <vector>
#include <iostream>

using namespace std;

void flip( char *c )
{
   char val = *c;

   if (val == '-')
      *c = '+';

   if (val == '+')
      *c = '-';
}

int solve( std::string &s, int k )
{
   int n = s.length(), wn = n - k + 1;

   bool flipped = true;

   for (int i = 0; i < n; i++)
   {
      if (s[i] != '+')
      {
         flipped = false;
         break;
      }
   }

   if (flipped)
      return 0;

   int ans = 0;

   for (int i = 0; i < n; i++)
   {
      if (s[i] == '-')
      {
         if (i > n - k)
            return -1;

         for (int j = 0; j < k; j++)
         {
            flip(&s[j + i]);
         }

         ans++;
      }
   }

   return ans;
}

int main( int argc, char *argv[] )
{
   int t = 0;
   vector<string> s;
   vector<int> k;

   cin >> t;

   k.resize(t);
   s.resize(t);

   for (int i = 0; i < t; i++)
   {
      cin >> s[i];
      cin >> k[i];
   }

   for (int i = 0; i < t; i++)
   {
      int ans = solve(s[i], k[i]);

      if (ans >= 0)
         cout << "Case #" << i + 1 << ": " << ans << endl;
      else
         cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
   }

   return 0;
}