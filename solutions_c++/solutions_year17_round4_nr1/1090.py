#include <bits/stdc++.h>

using namespace std;

#define dbg(x) (cout<<#x<<" = "<<(x)<<'\n')

typedef long long int lld;
const int NMAX = 100;
const int PMAX = 100;
const int VMAX = 100;

int N, P;
int V[4];

void read() {
  cin >> N >> P;

  for (int i = 1, x; i <= N; ++i) {
    cin >> x;
    V[x % P]++;
  }
}

int solve() {
  int sol = V[0];

  if (P == 2) {
    sol += (V[1] + 1) / 2;

  } else if (P == 3) {
    int p = min(V[1], V[2]);
    sol += p;
    V[1] -= p, V[2] -= p;

    sol += (V[1] + V[2] + 2) / 3;

  } else if (P == 4) {
    int p = min(V[1], V[3]);
    sol += p;
    V[1] -= p, V[3] -= p;

    sol += V[2] / 2;
    V[2] %= 2;

    if (!V[2]) {
      sol += (V[1] + V[3] + 3) / 4;
    } else {
      int r = V[1] + V[3];
      if (r <= 2) {
        sol += 1;
      } else {
        r -= 2;
        sol += 1;
        sol += (r + 3) / 4;
      }
    }
  }

  return sol;
}

void clean() {
  memset(V, 0, sizeof(V));
}

int main() {
  cin.sync_with_stdio(false);

  int num_cases;
  cin >> num_cases;

  for (int case_index = 1; case_index <= num_cases; ++case_index) {
    clean();

    read();

    cout << "Case #" << case_index << ": ";

    int sol = solve();
    cout << sol;

    cout << '\n';
  }


  return 0;
}
