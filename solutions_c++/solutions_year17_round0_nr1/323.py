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

void solve(){
  string str;
  int k;
  cin >> str >> k;
  int n = (int)str.size();
  int res = 0;
  for (int i = 0; i + k <= n; i++){
    if (str[i] == '-') {
      res++;
      for (int j = 0; j < k; j++){
	char &c = str[i+j];
	if (c == '+') c = '-';
	else c = '+';
      }
    }
  }
  for (char c : str) {
    if (c == '-') {
      cout << "IMPOSSIBLE" << endl;
      return;
    }
  }
  cout << res << endl;
}

int main() {
  ios::sync_with_stdio(0);  cin.tie(0);
  int tc; cin >> tc;
  for (int cs = 1; cs <= tc; cs++){
    cout << "Case #" << cs << ": ";
    solve();
  }
}
