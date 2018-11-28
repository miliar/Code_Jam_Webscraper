#include<bits/stdc++.h>
using namespace std;

#define X first
#define Y second

#define debug(a) cerr << #a << " = " << (a) << endl;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

template<typename T> ostream& operator<<(ostream& o, vector<T>& v) {
  for (auto& a: v) o << a << ' ';
  return o;
}

string str;
string ans;
int n;
int memo[20][10][2];
int dp(int id, int p, int eq){
  int &res = memo[id][p][eq];
  if (res != -1) return res;
  if (id == n) return res = 1;
  res = 0;
  if (!eq) {
    for (int nx = 9; nx >= p; nx--){
      if (dp(id + 1, nx, 0)){
	ans[id] = char(nx + '0');
	return res = 1;
      }
    }
  } else {
    for (int nx = int(str[id] - '0'); nx >= p; nx--){
      if (dp(id + 1, nx, int(str[id] - '0') == nx)){
	ans[id] = char(nx + '0');
	return res = 1;
      }
    }    
  }
  return res;
}

void solve(){
  cin >> str;
  n = (int)str.size();
  ans = string(n, '#');
  memset(memo, -1, sizeof memo);
  dp(0, 0, 1);
  while ((int)ans.size() && ans.front() == '0') ans = ans.substr(1);
  if (ans.empty()) cout << 0 << endl;
  else cout << ans << endl;
}

int main() {
  ios::sync_with_stdio(0);  cin.tie(0);
  int tc; cin >> tc;
  for (int cs = 1; cs <= tc; cs++){
    cout << "Case #" << cs << ": ";
    solve();
  }
}
