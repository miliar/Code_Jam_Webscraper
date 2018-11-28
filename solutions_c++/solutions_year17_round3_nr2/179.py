#include <cstdio>
#include <cstring>
#include <limits>
#include <vector>
using namespace std;

int const kDay = 24 * 60;
int const kInfinity = numeric_limits<int>::max() / 2;

struct Activity {
  int m_start = 0;
  int m_end = 0;
};

enum Person { PERSON_CAMERON = 0, PERSON_JAMIE = 1, PERSON_COUNT = 2 };

int g_dp[kDay + 1 /* time passed */][kDay + 1 /* Cameron time */]
        [PERSON_COUNT /* who last */];

int Solve(Person first, vector<Activity> const &ca,
          vector<Activity> const &ja) {
  int const kFree = -1;

  vector<int> day(kDay + 1, kFree);
  for (auto const &a : ca) {
    for (int t = a.m_start; t != a.m_end; ++t)
      day[t] = PERSON_CAMERON;
  }
  for (auto const &a : ja) {
    for (int t = a.m_start; t != a.m_end; ++t)
      day[t] = PERSON_JAMIE;
  }

  if (day[0] == first)
    return kInfinity;

  for (int timePassed = 0; timePassed <= kDay; ++timePassed) {
    for (int cameronTime = 0; cameronTime <= kDay; ++cameronTime) {
      g_dp[timePassed][cameronTime][PERSON_CAMERON] = kInfinity;
      g_dp[timePassed][cameronTime][PERSON_JAMIE] = kInfinity;
    }
  }

  g_dp[1][first == PERSON_CAMERON ? 1 : 0][first] = 0;
  for (int timePassed = 2; timePassed <= kDay; ++timePassed) {
    int const time = timePassed - 1;

    for (int cameronTime = 0; cameronTime <= timePassed; ++cameronTime) {
      int const jamieTime = timePassed - cameronTime;

      if (day[time] != PERSON_CAMERON && cameronTime != 0) {
        int const a = g_dp[timePassed - 1][cameronTime - 1][PERSON_CAMERON];
        int const b = g_dp[timePassed - 1][cameronTime - 1][PERSON_JAMIE] + 1;

        int const c = min(a, b);
        g_dp[timePassed][cameronTime][PERSON_CAMERON] = min(c, kInfinity);
      }
      if (day[time] != PERSON_JAMIE && jamieTime != 0) {
        int const a = g_dp[timePassed - 1][cameronTime][PERSON_JAMIE];
        int const b = g_dp[timePassed - 1][cameronTime][PERSON_CAMERON] + 1;

        int const c = min(a, b);
        g_dp[timePassed][cameronTime][PERSON_JAMIE] = min(c, kInfinity);
      }
    }
  }

  int const a =
      g_dp[kDay][kDay / 2][PERSON_CAMERON] + (first != PERSON_CAMERON);
  int const b = g_dp[kDay][kDay / 2][PERSON_JAMIE] + (first != PERSON_JAMIE);
  return min(a, b);
}

int Solve(vector<Activity> const &ca, vector<Activity> const &ja) {
  return min(Solve(PERSON_CAMERON, ca, ja), Solve(PERSON_JAMIE, ca, ja));
}

int main() {
  int numTests;
  scanf("%d", &numTests);
  for (int testNum = 1; testNum <= numTests; ++testNum) {
    int ac, aj;
    scanf("%d%d", &ac, &aj);

    vector<Activity> ca(ac);
    for (int i = 0; i < ac; ++i)
      scanf("%d%d", &ca[i].m_start, &ca[i].m_end);

    vector<Activity> ja(aj);
    for (int i = 0; i < aj; ++i)
      scanf("%d%d", &ja[i].m_start, &ja[i].m_end);

    printf("Case #%d: %d\n", testNum, Solve(ca, ja));
  }
  return 0;
}
