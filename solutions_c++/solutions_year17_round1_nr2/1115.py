#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

struct event{
  int x;
  int type; // 0 = min, 1 = max
  int id;
  // Extra info about the segment
  int l;
  int r;
};

bool operator<(const event &a, const event &b) {
  return a.x < b.x || (a.x == b.x && (a.type < b.type || (a.type == b.type && a.id < b.id)));
}

int solve(int n, int p, vector <int>& r, vector <vector <int> > & q) {
  vector <event> events;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < p; ++j) {
      // Calculate minimum and maximum
      int minval = ceil(((double)q[i][j]) / (1.1 * (double)r[i]));
      int maxval = floor(((double)q[i][j]) / (0.9 * (double)r[i]));
      // Check if there is a segment
      if (minval > 0 && minval <= maxval) {
        event minev;
        minev.type = 0;
        minev.id = i;
        minev.x = minval;
        minev.l = minval;
        minev.r = maxval;
        events.push_back(minev);
        event maxev;
        maxev.type = 1;
        maxev.id = i;
        maxev.x = maxval;
        maxev.l = minval;
        maxev.r = maxval;
        events.push_back(maxev);
      }
    }
  }
  sort(events.begin(), events.end());
  // cout << "Events:" << endl;
  // for (int i = 0; i < events.size(); ++i) {
  //   cout << events[i].x << endl;
  // }
  int ans = 0;
  vector <int> num(n, 0);
  vector < vector <int> > ignore(n, vector <int> (0));
  for (int i = 0; i < events.size(); ++i) {
    event cur = events[i];
    if (cur.type == 0) {
      num[cur.id]++;
    } else {
      // Need to ignore this closing
      bool skip = false;
      // decide whether to ignore
      for (int j = 0; j < ignore[cur.id].size(); ++j) {
        int val = ignore[cur.id][j];
        if (val != -1 && cur.l <= val) {
          ignore[cur.id][j] = -1;
          skip = true;
          break;
        }
      }

      if (!skip) {
        // Recheck whether the entirety of num is positive
        bool good = true;
        for (int j = 0; j < n; ++j) {
          if (num[j] < 1) {
            good = false;
            break;
          }
        }
        // We have a set!
        if (good) {
          ans++;
          //cout << "*" << cur.x << endl;
          // Decrement by 1 and ignore all the other closings
          for (int j = 0; j < n; ++j) {
            num[j]--;
            if (j != cur.id) { // The current one is accounted for
              ignore[j].push_back(cur.x);
            }
          }
        } else {
          num[cur.id]--;
        }
      }
    }
  }
  return ans;
}

void tcase(int t) {
  int n, p;
  cin >> n >> p;
  vector <int> r(n);
  for (int i = 0; i < n; ++i) {
    cin >> r[i];
  }
  vector <vector <int> > q;
  vector <int> qtemp;
  int temp;
  for (int i = 0; i < n; ++i) {
    qtemp = vector <int>(0);
    for (int j = 0; j < p; ++j) {
      cin >> temp;
      qtemp.push_back(temp);
    }
    q.push_back(qtemp);
  }

  cout << "Case #" << t+1 << ": " << solve(n, p, r, q) << endl;
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    tcase(i);
  }
  return 0;
}
