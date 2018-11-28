#include <cstdio>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <cstring>
#include <string>
#include <set>
#include <stack>
#define pb push_back

#define mp make_pair
#define f first
#define s second
#define ll long long

using namespace std;

void debug(vector<int>& V) {
    for (int i = 0; i < V.size(); ++i) {
        cerr << V[i];
    }
    cerr << "\n";
}
void solve(int N, int K) {
    vector <int> V(N + 2, 0);

    V[0] = V[N + 1] = 1;
    debug(V);
    for (int k = 0; k < K; ++k) {
        vector<int> L(N + 2, 0);
        vector<int> R(N + 2, 0);

        for (int i = 1; i <= N; ++i) {
            for (int j = i - 1; j >= 0; --j) {
                if (V[j] == 1) {
                    L[i] = i - j - 1;
                    break;
                }
            }
            for (int j = i + 1; j <= N + 1; ++j) {
                if (V[j] == 1) {
                    R[i] = j - i - 1;
                    break;
                }
            }
        }

        int pos = 1;
        int cur_max = -1;

        for (int i = 1; i <= N; ++i) {
            if (V[i] == 1) {
                continue;
            }
            int lr_min = min(L[i], R[i]);
            int lr_max = max(L[i], R[i]);
            if (lr_min > cur_max) {
                cur_max = lr_min;
                pos = i;
            } else if (lr_min == cur_max) {
                if (lr_max > max(L[pos], R[pos])) {
                    pos = i;
                }
            }
        }
        V[pos] = 1;
        cerr << N << " " << k + 1 << " -> (" << min(L[pos], R[pos]) << ", " << max(L[pos], R[pos]) << ")\n";
//        debug(V);
    }
}
pair<int,int> cute_solve(int N, int K) {
    priority_queue<int> pq;
    vector<pair<int, int> > Ans(K + 1, pair<int,int>(0, 0));
    pq.push(N);
    for (int i = 1; i <= K; ++i) {
        auto n = pq.top(); pq.pop();
        int left = (n-1)/2;
        int right = n - 1 - left;
        if (left > 0) pq.push(left);
        if (right > 0) pq.push(right);
        Ans[i] = make_pair(max(left, right), min(left, right));
    }
    return Ans[K];
    /*
    for (int i = 1; i <= K; ++i) {
        cerr << "("<<Ans[i].first<< ", "<< Ans[i].second << ")\n";
    }*/
}
int main() {
  ifstream cin("test.in");
  ofstream cout("test.out");

  int T; cin >> T;
  for (int tc = 1; tc <= T; ++tc) {
      int N, K; cin >> N >> K;
      //cerr << "test case " << tc << "\n";
      //solve(N, K);
      auto ans = cute_solve(N, K);
      cout << "Case #" << tc << ": " << ans.first << " " << ans.second << "\n";
  }
  return 0;
}
