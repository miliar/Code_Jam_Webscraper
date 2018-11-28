#include <iostream>
#include <sstream>
#include <climits>
#include <stdio.h>
#include <iomanip>
#include <list>
#include <map>
#include <set>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <string>
#include <gmpxx.h>

using namespace std;

int T;
int Aj;
int Ac;
const int minutes = 24 * 60;
int has_baby[minutes];


// Aj == 1; Ac == -1

int has_first() {
  for(int i=0; i<minutes; i++) {
    if(has_baby[i] != 0) return has_baby[i];
  }
  return 0;
}

int has_last() {
  int last = 0;
  for(int i=0; i<minutes; i++) {
    if(has_baby[i] != 0) last = has_baby[i];
  }
  return last;
}

int base_flips() {
  int has_it = has_first();
  int flips = 0;
  for(int i=0; i<minutes; i++) {
    if(has_baby[i] != 0) {
      if(has_baby[i] != has_it) {
        has_it = has_baby[i];
        flips++;
      }
    }
  }
  if(has_it != has_first()) {
    flips += 1;
  }
  return flips;
}

void no_change(int *times) {
  int has_it = has_first();
  times[0] = 0;
  times[1] = 0;
  for(int i=0; i<minutes; i++) {
    if(has_baby[i] != 0) has_it = has_baby[i];
    if(has_it == 1) {
      times[0]++;
    } else {
      times[1]++;
    }
  }
  return;
}

int unused_beginning() {
  int unused = 0;
  for(int i=0; i<minutes; i++) {
    if(has_baby[i] == 0) {
      unused++;
    } else {
      break;
    }
  }
  return unused;
}


int unused_end() {
  int unused = 0;
  for(int i=minutes-1; i>=0; i--) {
    if(has_baby[i] == 0) {
      unused++;
    } else {
      break;
    }
  }
  return unused;
}


int free_time() {
  int count = 0;
  int has_it = has_first();
  int count_since_change = 0;
  int i=0;
  while(has_baby[i] == 0 && i < minutes) {
    i++;
  }
  for(; i < minutes; i++) {
    if(has_baby[i] == 0) {
      count_since_change++;
      continue;
    }
    if(has_baby[i] != has_it) {
      count += count_since_change;
      has_it = has_baby[i];
    }
    count_since_change = 0;
  }
  int unused = 0;
  if(has_first() != has_last()) {
    unused = unused_beginning() + unused_end();
  }
  return count + unused;
}

void find_intervals(int need_more, int *intervals) {
  int interval = 0;
  int count = 0;
  int has_it = has_first();
  int i = 0;
  while(has_baby[i] == 0 && i < minutes) {
    i++;
  }
  for(; i<minutes; i++) {
    if(has_baby[i] == 0) {
      count++;
      continue;
    }
    if(has_baby[i] == has_it && count > 0 && has_it != need_more) {
      intervals[interval] = count;
      interval++;
    }
    has_it = has_baby[i];
    count = 0;
  }
  if(has_first() == has_last() && has_first() != need_more) {
    intervals[interval] = unused_beginning() + unused_end();
  }
}
 
int do_solve() {
  int intervals[100];
  for(int i=0; i<100; i++) {
    intervals[i] = 0;
  }
  for(int i=0; i<minutes; i++) has_baby[i] = 0;
  cin >> Aj >> Ac;
  for(int i=0; i<Aj; i++) {
    int start, end;
    cin >> start >> end;
    for(int j=start; j<end; j++) {
      has_baby[j] = 1;
    }
  }
  for(int i=0; i<Ac; i++) {
    int start, end;
    cin >> start >> end;
    for(int j=start; j<end; j++) {
      has_baby[j] = -1;
    }
  }
  int base = base_flips();
  //cerr << "base flips: " << base << endl;
  int free = free_time();
  int times[2] {0, 0};
  for(int i=0; i<minutes; i++) {
    if(has_baby[i] == 1) {
      times[0]++;
    } else if(has_baby[i] == -1) {
      times[1]++;
    }
  }
  for(int i=0; i<100; i++) {
    intervals[i] = 0;
  }
  find_intervals(-1, intervals);
  int interval_sum = 0;
  for(int i=0; i<100; i++) {
    interval_sum += intervals[i];
  }
  cerr << "interval sum: " << interval_sum << endl;
  int take_max1 = times[0] + free + interval_sum;
  for(int i=0; i<100; i++) {
    intervals[i] = 0;
  }
  find_intervals(1, intervals);
  interval_sum = 0;
  for(int i=0; i<100; i++) {
    interval_sum += intervals[i];
  }
  cerr << "interval sum: " << interval_sum << endl;
  int take_max2 = times[1] + free + interval_sum;
  cerr << "max1: " << take_max1 << " max2: " << take_max2 << " free: " << free << endl;
  if(take_max1 >= 12*60 && take_max2 >= 12*60) {
    return base;
  }
  int need_more;
  int need;
  if(take_max1 < 12*60) {
    need_more = 1;
    need = 12*60 - take_max1;
  } else {
    need_more = -1;
    need = 12*60 - take_max2;
  }
  cerr << "need more: " << need_more << endl;
  find_intervals(need_more, intervals);
  sort(begin(intervals), end(intervals), greater<int>());
  for(int i=0; i<10; i++) {
    cerr << "interval: " << intervals[i] << endl;
  }
  int i = 0;
  int flips = base;
  while(need > 0 && i<100) {
    //cerr << "need " << need << endl;
    need -= intervals[i];
    flips += 2;
    i++;
  }
  if(need > 0) {
    exit(1);
  }
  return flips;
}

void solve(int t) {
  cerr << "test " << t << endl;
  int flips = do_solve();
  cout << "Case #" << t << ": " << flips << endl;
}

int main() {
  cin >> T;
  for(int t=0; t<T; t++) {
    solve(t+1);
  }
}
