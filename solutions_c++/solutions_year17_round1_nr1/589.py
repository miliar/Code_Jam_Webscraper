#include <bits/stdc++.h>
#define FOR(x,n) for(int x = 0; x < n; x++)
#define ALL(a) (a).begin(), (a).end()
#define SZ(a) ((int)(a).size())
#define FIN ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
using namespace std;
typedef long long ll;

const int MXN = 25, MXV = 26;
char A[MXN][MXN], ANS[MXN][MXN];

int main() { FIN;
  int T; cin >> T;
  for(int cases = 1; cases <= T; cases++){
    int N, M; cin >> N >> M;
    memset(ANS,0,sizeof(ANS));
    FOR(x,N) FOR(y,M)
      cin >> A[x][y];
    int firstX = N;
    FOR(x,N) FOR(y,M) {
      if(A[x][y] != '?'){
        firstX = min(x,firstX);
        int I = y, J = y;
        for(int i = y; i >= 0; i--)
          if((A[x][i] != '?' && i != y) || ANS[x][i])
            break;
          else
            I = i;
        for(int j = y; j < M; j++)
          if((A[x][j] != '?' && j != y) || ANS[x][j])
            break;
          else
            J = j;
        for(int a = I; a <= J; a++)
          ANS[x][a] = A[x][y];
      }
    }

    int lastX = firstX;
    FOR(x,N) {
      if(ANS[x][0])
        lastX = x;
      else {
        for(int y = 0; y < M; y++)
          ANS[x][y] = ANS[lastX][y];
      }
    }

    cout << "Case #" << cases << ":\n";
    FOR(x,N) {
      FOR(y,M) cout << ANS[x][y];
      cout << "\n";
    }
  }
}
