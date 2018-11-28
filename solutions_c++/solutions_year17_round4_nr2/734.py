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


int num[1010];

int main(){
  cin.sync_with_stdio(0);
  cin.tie(nullptr);
  
  int T, n, c, m, x, y, z;
  cin >> T;
  rep(kase, 1, T+1){
    memset(num, 0, sizeof(num));
    cin >> n >> c >> m;
    int c[3] = {0, 0, 0};
    rep(i, 0, m){
      cin >> x >> y;
      num[x]++;
      c[y]++;
    }
    int mx = max(c[1], c[2]);
    mx = max(mx, num[1]);
    int move = 0;
    rep(i, 1, n+1){
      move = max(move, num[i] - mx);
    }

    cout << "Case #" << kase << ": " << mx << " "<< move << endl;
  }
  return 0;
}  
