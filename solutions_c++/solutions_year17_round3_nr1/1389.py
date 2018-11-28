#include <iostream>
#include <iomanip>  
#include <stdio.h>
#include <map>
#include <string>
#include <vector>
#include <queue>   
#include <algorithm>
#include <math.h>
#include <set>
#include <stdlib.h>
#include <stack> 
using namespace std;

#define fr(i,n)    for(int i=0;i<n;i++)
#define fru(i,a,b) for(int i=a;i<=b;i++)
#define frd(i,a,b) for(int i=a;i>=b;i--)

typedef long long   ll;
typedef long double ld;
	
const int INF = 2e9 + 10;
const int MOD = 1e9 + 7;
const int N   = 1e4 + 10;

struct POINT {
   ld r;
   ld h;
   ld v;
   //POINT(){}
   //POINT(int x, int y): x(x), y(y){}
   bool operator < (const POINT &e) const { return v > e.v || v == e.v && r > e.r; }
} p[N];

int n, k, m, t;

int main() {
   //ios_base::sync_with_stdio(0);
   //cout.tie(0); cin.tie(0);
   
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);

   cin >> t;
   
   fru(T, 1, t)
   {
      cin >> n >> k;
      fru(i, 1, n) 
      {
         cin >> p[i].r >> p[i].h;
         p[i].v = p[i].r * p[i].h * acos(-1.0) * 2LL;
      }
      
      sort(p + 1, p + 1 + n);
      
      ld ans = 0;
      fru(i, 1, n)
      {
         int cnt = 1;
         ld res  = p[i].h * p[i].r * acos(-1.0) * 2LL;
         res    += p[i].r * p[i].r * acos(-1.0);
         
         fru(j, 1, n)
         {
            if(cnt == k)
               break;
               
            if(p[i].r < p[j].r || i == j)
               continue;
            
            cnt++;
            res += p[j].v;
            
            if(cnt == k)
               break;
         }

         if(cnt == k)
            ans = max(ans, res);
      }
      
      cout << "Case #" << T << ": "; cout << fixed << setprecision(9) << ans << "\n";
   }
   
   return 0;
}