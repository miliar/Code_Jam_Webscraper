#include <iostream>
#include <iomanip>  
#include <stdio.h>
#include <map>
#include <unordered_map>
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

int t;

int main() {
   //ios_base::sync_with_stdio(0);
   //cout.tie(0); cin.tie(0);
   
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);

   cin >> t;
   fru(T, 1, t)
   {
      ll n, k;
      cin >> n >> k;
      
      priority_queue<ll> q;
      map<ll, ll> mp;
      
      q.push(n);
      mp[n] = 1;
      
      while(k > 0)
      {
         ll val = q.top();
         q.pop();
         ll cnt = mp[val];
         
         ll l = val / 2;
         ll r = val - l - 1;
         
         if(r > l)
            swap(l, r);
         
         if(cnt >= k)
         {
            cout << "Case #" << T << ": " << l << " " << r << "\n"; 
            break;
         }
         k -= cnt;
         
         if(mp.count(l) == 0 && l >= 0)
            q.push(l);
         mp[l] += cnt;
         
         if(mp.count(r) == 0 && r >= 0)
            q.push(r);
         mp[r] += cnt;
      }
   }
   
   return 0;
}