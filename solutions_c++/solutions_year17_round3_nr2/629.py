#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;

struct Interval {
  int x, y, type;
  Interval(){}
  Interval(int x, int y, int type) : x(x), y(y), type(type) {}
  bool operator < (const Interval &b) const {
    if (x != b.x) return x < b.x;
    return y < b.y;
  }
};

bool cmp(const pii &a, const pii &b) {
  if (a.first != b.first) return a.first < b.first;
  return a.second > b.second;
}

int main(void) {

  int cases; scanf("%d", &cases);
  for (int cas = 1; cas <= cases; ++cas) {
    printf("Case #%d: ", cas);
    int N, M; scanf("%d %d", &N, &M);
    vector<Interval> intervals;
    for (int i = 0; i < N; ++i) {
      int x, y; scanf("%d %d", &x, &y);
      intervals.emplace_back(x, y, 0);
    }
    for (int i = 0; i < M; ++i) {
      int x, y; scanf("%d %d", &x, &y);
      intervals.emplace_back(x, y, 1);
    }
    sort(intervals.begin(), intervals.end());
    int n = N + M;
    intervals.emplace_back(intervals[0].x + 1440, intervals[0].y + 1440, intervals[0].type);
    int sumA = 0;
    int sumB = 0;
    int ans = 0;
    vector<pii> avail_A, avail_B;
    for (int i = 0; i < n; ++i) {
      if (intervals[i].type == 0) {
        sumA += intervals[i+1].x - intervals[i].x;
        if (intervals[i+1].type != 0) {
          avail_A.emplace_back(0, intervals[i+1].x - intervals[i].y);
          ++ans;
        } else {
          avail_A.emplace_back(2, intervals[i+1].x - intervals[i].y);
        }
      } else {
        sumB += intervals[i+1].x - intervals[i].x;
        if (intervals[i+1].type == 0) {
          avail_B.emplace_back(0, intervals[i+1].x - intervals[i].y);
          ++ans;
        } else {
          avail_B.emplace_back(2, intervals[i+1].x - intervals[i].y);
        }
      }
    }
    if (sumA > sumB) {
      swap(sumA, sumB);
      swap(avail_A, avail_B);
    }
    int diff = sumB - 720;
    sort(avail_B.begin(), avail_B.end(), cmp);
    for (int i = 0; i < avail_B.size() && diff > 0; ++i) {
      int avail = avail_B[i].second;
      int cost = avail_B[i].first;
      diff -= avail;
      ans += cost;
    }
    printf("%d\n", ans);
  }


  return 0;
}