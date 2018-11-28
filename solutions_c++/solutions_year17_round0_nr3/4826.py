#include <iostream>
#include <deque>

using namespace std;

typedef tuple<unsigned long, unsigned long> ResultT;

struct Node {
  Node(unsigned long n, unsigned long v) : numElements(n), val(v) {
    // empty
  }
  unsigned long numElements;
  unsigned long val;
};

static unsigned GetMaxInterval(unsigned long N, unsigned long K) {
  deque<Node> q;

  unsigned long val = N;
  unsigned long nElements = 1;
  q.emplace_back(nElements, val);

  unsigned long processed = 0;
  while (processed < K) {
    Node n = q.front();
    val = n.val;
    q.pop_front();
    nElements = n.numElements;
    if (val % 2 == 0) {
      unsigned long left = (val / 2) - 1;
      unsigned long right = (val / 2);
      if (q.size() && (q.back().val == right)) {
        q.back().numElements += nElements;
      } else {
        q.emplace_back(nElements, right);
      }
      if (left > 0) {
        q.emplace_back(nElements, left);
      }
    } else {
      unsigned long right = (val / 2);
      if (q.size() && (q.back().val == right)) {
        q.back().numElements += 2 * nElements ;
      } else {
        q.emplace_back(2 * nElements, right);
      }
    }
    processed += min(nElements, K - processed);
  }
  return val;
}

static ResultT GetMinMax(unsigned long N, unsigned long K) {
  unsigned long s = GetMaxInterval(N, K);
  unsigned long Ls = (s % 2 == 0) ? (s / 2) - 1 : (s / 2);
  unsigned long Rs = s / 2;
  return make_tuple(Rs, Ls);
}

ostream& operator<<(ostream& out, const ResultT& result) {
  out << get<0>(result) << " " << get<1>(result);
  return out;
}

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; ++t) {
    unsigned long N, K;
    cin >> N >> K;
    cout << "Case #" << (t + 1) << ": " << GetMinMax(N, K) << endl;
  }

  return 0;
}
