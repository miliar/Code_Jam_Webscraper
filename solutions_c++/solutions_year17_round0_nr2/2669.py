#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

bool tidy(long long int a) {
  long long int last = 9;
  while(a != 0) {
    if(a % 10 > last)
      return false;
    last = min(last, a % 10);
    a /= 10;
  }

  return true;
}

int main(int argc, char** argv) {
  if(argc != 2) 
    return -1;

  ifstream in {argv[1]};
  int loops;
  int loop = 0;
  for(in >> loops; loops > 0; --loops) {

    long long int num;
    in >> num;
    long long int cut = 0;
    long long int mult = 10;
    long long int tidied = num;
    while(!tidy(tidied)) {
      tidied -= tidied % mult + 1;
      mult *= 10;
    }

    cout << "Case #" << ++loop << ": " << tidied << endl;
  }

  
}
