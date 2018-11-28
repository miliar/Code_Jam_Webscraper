#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <list>

using namespace std;

int main() {
  ifstream input("bath.in");
  ofstream output("bath.out");
  string line;
  int num, i, j, n, k, soln, brk, curr, maxS, minS;
  list<int>::iterator it, place;

  getline(input, line);
  num = atoi(line.c_str());
  
  for (i = 0; i < num; i++) {
    getline(input, line);
    for (j = 0; j < line.length(); j++) {
      if (line[j] == ' ') brk = j;
    }
    
    n = atoi(line.substr(0,brk).c_str());
    k = atoi(line.substr(brk+1,string::npos).c_str());

    list<int> spaces;
    spaces.push_back(n);
    for (j = 0; j < k; j++) {
      curr = spaces.front();
      place = spaces.begin();
      for (it = spaces.begin(); it != spaces.end(); it++) {
	if (*it > curr) {
	  curr = *it;
	  place = it;
	}
      }
      spaces.erase(place);
      minS = ((curr+1)/2)-1;
      maxS = curr/2;
      spaces.push_back(minS);
      spaces.push_back(maxS);
    }
    cout << "Case #" << (i+1) << ": " << maxS << " " << minS << endl;
    output << "Case #" << (i+1) << ": " << maxS << " " << minS << endl;
  }

  return 0;
}
