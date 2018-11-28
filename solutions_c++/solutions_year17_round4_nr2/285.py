#include <stdio.h>

#include <algorithm>
#include <cmath>
#include <cassert>

struct Data {
  int P, B;
} data[1001];

bool cmp(Data x, Data y) { return x.P < y.P; }

int seat_cnt[1001], person_cnt[1001], arrange[1001], full_id;

int numRide(int N, int C) {
  int numSeat = 0, numPerson = 0;
  for (int i = 1, sum = 0; i <= N; ++i) {
    sum += seat_cnt[i];
    numSeat = std::max(numSeat, (sum + i - 1) / i);
  }
  for (int i = 1; i <= C; ++i)
    numPerson = std::max(numPerson, person_cnt[i]);
  return std::max(numSeat, numPerson);
}

int findAvailable(int N, int r) {
  while (arrange[full_id] == r) ++full_id;
  return full_id;
}

int main() {
  int T, N, C, M;
  int r, promote;
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    scanf("%d%d%d", &N, &C, &M);
    for (int i = 1; i <= N; ++i)
      seat_cnt[i] = 0;
    for (int i = 1; i <= C; ++i)
      person_cnt[i] = 0;
    for (int i = 0; i < M; ++i) {
      scanf("%d%d", &data[i].P, &data[i].B);
      seat_cnt[data[i].P] += 1;
      person_cnt[data[i].B] += 1;
    }
    r = numRide(N, C);
    promote = 0;
    full_id = 0;

    std::sort(data, data + M, cmp);
    for (int i = 1; i <= N; ++i)
      arrange[i] = 0;

    for (int i = 0; i < M; ++i) {
      int p = data[i].P;
      if (arrange[p] < r) {
        arrange[p] += 1;
      } else {
        int p2 = findAvailable(N, r);
        assert(p2 < p);
        arrange[p2] += 1;
        promote += 1;
      }
    }

    printf("Case #%d: %d %d\n", t, r, promote);
  }
}
