#include <bits/stdc++.h>

using namespace std;

long long _();
int main() { _(); return 0; }
#define main _
#define int long long 

int main()
{
   ios_base::sync_with_stdio(false);
   int T;
   cin >> T;
   for(int test=1; test<=T; test++)
   {
      string s;
      cin >> s;
      int i = 0;
      for(; i<s.size()-1; i++)
         if(s[i] > s[i+1])
            break;
      string r = s;
      if(i < s.size()-1)
      {
         if(s[i] != '1')
         {
            while(i > 0 && s[i] == s[i-1])
               i--;
            s[i]--;
            for(int j=i+1; j<s.size(); j++)
               s[j] = '9';
         }
         else
            s = string(s.size()-1, '9');
      }
      cout << "Case #" << test << ": " << s << endl;
   }
   return 0;
}