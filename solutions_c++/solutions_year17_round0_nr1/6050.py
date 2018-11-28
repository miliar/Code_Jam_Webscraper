//
//  main.cpp
//  GoogleCodeJamQs2
//
//  Created by HarshRashiMeet on 4/7/17.
//  Copyright © 2017 Harsh. All rights reserved.
//

//#include <iostream>
//
//int main(int argc, const char * argv[]) {
//  // insert code here...
//  std::cout << "Hello, World!\n";
//  return 0;
//}


//
//  main.cpp
//  qs1-pancake
//
//  Created by HarshRashiMeet on 4/7/17.
//  Copyright © 2017 Harsh. All rights reserved.
//
//
#include <iostream>
#include <string>
#include <fstream>
#include <stdio.h>

using namespace std;

void flip(string &arr, int st, int end) {
  for (int i = st; i<=end; i++) {
    arr[i] = arr[i] == '+' ? '-' : '+';
  }
}

int min_required(string arr, int k) {
  int size = arr.length();
  int i = 0;
  int min = 0;
  while (i<size) {
    if (arr[i] == '-') {
      if ((i+k) > arr.length())
        return -1;
      flip(arr, i, i+k-1);
      min++;
    }
    i++;
  }
  return min;
}


int main(int argc, const char * argv[]) {
//  int res = min_required("---+", 3);
  ifstream in;
  ofstream os;
  os.open("output2.txt");
  in.open("A-large.in.");
  int test_cases;
  string s;
  in >> s;
  test_cases = stoi(s);
  int case_num  = 1;
  while (test_cases) {
    string arr;
    in >> arr;
    string num;
    in >> num;
    int rep = min_required(arr, stoi(num));
    string ans = rep >= 0 ? to_string(rep) : "IMPOSSIBLE";
    string res =  "Case #" + to_string(case_num++) + ": " + ans;
    os << res << endl;
    test_cases--;
  }
  
  os.close();
  //int res = min_required("-+-+-", 4);
//  cout << "min" << res << endl;
  return 0;
}
