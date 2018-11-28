#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

struct Task {
  Task(int s, int e, bool l):start_(s), end_(e), label_(l) {}
  Task& operator = (const Task& other) {
    if(this != &other) {
      start_ = other.start_;
      end_ = other.end_;
      label_ = other.label_;
    }
    return *this;
  }
  int start_;
  int end_;
  bool label_;
};

bool cmp(Task a, Task b) {
  return (a.start_ < b.start_);
}

void solve(istream& ifile) {
  int T = 0;
  ifile >> T;

  for(int i = 0; i < T; ++i) {
    int AC = 0;
    int AJ = 0;
    vector<Task> TASKS;
    int exchange = 0;
    ifile >> AC >> AJ;
    for(int j = 0; j < AC; ++j) {
      int S = 0;
      int E = 0;
      ifile >> S >> E;
      TASKS.push_back(Task(S, E, false));
    }
    for(int j = 0; j < AJ; ++j) {
      int S = 0;
      int E = 0;
      ifile >> S >> E;
      TASKS.push_back(Task(S, E, true));
    }
    sort(TASKS.begin(), TASKS.end(), cmp);
    TASKS.push_back(Task(TASKS[0].start_+1440, TASKS[0].end_+1440, TASKS[0].label_));

    int l = TASKS.size();
    for(int j = 0; j < l-1; ++j) {
      if(TASKS[j].label_ == TASKS[j+1].label_) {
        if(TASKS[j+1].end_ - TASKS[j].start_ > 720) {
          exchange += 2;
        }
      } else {
        //if(TASKS[j+1].start_ - TASKS[j].start_ > 720) {
        //  exchange += 2;
        //} else {
          exchange++;
        //}
      }
    }
    /*cerr << "===========" << endl;
    for(int j = 0; j < l; ++j) {
      cerr << TASKS[j].start_ << ' ' << TASKS[j].end_ << ' ' << TASKS[j].label_ << endl;
    }
    cerr << "===========" << endl;*/
    cout << "Case #" << (i+1) << ": " << exchange << endl;
  }
}

int main(int argc, char** argv) {
  if(argc != 2) {
    cerr << "Wrong usage." << endl;
    return 0;
  }
  ifstream ifile(argv[1]);

  solve(ifile);

  return 0;
}
