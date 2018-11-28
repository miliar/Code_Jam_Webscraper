/* GCJ 2017 Qualifier Problem C */

#include <iostream>
#include <vector>
#include <list>
#include <queue>

using namespace std;

// #define DEBUG

struct stall {
  unsigned long start, end; // positions of start/end
  unsigned long mid; // position of best stall
  unsigned long L_s, R_s;
  unsigned long min_L; // min(L_s, R_s)
  unsigned long max_L; // max(L_s, R_s)
};

// Compute the best stall in an interval:
void best_stall(unsigned long start, unsigned long end, stall &st) {
  st.start = start; st.end = end;
  st.mid = (st.start+st.end)/2; // TODO check rounding
  st.L_s = st.mid-(st.start); // distance of 0 if adjacent
  st.R_s = (st.end)-st.mid;   // distance of 0 if adjacent
  st.min_L = min(st.L_s, st.R_s);
  st.max_L = max(st.L_s, st.R_s);
}

#ifdef DEBUG
void print_stall(stall &st) {
  cout << "(" << st.start << "," << st.end << ") w/mid "
       << st.mid << " (L_s = " << st.L_s
       << ", R_s = " << st.R_s
       << ", min_L = " << st.min_L
       << ", max_L = " << st.max_L << ")" << endl;
}
#endif

int compare_stalls(stall &st1, stall &st2) {
  // Prefer larger min_L:
  if (st1.min_L > st2.min_L) return 1;
  if (st1.min_L < st2.min_L) return -1;

  // Or prefer larger max_L:
  if (st1.max_L > st2.max_L) return 1;
  if (st1.max_L < st2.max_L) return -1;

  // Or prefer leftmost stall:
  //cerr << "PICKING LEFT" << endl;
  return st1.start < st2.start;
}

class my_compare {
public:
  bool operator() (stall &st1, stall &st2) {
    int k = compare_stalls(st1, st2);
    return k < 1;
  }
};

struct stall_list {
  list<stall> available;
  priority_queue<stall, vector<stall>, my_compare> best_available;

  stall_list(unsigned long N) {
    stall st; best_stall(1, N, st);
    best_available.push(st);
  }

  void next_split(stall &st) {
    st = best_available.top(); best_available.pop();
#ifdef DEBUG
      cout << "SPLIT "; print_stall(st);
#endif
    unsigned long start = st.start, end = st.end;
    if (start == end) return; // -- no more empty stalls here
    if (st.mid != start) { // -- add [start..mid)
      stall st1; best_stall(start, st.mid-1, st1);
#ifdef DEBUG
      cout << "-> "; print_stall(st1);
#endif
      best_available.push(st1);
    }
    if (st.mid != end) { // -- add (mid..end]
      stall st2; best_stall(st.mid+1, end, st2);
#ifdef DEBUG
      cout << "-> "; print_stall(st2);
#endif
      best_available.push(st2);
    }
  }
};

void testcase(int case_no) {
  unsigned long N, K; cin >> N >> K;

  // Basic algorithm:
  // - linked-list of stall intervals (runs of empty stalls)
  // - find the best stall inside an interval
  // - repeat K times
  // - return result for K+1st time
  stall_list sts(N);
  stall st;
  for (unsigned long i = 0; i < K; i++) {
    sts.next_split(st);
  }

  // print final stall st:
  cout << "Case #" << case_no << ": ";
  cout << st.max_L << " " << st.min_L << endl;
}
 
int main()
{
  int T; cin >> T;
  for (int i = 0; i < T; i++)
    testcase(i+1);
  return 0;
}
