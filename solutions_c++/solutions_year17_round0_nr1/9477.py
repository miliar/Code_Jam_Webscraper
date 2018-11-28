#include <algorithm>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define EPS 1e-10
#define INF 1000000
#define mp make_pair
#define pb push_back

typedef vector<int> vi;
typedef vector<vi> vii;
typedef pair<int,int> pii;
typedef long long ll;

string flip( string S, int K, int pos ) {
  for (int i = 0; i < K; i++) {
    int npos = pos + i;
    S[npos] = (S[npos] == '+') ? '-' : '+';
  }
  return S;
}

bool is_all_smile( string S ) {
  for (int i = 0; i < S.size(); i++) {
    if (S[i] == '-') {
      return false;
    }
  }
  return true;
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    string S;
    int K;
    cin >> S;
    cin >> K;

    int cnt = 0;
    for (int i = 0; i < S.size(); i++) {
      if (S[i] == '+') {
        continue;
      }

      if (i + K > S.size()) {
        break;
      }

      S = flip(S, K, i);

      cnt++;
    }

    if (is_all_smile(S)) {
      cout << "Case #" << t << ": " << cnt << endl;
    } else {
      cout << "Case #" << t << ": IMPOSSIBLE" << endl;
    }
  }
}

