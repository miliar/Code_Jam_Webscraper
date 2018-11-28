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
const int N   = 1e6 + 10;

struct POINT {
   int x;
   int y;
   //POINT(){}
   //POINT(int x, int y): x(x), y(y){}
   //bool operator < (const POINT &e) const { return x < e.x || x == e.x && y < e.y; }
} p[N];

int n, k, m, t;
int a[10], tick[10];
char c[10];

int main() {
   //ios_base::sync_with_stdio(0);
   //cout.tie(0); cin.tie(0);
   
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);

   cin >> t;
   
   fru(T, 1, t)
   {
      int n;
      cin >> n;
      
      c[1] = 'R';
      c[2] = 'O';
      c[3] = 'Y';
      c[4] = 'G';
      c[5] = 'B';
      c[6] = 'V';
      
      m = 6;
      fru(i, 1, m) cin >> a[i];
      fru(i, 1, m) tick[i] = 0;
      
      string res = "";
      char pred  = 'X';
      bool flag  = true;
      fru(h, 1, n)
      {
         int ind = -1;
         fru(i, 1, m) if(c[i] != pred && a[i] > 0 && (ind == -1 || a[i] > a[ind] || a[i] == a[ind] && h > 1 && c[i] == res[0]))
            ind = i;
         
         if(ind == -1)
            flag = false;
         else
         {
            res += c[ind];
            pred = c[ind];
            tick[ind] = h;
            a[ind]--;
         }
      }
      
      if(res[0] == res[n - 1] || n > 1 && res[n - 1] == res[n])
         flag = false;
      
      if(flag)
         cout << "Case #" << T << ": " << res << "\n";
      else
         cout << "Case #" << T << ": " << "IMPOSSIBLE" << "\n";
   }
   
   return 0;
}