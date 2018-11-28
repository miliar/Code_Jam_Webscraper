#include <bits/stdc++.h>

using namespace std;

long long _();
int main() { _(); return 0; }
#define main _
#define int long long 

const int P = 4;

int p;

void choose(int c[P], int v, int& cur)
{
   c[v]--;
   cur = (cur + v) % p;
}

int main()
{
   ios_base::sync_with_stdio(false);
   int T;
   cin >> T;
   for(int test=1; test<=T; test++)
   {
      int n;
      cin >> n >> p;
      int c[P] = {0};
      for(int i=0; i<n; i++)
      {
         int x;
         cin >> x;
         c[x%p]++;
      }
      /*int r = c[0] + min(c[1], c[2]);
      if(p == 2)
         r += (c[1]+1)/2;
      else
      {
         if(c[1] > c[2])
            r += (c[1]-c[2])/3
      }*/
      int r = c[0];
      int cur = 0;
      while(c[1] || c[2])
      {
         if(cur == 0)
            r++;
         if(p == 2)
            choose(c, 1, cur);
         else if(p == 3)
         {
            if(c[1] && c[2])
               c[1]--, c[2]--;
            else if(c[1])
               choose(c, 1, cur);
            else
               choose(c, 2, cur);
         }
      }
      cout << "Case #" << test << ": " << r << endl;
   }
   return 0;
}