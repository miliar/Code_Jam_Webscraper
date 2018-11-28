#include <iostream>
#include <deque>
#include <cmath>
#include <cstdbool>
#include <vector>
#include <algorithm>
using namespace std;

typedef struct node node_t;
struct node {
  long long int stall, left_lim, right_lim;
  bool operator<( const node& n ) const {
    long long int n_priority = n.right_lim - n.left_lim - 1;
    long long int priority = right_lim - left_lim - 1;
    if (n_priority != priority) {
      return priority > n_priority;
    } else {
      return stall < n.stall;
    }
  }
};

node_t make_node(long long int stall, long long int left_lim,
  long long int right_lim) {
  node_t node;
  node.stall = stall;
  node.left_lim = left_lim;
  node.right_lim = right_lim;
  return node;
}

void print_deque(deque<node_t> q) {
  for (int i=0; i<q.size(); i++) {
    node_t s = q.at(i);
    cout << "(" << s.stall << ", " << s.right_lim-s.left_lim-1 << "), ";  
  }
  cout << endl;
}

void queue_left_stall(deque<node_t> *q, node_t s) {
  if (s.right_lim - s.stall > 1) {
    int stall = s.stall + (s.right_lim-s.stall)/2;
    (*q).push_back(make_node(stall, s.stall, s.right_lim));
  }
}

void queue_right_stall(deque<node_t> *q, node_t s) {
  if (s.stall - s.left_lim > 1) { 
    int stall = s.left_lim + (s.stall-s.left_lim)/2;
    (*q).push_back(make_node(stall, s.left_lim, s.stall));
  }
}

int main() {
  int t;
  long long int N, K;
  cin >> t;
  
  for (int i = 1; i <= t; ++i) {
  	cin >> N >> K;
    if (N == K) {
      cout << "Case #" << i << ": " << "0 0" << endl;
      continue;
    }
    deque<node_t> q;
    long long int k = 1, empty_stall_len, stall;
    stall = (N % 2 == 0) ? (N/2) : (N/2+1);
    q.push_back(make_node(stall, 0, N+1));
    node_t s, s2;

    while (k <= K) {
      sort(q.begin(), q.end());
      //print_deque(q);
      s = q.front();
      q.pop_front();
      /*vector<node_t> v;
      v.push_back(s);
      while (!q.empty()) {
        s2 = q.front();
        if (s2.right_lim - s2.left_lim - 1 == s.right_lim - s.left_lim - 1) {
          q.pop_front();
          v.push_back(s2);
        } else {
          break;
        }
      }
      if (v.size() > 1) {
        sort(v.begin(), v.end());
        for (int z=v.size()-1; z>0; z--) {
          q.push_front(v[z]);
        }
      }
      s = v[0];
      */
      //cout << s.stall << " has been filled." << endl;

      empty_stall_len = s.right_lim - s.left_lim - 1;
      if (empty_stall_len % 2 == 0) { // queue right first
        queue_left_stall(&q, s);
        queue_right_stall(&q, s);
      } else { // queue left first
        queue_right_stall(&q, s);
        queue_left_stall(&q, s);
      }
      k++;
    } 
    long long int Ls = s.stall - s.left_lim - 1;
    //cout << s.stall << " " << s.left_lim << endl;

    long long int Rs = s.right_lim - s.stall - 1;
    //cout << Ls << " " << Rs << endl;
    cout << "Case #" << i << ": " << max(Ls, Rs) 
         << " " << min(Ls, Rs) << endl;
  }
  return 0;

}