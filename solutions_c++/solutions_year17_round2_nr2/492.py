#include <bits/stdc++.h>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

bool FindMatch(int i, const VVI &w, VI &mr, VI &mc, VI &seen) {
  for (int j = 0; j < w[i].size(); j++) {
    if (w[i][j] && !seen[j]) {
      seen[j] = true;
      if (mc[j] < 0 || FindMatch(mc[j], w, mr, mc, seen)) {
        mr[i] = j;
        mc[j] = i;
        return true;
      }
    }
  }
  return false;
}

int BipartiteMatching(const VVI &w, VI &mr, VI &mc) {
  mr = VI(w.size(), -1);
  mc = VI(w[0].size(), -1);
  
  int ct = 0;
  for (int i = 0; i < w.size(); i++) {
    VI seen(w[0].size());
    if (FindMatch(i, w, mr, mc, seen)) ct++;
  }
  return ct;
}

int N, A[10];
int vertices[1234];

int main() {
  ios::sync_with_stdio(0);
  int T;
  cin >> T;
  int case_num = 0;
  while (T--) {
    case_num++;
    cin >> N;
    for (int i = 0; i < 6; i++) cin >> A[i];
    int idx = 0;
    /*
    for (int i = 0; i < 6; i++) {
      while (A[i] > 0) {
        vertices[idx] = i;
        idx++;
        A[i]--;
        //cout << idx << ": " << i << endl;
      }
    }
    */

    map<int, char> colors;
    colors[0] = 'R';
    colors[1] = 'O';
    colors[2] = 'Y';
    colors[3] = 'G';
    colors[4] = 'B';
    colors[5] = 'V';


    // Small--------------
    vector<int> v;
    for (int i = 0; i < 6; i += 2) {
      if (A[i] > 0) {
        v.push_back(i);
        A[i]--;
        break;
      }
    }

    for (int i = 1; i < N; i++) {
      // Find max cur color
      int current_color = -1;
      int most_seen = 0;
      for (int j = 0; j < 6; j += 2) {
        if (v.back() != j && A[j] > most_seen) {
          most_seen = A[j];
          current_color = j;
        }
      }
      if (current_color == -1) {
        break;
      }
      v.push_back(current_color);
      A[current_color]--;
    }

    if (v.size() != N) {
      printf("Case #%d: IMPOSSIBLE\n", case_num);
      continue;
    }
    if (v[0] == v.back()) {
      printf("Case #%d: IMPOSSIBLE\n", case_num);
      continue;
    }
    string s;
    for (int i = 0; i < N; i++) {
      s += colors[v[i]];
    }

    printf("Case #%d: %s\n", case_num, s.c_str());

    /*
    continue;

    VVI adj(N, VI(N));
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        int diff = (12 + vertices[i] - vertices[j]) % 6;
        if (diff != 1 && diff != 0 && diff != 5) adj[i][j] = 1;
      }
    }

    VI mr(N), mc(N);
    int card = BipartiteMatching(adj, mr, mc);
    if (card != N) {
      printf("Case #%d: IMPOSSIBLE\n", case_num);
      continue;
    }
    */


    
    /*
    int node = 0;
    string ans;
    for (int i = 0; i < N; i++) {
      cout << i << ": " << node << endl;
      ans += colors[vertices[node]];
      node = mr[node];
    }
    printf("Case #%d: %s\n", case_num, ans.c_str());

    */
  }
  return 0;
}
