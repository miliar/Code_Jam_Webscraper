#include<bits/stdc++.h>
#define ll long long
using namespace std;
int f(string x){
  for(int i = x.size()-1; i >= 0 ; --i){
    if(x[i]=='-')
    return i;
  }
  return -1;
}
int solve(string x , int k){
   int val = f(x);
    if(val == -1)
    return 0;
    else {
        int dist = val + 1;
        if(dist < k ) return -1e9;
      for(int i = dist - k ; i < dist ; ++i ){
        if(x[i]=='-')
        x[i] = '+';
        else
        x[i] = '-';
      }
    return 1 + solve(x , k);
    }
}
int main(){
       cin.sync_with_stdio(false);
      ifstream cin("a.txt");
       ofstream cout("b.txt");
       int T;
       cin >> T;
       for(int t = 1 ; t <= T ; ++t ){
        string x;
        int k;
         cin >> x >> k;
         cout << "Case #" << t <<": ";
         int res = solve(x , k);
         if(res < 0 )
         cout << "IMPOSSIBLE" << endl; else
         cout << res << endl;
       }
  return 0;
}
