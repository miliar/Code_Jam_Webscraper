#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <string.h>
#include <set>
#include <stdio.h>
#include <assert.h>
#include <sstream>
using namespace std;

int main(int argc, char* argv[]) {
  int nocases;
  cin >> nocases;
  getchar();
  for (int rr = 1; rr <= nocases; ++rr) {
    string line;
    getline(cin, line);
    istringstream iss(line);
    string a, b;
    iss >> a >> b;
    int k = atoi(b.c_str());
    int ret = 0;
    for (int i = 0; i+k-1 < a.size(); ++i)
      if (a[i] == '-') {
	++ret;
	for (int j = 0; j < k; ++j)
	  if (a[i+j] == '-')
	    a[i+j] = '+';
          else
	    a[i+j] = '-';
      }
    bool bad = false;
    for (int i = 0; i < a.size(); ++i)
      if (a[i] == '-') {
	bad = true;
	break;
      }
    if (bad)
      printf("Case #%d: IMPOSSIBLE\n", rr);
    else
      printf("Case #%d: %d\n", rr, ret);
  }
  return 0;
}
