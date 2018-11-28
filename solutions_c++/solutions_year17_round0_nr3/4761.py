#include <iostream>
#include <queue>
#include <vector>

using namespace std;

typedef struct {
  int start_index;
  int length;
}elem;


struct cmp_less { // elem koje vrati true nece biti na vrhu
    bool operator()(const elem a, const elem b) {
      if (a.length < b.length) return true;
      if (a.length == b.length) return a.start_index > b.start_index;
      return false;
    }
};

void print_q(priority_queue<elem, vector<elem>, cmp_less > intervals) {
  elem cur;
  cout << "QUEUE\n";
  while (!intervals.empty()) {
    cur = intervals.top();
    intervals.pop();
    cout << cur.start_index << ", " << cur.length << "\n";

  }
  cout << "\n";
}

pair<int, int> solve(int N, int K) {
  priority_queue<elem, vector<elem>, cmp_less > intervals;
  elem e;
  e.start_index = 1;
  e.length = N;
  intervals.push(e);

  pair<int, int> p;
  int middle;
  elem cur, left, right;
  for (int i=0; i<K; i++) {
    cur = intervals.top();
    intervals.pop();
    //cout << "current: " << cur.start_index << ", " << cur.length << "\n";
    if (cur.length == 0) continue;
    if (cur.length == 1) return make_pair(0, 0);

    middle = cur.start_index + (cur.length-1)/2;
    p = make_pair(cur.start_index + cur.length - 1 - middle, middle - cur.start_index);

    left.start_index = cur.start_index;
    left.length = middle - left.start_index;

    right.start_index = middle+1;
    right.length = cur.length - 1 - left.length;

    //cout << "pushing:\n";
    //cout << "lef: " << left.start_index << ", " << left.length << "\n";
    //cout << "right: " << right.start_index << ", " << right.length << "\n\n";

    intervals.push(left);
    intervals.push(right);
    //print_q(intervals);
  }
  return p;
}


int main() {
  int T;
  int N, K;

  cin >> T;
  for (int i=0; i<T; i++) {
    cin >> N >> K;
    pair<int, int> p = solve(N, K);
    cout << "Case #" << i+1 << ": " << p.first << " " << p.second << "\n";
  }
  return 0;
}
