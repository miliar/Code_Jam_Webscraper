#include <vector>
#include <string>
#include <iostream>

using namespace std;


void solve( string &s )
{
   int n = s.length();
   bool found = false;

   while (true)
   {
      found = false;

      for (int i = 0; i < n - 1; i++)
      {
         if (s[i] > s[i + 1])
         {
            found = true;
            s[i] = s[i] - 1;

            for (int j = i + 1; j < n; j++)
               s[j] = '9';
         }
      }

      if (!found)
         break;
   }
}

int main( int argc, char *argv[] )
{
   int t = 0;
   vector<string> s;   
   
   cin >> t;

   s.resize(t);

   for (int i = 0; i < t; i++)
   {
      cin >> s[i];
   }

   for (int i = 0; i < t; i++)
   {
      
      solve(s[i]);

      s[i].erase(0, s[i].find_first_not_of('0'));

      cout << "Case #" << i + 1 << ": " << s[i] << endl;
   }

   return 0;
}