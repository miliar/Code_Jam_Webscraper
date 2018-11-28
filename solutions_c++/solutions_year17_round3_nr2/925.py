#include <iostream>
#include <cmath>
#include <set>
using namespace std;

struct schedule {
  int startTime, endTime;
};

bool cmp(schedule x, schedule y) {
  return x.startTime < y.startTime;
}

int main() {
  int T, C, J;
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    scanf("%d%d", &C, &J);
    schedule *scheduleC = new schedule[C];
    schedule *scheduleJ = new schedule[J];
    for (int j = 0; j < C; j++) {
      scanf("%d%d", &scheduleC[j].startTime, &scheduleC[j].endTime);
    }
    for (int j = 0; j < J; j++) {
      scanf("%d%d", &scheduleJ[j].startTime, &scheduleJ[j].endTime);
    }
    sort(scheduleC, scheduleC + C, cmp);
    sort(scheduleJ, scheduleJ + J, cmp);
    if (C == 1 || J == 1) {
      printf("Case #%d: %d\n", i + 1, 2);
    } else {
      if (C == 2) {
        if (((scheduleC[1].endTime - scheduleC[0].startTime) <= 720) 
            || ((1440 - scheduleC[1].startTime + scheduleC[0].endTime) <= 720)) {
          printf("Case #%d: %d\n", i + 1, 2);
        } else {
          printf("Case #%d: %d\n", i + 1, 4);
        }
      } else {
        if (((scheduleJ[1].endTime - scheduleJ[0].startTime) <= 720)
            || ((1440 - scheduleJ[1].startTime + scheduleJ[0].endTime) <= 720)) {
          printf("Case #%d: %d\n", i + 1, 2);
        } else {
          printf("Case #%d: %d\n", i + 1, 4);
        }
      }
    }
  }
}