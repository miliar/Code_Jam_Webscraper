//
//  main.cpp
//  GoogleCodeJam2017
//
//  Created by HarshRashiMeet on 4/7/17.
//  Copyright © 2017 Harsh. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

bool checkIfAllSame(int N) {
  string n= to_string(N);
  for (int i = n.length() - 1; i>0; i--) {
    int left = n[i-1] - '0';
    int right = n[i] - '0';
    if (left != right)
      return false;
  }
  return true;
}

//int getLastTidyNumber(int N) {
//  if (checkIfAllSame(N))
//    return N;
//  string n= to_string(N);
//  for (int i = n.length() - 1; i>0; i--) {
//    int left = n[i-1] - '0';
//    int right = n[i] - '0';
//    if (left >= right) {
//      left = left == 0 ? 0 : left-1;
//      right = 9;
//    }
//    n[i] = right + '0';
//    n[i-1] = left + '0';
//    
//  }
//  return stoi(n);
//}

int getLastTidyNumber(int N) {
  bool changed =true;
  if (checkIfAllSame(N))
    return N;
  string n= to_string(N);
  for (int i = 0; i<n.length()-1; i++) {
    int left = n[i] - '0';
    int right = n[i+1] - '0';
    if (left > right) {
     left =  changed ? left - 1:left;
      changed = false;
      right = 9;
    }
    n[i] = left + '0';
    n[i+1] = right + '0';
    
  }
  return stoi(n);
}

void getTidyHelper(string &n, long index) {
  if (index <= 0)
    return;
  int left = n[index-1] - '0';
  int right = n[index] - '0';
  if(left > right) {
    n[index-1] = left - 1 + '0';
    n[index] = '9';
  }
  getTidyHelper(n, index-1);
  left = n[index-1] - '0';
  right = n[index] - '0';
  if(left > right) {
//    n[index-1] = left - 1 + '0';
    n[index] = '9';
  }
}


long getLastTidyNumberRec(long N) {
  string n = to_string(N);
  getTidyHelper(n, n.length()-1);
  return stol(n);
}




int main(int argc, const char * argv[]) {
  // insert code here...
  ifstream in;
  ofstream of;
  of.open("output2.txt");
//   int res =  getLastTidyNumberRec(665);
  in.open("B-large.in");
  string test_case_str;
  in >> test_case_str;
  int test_cases = stoi(test_case_str);
  int case_num = 1;
  
  while (test_cases) {
    string curr_input_str;
    in >> curr_input_str;
    long N = stol(curr_input_str);
    string out = "Case #" + to_string(case_num++) + ": " + to_string(getLastTidyNumberRec(N));
//    cout << out << endl;
    of << out << endl;
    test_cases--;
    
  }
  of.close();
  return 0;
}


