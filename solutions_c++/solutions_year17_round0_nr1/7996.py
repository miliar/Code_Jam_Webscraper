#include <bits/stdc++.h>

using namespace std;

long long _();
int main() { _(); return 0; }
#define main _
#define int long long 

int main()
{
   ios_base::sync_with_stdio(false);
   int n;
   cin >> n;
   for(int i=0; i<n; i++)
   {
      string s;
      int x;
      cin >> s >> x;
      queue<int> f;
      int r = 0;
      for(int j=0; j<s.size(); j++)
      {
         if(f.size() && j - f.front() >= x)
            f.pop();
         if((s[j] == '-') ^ (f.size() % 2))
         {
            if(j > s.size() - x)
            {
               r = -1;
               break;
            }
            f.push(j);
            r++;
         }
      }
      cout << "Case #" << i+1 << ": ";
      if(r == -1)
         cout << "IMPOSSIBLE";
      else
         cout << r;
      cout << endl;
   }
   return 0;
}