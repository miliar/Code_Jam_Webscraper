#include <iostream>
#include <vector>
#include <set>
#include <unordered_set>
#include <map>
#include <string>
#include <unordered_map>
#include <utility>
#include <algorithm>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
using namespace std;

typedef pair<int, int> pii;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef long long ll;

#define fi first
#define se second
#define pb push_back
#define rep(i, a, b) for(int (i)=(a); (i)<(b); (i)++)

const int INF = 0x3f3f3f3f;

int main(){
  cin.sync_with_stdio(0);
  cin.tie(nullptr);
  
  int n;
  cin >> n;
  rep(kase, 1, n+1){
    ll a, b, num;
    cin >> a >> num;
    map<ll, ll> M;
    M[a] = 1;
    for (;;){
      auto itr = M.end();
      itr--;
      ll cur = (itr->fi - 1);
      ll mx = (cur/2)+(cur%2);
      ll mn = cur/2;
      if (itr->se >= num){
        cout << "Case #" << kase << ": " << mx << " " << mn << endl;
        break;
      }
      num -= itr->se;
      M[mx] += itr->se;
      M[mn] += itr->se;
      M.erase(itr);
    }
  }
  return 0;
  
}  
