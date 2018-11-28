#include <string>
#include <iostream>
#include <queue>
using namespace std;

class Node {
public:
  int l, r;

  Node(const int& l, const int& r) {
    this->l = l;
    this->r = r;
  }
};

class Comparison {
public:
  bool operator() (const Node& lhs, const Node& rhs) {
    int disL = lhs.r - lhs.l;
    int disR = rhs.r - rhs.l;
    if (disL == disR) {
      return lhs.l > rhs.l;
    }
    return disL < disR;
  }
};

bool arr[1000001];

int main() {
  int T, N, K;
  cin >> T;
  for (int c = 1; c <= T; ++c) {
    cin >> N >> K;
    for (int i = 0; i < N; ++i) {
      arr[i] = false;
    }
    int l = 0;
    int r = N - 1;
    priority_queue<Node, vector<Node>, Comparison> q;
    q.push(Node(l , r));
    int last = 0;
    while (K--) {
      Node n = q.top();
      q.pop();
      int mid = (n.l + n.r) >> 1;
      arr[mid] = true;
      last = mid;
      if (n.l == n.r) {
        continue;
      }
      if ((n.r - n.l + 1) % 2) {
        if (mid - 1 >= n.l) {
          q.push(Node(n.l, mid - 1));
        }
        q.push(Node(mid + 1, n.r));
      } else {
        q.push(Node(mid + 1, n.r));
        if (mid - 1 >= n.l) {
          q.push(Node(n.l, mid - 1));
        }
      }
    }


    int left = 0;
    int right = 0;
    int p = last - 1;
    while (p >= 0) {
      if (arr[p]) {
        break;
      }
      left++;
      p--;
    }
    p = last + 1;
    while (p < N) {
      if (arr[p]) {
        break;
      }
      right++;
      p++;
    }
    int minAns = min(left, right);
    int maxAns = max(left, right);

    cout << "Case #" << c << ": " << maxAns << " " << minAns << "\n";
  }
  return 0;
}
