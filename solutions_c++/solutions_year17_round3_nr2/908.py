#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <map>
#include <set>
#include <tuple>
#include <string.h>

typedef long long ll;
using namespace std;

int solve(int A1, int A2, int *S1, int *E1, int *S2, int *E2) {
  tuple<int, int, int> s[300];
  for (int i = 0; i < A1; i++) {
    s[i] = make_tuple(S1[i], E1[i], 1);
  }
  for (int i = 0; i < A2; i++) {
    s[A1+i] = make_tuple(S2[i], E2[i], 2);
  }
  sort(s, s+A1+A2);
  pair<int, int> d[300];
  for (int i = 1; i < A1+A2; i++) {
    int c;
    if (get<2>(s[i]) != get<2>(s[i-1])) {
      c = -1;
    } else {
      c = get<2>(s[i]);
    }
    d[i] = make_pair(get<0>(s[i]) - get<1>(s[i-1]), c);
  }
  int c;
  if (get<2>(s[0]) != get<2>(s[A1+A2-1])) {
    c = -1;
  } else {
    c = get<2>(s[0]);
  }
  d[0] = make_pair(1440 + get<0>(s[0]) - get<1>(s[A1+A2-1]), c);
  double e1 = 720;
  double e2 = 720;
  for (int i = 0; i < A1+A2; i++) {
    if (get<2>(s[i]) == 1)
      e2 -= get<1>(s[i]) - get<0>(s[i]);
    else
      e1 -= get<1>(s[i]) - get<0>(s[i]);
  }
  int ans = 0;
  for (int i = 0; i < A1+A2; i++) {
    //printf("%d %d\n", d[i].first, d[i].second);
    if (d[i].second == -1) {
      if (e1 >= e2) {
        double x = min((double)d[i].first, e1-e2);
        double y = (d[i].first - x) / 2.0;
        e1 -= x + y;
        e2 -= y;
      } else {
        double x = min((double)d[i].first, e2-e1);
        double y = (d[i].first - x) / 2.0;
        e1 -= y;
        e2 -= x + y;
      }
      ans++;
    }
  }
  if (e1 == 0 && e2 == 0)
    return ans;
  int d1[300];
  int d2[300];
  int n1 = 0, n2 = 0;
  for (int i = 0; i < A1+A2; i++) {
    if (d[i].second == 1) {
      e2 -= d[i].first;
      d2[n2++] = d[i].first;
    } else if (d[i].second == 2) {
      e1 -= d[i].first;
      d1[n1++] = d[i].first;
    }
  }
  sort(d1, d1+n1, greater<int>());
  sort(d2, d2+n2, greater<int>());
  if (e1 == 0 && e2 == 0)
    return ans;
  if (e1 != -e2)
    fprintf(stderr, "??????\n");
  if (e1 <= 0) {
    for (int i = 0; i < n1; i++) {
      ans += 2;
      e1 += d1[i];
      if (e1 >= 0)
        return ans;
    }
  } else {
    for (int i = 0; i < n2; i++) {
      ans += 2;
      e2 += d2[i];
      if (e2 >= 0)
        return ans;
    }
  }
  fprintf(stderr, "2??????\n");
  return ans;
}

int main()
{
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    int A1, A2;
    int S1[110];
    int E1[110];
    int S2[110];
    int E2[110];
    cin >> A1 >> A2;
    for (int j = 0; j < A1; j++) {
      cin >> S1[j] >> E1[j];
    }
    for (int j = 0; j < A2; j++) {
      cin >> S2[j] >> E2[j];
    }
    int ans = solve(A1, A2, S1, E1, S2, E2);
    printf("Case #%d: %d\n", i+1, ans);
  }
}
