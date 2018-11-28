// test.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <vector>
#include <cassert>
using namespace std;

typedef struct {
  int K;
  int S;
}Horse;


bool myfunction(Horse h1, Horse h2) { return (h1.K>h2.K); }

string compute(int D, int N, vector<Horse> horses) {
  std::sort(horses.begin(), horses.end(), myfunction);

  double max_time = 0;
  for (vector<Horse>::iterator it = horses.begin(); it != horses.end(); ++it) {
    double time = 1.0*(D - it->K) / it->S;
    if (time > max_time)max_time = time;
  }
  assert(max_time > 0);

  double result = 1.0 * D / max_time;

  return to_string(result);
}

int main() {
  ifstream in("A-large.in");
  ofstream out("out.txt");

  int T;
  int D, N;

  in >> T;
  for (int i = 1; i <= T; ++i) {
    vector<Horse> horses;
    in >> D >> N;  // read n and then m.
    for (int j = 0; j < N; j++) {
      Horse h;
      in >> h.K >> h.S;
      horses.push_back(h);
    }
    out << "Case #" << i << ": " << compute(D,N,horses) << endl;
  }

  return 0;
}