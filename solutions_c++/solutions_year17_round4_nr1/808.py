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


int num[200];

int main(){
  cin.sync_with_stdio(0);
  cin.tie(nullptr);
  
  int T, m, n, x;
  cin >> T;
  rep(kase, 1, T+1){
    cin >> m >> n;
    memset(num, 0, sizeof(num));
    rep(i, 0, m){
      cin >> x;
      num[x%n]++;
    }
    cout << "Case #" << kase << ": ";
    if (n == 2){
      cout << (num[0] + num[1]/2 + num[1]%2) << endl;
    }else if (n==3){
      int res = min(num[1], num[2]);
      num[1] -= res;
      num[2] -= res;
      if (num[1] > 0){
        res += num[1]/3 + (num[1]%3 ? 1 :0 );
      }else{
        res += num[2]/3 + (num[2]%3 ? 1 :0 );
      }
      res += num[0];
        
      cout << res << endl; 
    }else{
      int res = num[0] + num[2]/2 + min(num[1], num[3]);
      num[2] = num[2] % 2;
      num[1] = max(num[1], num[3]) - min(num[1], num[3]);
      if (num[2] && num[1] >= 2){
        num[2]--;
        num[1] -= 2;
        res ++;
      }
      res += num[1]/4;
      num[1] = num[1]%4;
      if (num[2] || num[1]){
        res ++;
      }
      cout << res << endl;
    }
  }
  return 0;
}  
