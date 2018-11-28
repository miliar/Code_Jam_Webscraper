#include <iostream>
#include <queue>
#include <vector>
#include <functional>

using namespace std;

class pos {
  public:
    int min;
    int max;
};

struct PosComparator {
  bool operator()(const pos& lhs, const pos& rhs ) const {
    if ( lhs.max != rhs.max ) {
      return lhs.max < rhs.max;
    } else {
      return lhs.min < rhs.min;
    }
  }
};

int main() {
  int t;
  cin >> t;

  for(int z = 1; z <= t; z++) {
    int n, k;

    cin >> n >> k;

    if ( n == k ) {
      cout << "Case #" << z << ": " << "0" << " " << "0" << endl;
      continue;
    }

    if ( k == 1 ) {
      if ( n % 2 == 0 ) {
        int max = n / 2;
        int min = n / 2 - 1;
        if ( min < 0 ) min = 0;
        cout << "Case #" << z << ": " << max << " " << min << endl;
      } else {
        cout << "Case #" << z << ": " << n / 2 << " " << n / 2 << endl;
      }
      continue;
    }

    priority_queue<pos, vector<pos>, PosComparator> q;

    if ( n % 2 == 0 ) {
      // even
      pos p;
      p.min = n / 2 - 1;
      if ( p.min < 0 ) p.min = 0;
      p.max = n / 2;

      q.push(p);
    } else {
      pos p;
      p.min = n / 2;
      p.max = n / 2;
      q.push(p);
    }

    int cnt = 0;
    pos last;
    while(q.size() != 0) {
      pos p = q.top();
      q.pop();

      cnt++;
      if ( cnt == k || (p.max == 0 && p.min == 0)) {
        last = p;
        break;
      } else {
        if ( p.max % 2 == 0 ) {
          pos tmp;
          tmp.min = (p.max / 2) - 1;
          if ( tmp.min < 0 ) tmp.min = 0;
          tmp.max = p.max / 2;
          q.push(tmp);
        } else {
          pos tmp;
          tmp.min = p.max / 2;
          tmp.max = p.max / 2;
          q.push(tmp);
        }

        if ( p.min % 2 == 0 ) {
          pos tmp;
          tmp.min = (p.min / 2) - 1;
          if ( tmp.min < 0 ) tmp.min = 0;
          tmp.max = p.min / 2;
          q.push(tmp);
        } else {
          pos tmp;
          tmp.min = p.min / 2;
          tmp.max = p.min / 2;
          q.push(tmp);
        }
      }
    }

    cout << "Case #" << z << ": " << last.max << " " << last.min << endl;
  }

  return 0;
}