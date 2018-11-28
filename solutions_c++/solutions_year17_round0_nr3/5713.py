#include <cstdio>
#include <set>
#include <stack>
#include <utility>
#include <vector>
#include <queue>
#include <map>
#include <iostream>
#include <cassert>
#include <cmath>
#include <algorithm>
#include <climits>

using namespace std;

template <typename A> void print(A x) {
    cout << x << endl;
}

template <typename A> void print(vector<A> v) {
    cout << v.size() << ": ";
    for (auto x : v) {
        cout << x << " ";
    }
    cout << endl;
}

#define loop(x,a,b) for(int x = a; x < b; ++x)

typedef long long ll;
typedef pair<int, int> pii;
using namespace std;

int T;

struct Node {
  int ls;
  int rs;
  Node *left;
  Node *right;
  bool isLeave() {
    return (left == NULL && right == NULL);
  }
};

tuple<Node *, int> pick_leaf(Node *n) {
  if (n->isLeave()) {
    return {n, n->rs - n->ls};
  } else {
    Node *n1 = n->left;
    Node *n2 = n->right;
    Node *res1, *res2;
    int n_res1, n_res2;
    tie(res1, n_res1) = pick_leaf(n1);
    tie(res2, n_res2) = pick_leaf(n2);
    if (n_res1 >= n_res2) {
      return {res1, n_res1};
    }  else {
      return {res2, n_res2};
    }
  }
}

pii solve(int n, int k) {
  Node *root = new Node({0, n+1, NULL, NULL});
  int new_stall;
  int ls = 0;
  int rs = 0;
  loop(i,0,k) {
    Node *leaf;
    tie(leaf, ignore) = pick_leaf(root);
    ls = leaf->ls;
    rs = leaf->rs;
    new_stall = (rs + ls) / 2;
    Node *n1 = new Node({ls, new_stall, NULL, NULL}); 
    Node *n2 = new Node({new_stall, rs, NULL, NULL}); 
    cout << "add " << new_stall << " between " << leaf->ls << " and " << leaf->rs << endl;
    assert(new_stall > ls && new_stall < rs);
    leaf->left = n1;
    leaf->right = n2;
  }
  int d1 = new_stall - ls - 1;
  int d2 = rs - new_stall - 1;
  return {max(d1, d2), min(d1,d2)};
}

pii dist(int ls, int rs) {
  int stall = (rs + ls) / 2;
  int d1 = stall - ls - 1;
  int d2 = rs - stall - 1;
  return {max(d1,d2), min(d1,d2)};
}

struct mypair {
  int ls;
  int rs;

  bool operator<(mypair const &p) const { 
    int mi1,mi2,ma1,ma2;
    tie(ma1,mi1) = dist(ls,rs);
    tie(ma2,mi2) = dist(p.ls,p.rs);
    if (ma1 < ma2) {
        return true;
    }
    if (ma2 < ma1) {
      return false;
    }
    if (mi1 < mi2) {
      return true;
    }
    if (mi2 < mi1) {
      return false;
    }
    return ls > p.ls; 
  }

};

pii solve2(int n, int k) {
  mypair init = {0, n+1};
  priority_queue<mypair> q;
  q.push(init);

  mypair current;
  loop(i,0,k) {
    current = q.top(); q.pop();
    int new_stall = (current.rs + current.ls) / 2; 
    mypair p1 = {current.ls, new_stall};
    mypair p2 = {new_stall, current.rs};
    q.push(p1);
    q.push(p2);
  }

  return dist(current.ls, current.rs);

}


int main(int nargs, char **argv) {
    std::ios::sync_with_stdio(false);
    cin >> T;
    loop(i,0,T) {
      cout << "Case #" << i + 1<< ": ";
      int N, K;
      cin >> N >> K;
      auto res = solve2(N, K);
      cout << res.first << " " << res.second << endl;; 
    }
    return 0;
}
