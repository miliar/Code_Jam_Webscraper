//
//  main.cpp
//  round1B
//
//  Created by HarshRashiMeet on 4/22/17.
//  Copyright © 2017 Harsh. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

double find_min_speed(vector<pair<double, double>> horses, long dest) {
  double max_time = INT_MIN;
  for (auto i : horses) {
    double curr_time = (dest - i.first) / i.second;
    max_time = max(max_time, curr_time);
  }
  double res  = (dest / max_time);
  return res;
}



int main(int argc, const char * argv[]) {
  // insert code here...
  std::cout << "Hello, World!\n";
  ifstream in;
  ofstream out;
  in.open("A-large.in-2.txt");
  out.open("out4.txt");
  int test_cases = 0;
  in >> test_cases;
  int case_num = 1;
  while (test_cases) {
    long dest = 0;
    in >> dest;
    int horses;
    in >> horses;
    vector<pair<double,double>> h_data;
    while (horses) {
      pair<double,double> curr;
      in >> curr.first;
      in >> curr.second;
      h_data.push_back(curr);
      horses --;
    }
    test_cases --;
    string res = "Case #" + to_string(case_num++) + ": " + to_string(find_min_speed(h_data, dest));
    out << res << endl;
  }
  return 0;
}
