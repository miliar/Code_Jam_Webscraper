#include <bits/stdc++.h>
#include <cassert>

using namespace std;

int N, Q;
int E[100], S[100];
int D[100][100];
int U, V;


void query()
{
  assert(V == N-1);

  double memo[101];
  memo[V] = 0;
  for (int i = V-1; i >= 0; i--) {
    memo[i] = 1e100;

    double dist = 0;
    for (int j = i+1; j < N; j++) {
      dist += D[j-1][j];
      if (E[i] < dist) break;
      double t = dist  / S[i];
      memo[i] = min(memo[i], t + memo[j]);
    }
  }

  cout << fixed << setprecision(9) << memo[0];
}

void solve()
{
  cin >> N >> Q;

  for (int i = 0; i < N; i++) {
    cin >> E[i] >> S[i];
  }
  
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      cin >> D[i][j];
    }
  }

  for (int i = 0; i < Q; i++) {
    cin >> U >> V;
    U--; V--;
    cout << ' ';
    query();
  }
}

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ":" << fixed << setprecision(6);
    solve();
    cout << endl;
  }    
  return 0;
}
