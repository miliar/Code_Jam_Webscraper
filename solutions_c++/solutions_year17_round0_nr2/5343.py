#include <bits/stdc++.h>

using namespace std;

#define dbg(x) (cout<<#x<<" = "<<(x)<<'\n')
typedef long long int lld;

bool is_tidy(lld x) {
  int c = 10;
  while (x) {
    if (x % 10 > c) {
      return false;
    }
    c = x % 10;
    x /= 10;
  }
  return true;
}

lld to_lld(char* T) {
  if (*T == 0) {
    return 0;
  }
  return to_lld(T + 1) * 10LL + (T[0] - '0');
}

lld solve(lld N) {
  char S[30];
  sprintf(S, "%lld", N);
  int L = strlen(S);
  lld sol = -1;

  for (int i = 0; i <= L; ++i) {
    char T[30];
    sprintf(T, "%s", S);

    if (T[i] == '0') {
      continue;
    }

    T[i]--;

    for (int j = i + 1; j < L; ++j) {
      T[j] = '9';
    }

    T[L] = 0;
    reverse(T, T + L);
    lld number = to_lld(T);
    if (is_tidy(number)) {
      sol = max(sol, number);
    }
  }

  return sol;
}

int main() {
  cin.sync_with_stdio(false);

  int num_cases;
  cin >> num_cases;

  lld N;
  for (int case_index = 1; case_index <= num_cases; ++case_index) {
    cin >> N;
    lld sol = solve(N);

    cout << "Case #" << case_index << ": ";
    cout << sol;
    cout << '\n';
  }


  return 0;
}
