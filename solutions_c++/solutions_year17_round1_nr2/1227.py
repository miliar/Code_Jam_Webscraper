#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <string>
#include <map>
#include <iterator>
#include <cassert>

typedef long long ll;

using namespace std;

int N, P;
vector< int > ing[100]; // should have P
vector< int > needed;

map<int, int> inters(map<int, int> A, map<int, int> B) {
  map<int, int> ret;
  map<int, int>::iterator it;
  for (it = A.begin(); it != A.end(); it++) {
    int occ = min(it->second, B[it->first]);
    if (occ != 0) {
      ret[it->first] = occ;
    }
  }
  return ret;
}

int loww(int a, int n) {
   int qq = a * 100;
   int tt = 110 * n;
   if (qq % tt == 0) {
     return qq / tt;
   }
   return qq / tt + 1;
}

int highh(int a, int n) {
  return 100*a / (90 * n);
}

typedef pair<int, int> pi;

#define SRC 0

typedef vector<int> VI;
typedef vector<VI> VVI;

const int INF = 1000000000;

struct MaxFlow {
  int N;
  VVI cap, flow;
  VI dad, Q;

  MaxFlow(int N) :
    N(N), cap(N, VI(N)), flow(N, VI(N)), dad(N), Q(N) {}

  void AddEdge(int from, int to, int cap) {
    //cout << from << " " << to << endl;
    this->cap[from][to] += cap;
  }

  int BlockingFlow(int s, int t) {
    fill(dad.begin(), dad.end(), -1);
    dad[s] = -2;

    int head = 0, tail = 0;
    Q[tail++] = s;
    while (head < tail) {
      int x = Q[head++];
      for (int i = 0; i < N; i++) {
        if (dad[i] == -1 && cap[x][i] - flow[x][i] > 0) {
          dad[i] = x;
          Q[tail++] = i;
        }
      }
    }

    if (dad[t] == -1) return 0;

    int totflow = 0;
    for (int i = 0; i < N; i++) {
      if (dad[i] == -1) continue;
      int amt = cap[i][t] - flow[i][t];
      for (int j = i; amt && j != s; j = dad[j])
        amt = min(amt, cap[dad[j]][j] - flow[dad[j]][j]);
      if (amt == 0) continue;
      flow[i][t] += amt;
      flow[t][i] -= amt;
      for (int j = i; j != s; j = dad[j]) {
        flow[dad[j]][j] += amt;
        flow[j][dad[j]] -= amt;
      }
      totflow += amt;
    }

    return totflow;
  }

  int GetMaxFlow(int source, int sink) {
    //cout << "flow " << source << " " << sink << endl;
    int totflow = 0;
    while (int flow = BlockingFlow(source, sink))
      totflow += flow;
    return totflow;
  }
};

bool inters(pi a, pi b) {
  int maxS = max(a.first, b.first);
  int minE = min(a.second, b.second);
  return maxS <= minE;
}

int main() {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  ios::sync_with_stdio(false);
  cin.tie(0);

  int T, x;
  cin >> T;
  for (int tt = 1; tt <= T; tt++) {
    cin >> N >> P;
    int SNK = N * P + 3;
    MaxFlow mf(SNK + 1);
    for (int i = 0; i < N; i++) {
      ing[i].clear();
    }
    needed.clear();
    for (int i = 0; i < N; i++) {
      cin >> x;
      needed.push_back(x);
    }
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < P; j++) {
        cin >> x;
        ing[i].push_back(x);
      }
    }

    vector< pi > prev;

    for (int i = 0; i < N; i++) {
      vector< pi > vv;
      for (int j = 0; j < P; j++) {
        int low = loww(ing[i][j], needed[i]);
        int high = highh(ing[i][j], needed[i]);

        if (low <= high) {
          vv.push_back(pi(low, high));
        }
      }

      if (i == 0) {
        for (int i = 0; i < P; i++) {
          mf.AddEdge(SRC, i + 1, 1);
        }
      } else {
        for (int j = 0; j < prev.size(); j++) {
          for (int k = 0; k < vv.size(); k++) {
            if (inters(prev[j], vv[k])) {
              mf.AddEdge((i-1) * P + 1 + j, i*P + 1 + k, 1);
            }
          }
        }
      }
      prev = vv;

    }

    for (int i = 0; i < P; i++) {
      mf.AddEdge((N-1) * P + i + 1, SNK, 1);
    }
    if (N == 1) {
      cout << "Case #" << tt << ": " << prev.size() << endl;
    } else {
      cout << "Case #" << tt << ": " << mf.GetMaxFlow(SRC, SNK) << endl;
    }
  }

  return 0;
}
