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

string flip(string str, int startPos, int k) {
  for(int i = startPos;i < startPos + k; ++i) {
    str[i] = str[i] == '-' ? '+' : '-';
  }
  return str;
}

bool isOK(string str) {
  for(int i = 0; i < str.size(); ++i)
    if(str[i] == '-')
      return false;
  return true;
}

long long solve(string str, int k) {
  // base case
  if(str.size() == 0 || isOK(str))
    return 0;
  if(str.size() < k)
    return 9000000000;
  
  if(m.find(str) != m.end())
    return m[str];
  
  long long minVal = 9000000000;
  long long res = 0;
  for(int i = 0; i + k <= str.size(); ++i) {
    if(str[i] == '-' && (res + 1 < minVal)) {
      const string tmp = flip(str,i,k);
      res += solve(tmp.substr(1), k) + 1;
      if(res < minVal) {
        m[tmp.substr(1)] = res;
        minVal = res;
      }
    }
  }
  return minVal;
}


int main() {
  int t, k;
  ifstream in("ps.txt");
  ofstream out("res");
  assert(in.good());
  
  in >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    m.clear();
    string str;
    in >> str >> k;
    out << "Case #" << i << ": ";
    long long res = solve(str,k);
    if(res == 9000000000) out << "IMPOSSIBLE";
    else out << res;
    out << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
 
  return 0;
}
