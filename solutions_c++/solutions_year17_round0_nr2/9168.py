//
//  main.cpp
//  InterviewPrep
//
//  Created by mac on 20.03.17.
//  Copyright © 2017 mac. All rights reserved.
//

#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <fstream>


#include <string>
#include <algorithm>
#include <cmath>
#include <map>
#include <cassert>

using namespace std;

map<string, long long> m;

bool isOK(long long n) {
  if(n < 10)
    return true;
  int second = (n / 10) % 10;
  if(second > (n % 10))
    return false;
  return isOK(n / 10);
}

long long solve(long long n) {
  while(!isOK(n)) {
    --n;
  }
  return n;
}


int main() {
  int t;
  ifstream in("ps.txt");
  ofstream out("res");
  assert(in.good());
  
  in >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    long long num;
    in >> num;
    out << "Case #" << i << ": " << solve(num) << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
 
  return 0;
}
