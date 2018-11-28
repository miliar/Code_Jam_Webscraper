#include <fstream>
#include <vector>
#include <queue>
#include <cstring>
#include <iomanip>

using namespace std;

ifstream cin ("test.in");
ofstream cout ("test.out");

const int MaxN = 105;

int T, n, q;
long double dijk[MaxN][MaxN];

class PonyType {
public:
  long double speed;
  int cap;

  PonyType(int _cap = 0, long double _speed = 0) {
    cap = _cap;
    speed = _speed;
  }
};

PonyType pony[MaxN];

class RoadType {
public:
  int nd, dist;

  RoadType(int _nd = 0, int _dist = 0) {
    nd = _nd;
    dist = _dist;
  }
};

vector <RoadType> G[MaxN];

class HeapType {
public:
  long double t;
  int nd, pony, ponyLeft;

  HeapType(int _nd = 0, int _pony = 0, int _ponyLeft = 0, long double _t = 0) {
    nd = _nd;
    pony = _pony;
    ponyLeft = _ponyLeft;
    t = _t;
  }

  bool operator < (const HeapType& other) const {
    if (t == other.t) {
      return ponyLeft > other.ponyLeft;
    }

    return t > other.t;
  }
};

priority_queue <HeapType> Heap;

long double Dijkstra(int stNode, int edNode) {
  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= n; ++j) {
      dijk[i][j] = 1000000000000000000;
    }
  }

  Heap.push(HeapType(stNode, stNode, pony[stNode].cap, 0));
  dijk[stNode][stNode] = 0;

  while (Heap.size()) {
    HeapType node = Heap.top();
    Heap.pop();

    for (RoadType nxt: G[node.nd]) {
      long double newTime = node.t + nxt.dist / pony[node.pony].speed;
      if (node.ponyLeft >= nxt.dist and newTime < dijk[nxt.nd][node.pony]) {
        dijk[nxt.nd][node.pony] = newTime;
        Heap.push(HeapType(nxt.nd, node.pony, node.ponyLeft - nxt.dist, dijk[nxt.nd][node.pony]));
      }

      newTime = node.t + nxt.dist / pony[node.nd].speed;
      if (pony[node.nd].cap >= nxt.dist and newTime < dijk[nxt.nd][node.nd]) {
        dijk[nxt.nd][node.nd] = newTime;
        Heap.push(HeapType(nxt.nd, node.nd, pony[node.nd].cap - nxt.dist, dijk[nxt.nd][node.nd]));
      }
    }
  }

  long double ans = 1000000000000000000;
  for (int i = 1; i <= n; ++i) {
    ans = min(ans, dijk[edNode][i]);
  }

  return ans;
}

int main() {
  cin >> T;
  for (int task = 1; task <= T; ++task) {
    cin >> n >> q;
    memset(pony, 0, sizeof pony);
    for (int i = 1; i <= n; ++i) {
      cin >> pony[i].cap >> pony[i].speed;
    }

    for (int i = 1; i <= n; ++i) {
      for (int j = 1; j <= n; ++j) {
        int x;
        cin >> x;
        if (x == -1) {
          continue;
        }

        G[i].push_back(RoadType(j, x));
      }
    }

    cout << "Case #" << task << ": ";
    for (int i = 1; i <= q; ++i) {
      int stNode, edNode;
      cin >> stNode >> edNode;
      cout << fixed << setprecision(10) << Dijkstra(stNode, edNode) << ' ';
    }
    cout << '\n';

    for (int i = 1; i <= n; ++i) {
      G[i].clear();
    }
  }
  return 0;
}
