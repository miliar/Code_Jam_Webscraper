#include <iostream>
#include <queue>
#include <utility>
using namespace std;

struct node {
  long long pos;
  long long left;
  long long right;
  long long parentFrom;
  long long parentTo;

  long long minDist() {
    return min(left, right);
  }

  long long maxDist() {
    return max(left, right);
  }

  void print() {
    printf("(%lld %lld %lld %lld %lld)\n", pos, left, right, parentFrom, parentTo);
  }
};


struct cmp {
  bool operator()(node n1, node n2) {
    return make_tuple(n1.minDist(), n1.maxDist(), -n1.pos) < make_tuple(n2.minDist(), n2.maxDist(), -n2.pos);
  }
};

long long n, k;

bool hasMiddle(long long from, long long to) {
  return (from + to)/2 != from;
}

node createNode(long long from, long long to) {
  long long middle = (from + to)/2;
  return node { middle, middle - from - 1, to - middle -1, from, to };
}

tuple<long long, long long, long long> rec(long long pos) {
  if(pos == 1) {
    return make_tuple(n, pos%2, !(pos%2));
  }

  long long cnt, big, small;

  std::tie(cnt, big, small) = rec(pos/2);

  long long nbig = 0, nsmall = 0;
  if(cnt%2 == 1) {
    nbig += big * 2 + small;
    nsmall += small;
  } else {
    nbig += big;
    nsmall += 2*small + big;
  }

  return make_tuple(cnt/2, nbig, nsmall);
}

void solve() {
  priority_queue<node, vector<node>, cmp> q;

  cin >> n >> k;
  n+= 2;

  q.push(createNode(1, n));

  while(k-- > 1) {
    node temp = q.top();
    //cout << "pop " ; temp.print();
    q.pop();
    if(hasMiddle(temp.parentFrom, temp.pos)) {
      //cout << "create " ; createNode(temp.parentFrom, temp.pos).print();
      q.push(createNode(temp.parentFrom, temp.pos));
    }

    if(hasMiddle(temp.pos, temp.parentTo)) {
      //cout << "create " ; createNode(temp.pos, temp.parentTo).print();
      q.push(createNode(temp.pos, temp.parentTo));
    }
  }

  node ret = q.top();
  cout << ret.maxDist() << " " << ret.minDist() << endl;
}

void solve2() {
  cin >> n >> k;

  long long l, big, small;
  tie(l, big, small) = rec(k);
  //cout << l <<" "<< big<<" " << small << endl;

  long long x = 1;
  while(2*x <= k) x *= 2;
  k -= x;

  k++;
  long long left, right;
  if(k > big) {
    l--;
  }

  left = l/2;
  right = (l-1)/2;
  cout << max(left, right) << " " << min(left, right) << endl;
}

int main () {
  int t;

  cin >> t;
  for(int i = 1; i <= t; i++)
  {
    printf("Case #%d: ", i);
    solve2();
  }

  return 0;
}
