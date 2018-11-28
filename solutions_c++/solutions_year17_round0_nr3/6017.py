#include <fstream>
#include <queue>

using namespace std;

ifstream cin ("test.in");
ofstream cout ("test.out");

// class HeapType {
// public:
//   int val, pos;

//   HeapType(int _val = 0, int _pos = 0) {
//     val = _val;
//     pos = _pos;
//   }

//   bool operator < (const HeapType& other) const {
//     if (val == other.val) {
//       return pos > other.pos;
//     }

//     return val < other.val;
//   }
// };

priority_queue <int> Heap;

int main() {
  int T;
  cin >> T;
  for (int task = 1; task <= T; ++task) {
    long long n, k;
    cin >> n >> k;
    while (Heap.size()) {
      Heap.pop();
    }

    Heap.push(n);
    for (int i = 1; i <= k; ++i) {
      int top = Heap.top();
      Heap.pop();

      int val1 = (top - 1) / 2;
      int val2 = (top - 1) - val1;
      Heap.push(val1);
      Heap.push(val2);

      if (i == k) {
        cout << "Case #" << task << ": " << max(val1, val2) << ' ' << min(val1, val2) << '\n';
      }
    }
  }
  return 0;
}