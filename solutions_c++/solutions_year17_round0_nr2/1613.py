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
const int N   = 200 + 10;

int t;

int main() {
   //ios_base::sync_with_stdio(0);
   //cout.tie(0); cin.tie(0);
   
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);

   cin >> t;
   fru(T, 1, t)
   {
      ll n; cin >> n;

      int a[105];
      fill(a, a + 100, 0);
      
      int cnt = 0;
      while(n > 0)
      {
         cnt++;
         a[cnt] = n % 10;
         n /= 10;
      }
      
      reverse(a + 1, a + 1 + cnt);
      
      while(true)
      {
         int flag   = true;
         int mx     = 0;
         int badind = 1;
         fru(i, 1, cnt)
         {
            if(mx > a[i])
            {
               flag   = false;
               badind = i;
               break;
            }
            
            mx = max(mx, a[i]);
         }
         
         if(flag)
            break;
         else
         {
            a[badind - 1]--;
            fru(i, badind, cnt)
               a[i] = 9;
         }
      }  
      
      cout << "Case #" << T << ": ";
      int st = 1;
      while(a[st] == 0)
         st++;
      fru(i, st, cnt)
         cout << a[i];
      cout << "\n";
   }
  
   return 0;
}