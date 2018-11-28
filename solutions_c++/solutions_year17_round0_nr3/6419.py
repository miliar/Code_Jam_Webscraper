#include <iostream>
#include <map>
using namespace std;
typedef long long ll;

void test_case(){
   ll N, K;
   cin >> N >> K;
   
   map<ll, ll> count;
   
   count[N] = 1;
   while(K > 0){
      auto it = count.rbegin();
      ll n = it->first;
      ll u = n/2;
      ll d = n-1-u;
      ll c = it->second;
      
      if(c >= K){
         cout << u << ' ' << d << endl;
         return;
      }
      K -= c;
      count[u] += c;
      count[d] += c;
      count.erase(n);
   }
}

int main(){
   int T; cin >> T;
   for(int i=1; i<=T; i++){
      cout << "Case #" << i << ": ";
      test_case();
   }
   return 0;
}
