#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
template<typename T> using Graph = vector<vector<T>>;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())
#define HAS(a, x) (a.find(x) != a.end())
#define endl '\n'

int T, N, C, M;
int P[1005], B[1005];
int BP[2][1005];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> T;

  rep(loop, T) {
      cin >> N >> C >> M;
      rep(i, N) BP[0][i] = BP[1][i] = 0;
      rep(i, M) {
        cin >> P[i] >> B[i];
        P[i]--; B[i]--;
        BP[B[i]][P[i]]++;
      }

      int rides = 0, promotes = 0;
      rep(i, N) {
        int tmp = BP[0][i];
        rep(j, tmp) {
            bool match = false;
            rep(k, N) {
                if (k != i && BP[0][k] > 0 && BP[1][k] > 0) {
                    rides++;
                    BP[0][i]--;
                    BP[1][k]--;
                    match = true;
                    break;
                }
            }
            if (match) continue;
            rep(k, N) {
                if (k != i && BP[1][k] > 0) {
                    rides++;
                    BP[0][i]--;
                    BP[1][k]--;
                    match = true;
                    break;
                }
            }
        } 
      }

      rep(i, N) {
        rep(j, BP[0][i]) {
            rides++;
            if (i != 0 && BP[1][i] > 0) {
                promotes++;
                BP[1][i]--;
            }
        } 
      }

      rep(i, N) rides += BP[1][i];

      printf("Case #%d: %d %d\n", loop + 1, rides, promotes);
  }

  return 0;
}
