//============================================================================
// Name        : round0.cpp
// Author      : rodrijuana
// Date	(D/M/Y): 12/04/2013
//============================================================================
#include <fstream>
#include <string>
#include <math.h>
#include <iostream>
#include <stdlib.h>   

using namespace std;

int main() {
	
  ifstream input("B-large.in");
  ofstream output("B-large.out");

  int cnt, CNT;
  std::string n;
  bool fill = false;

  input >> CNT;
  printf("%d\n", CNT);

  for (cnt = 1; cnt <= CNT; cnt++) {   
    //get case 
    input >> n;
    fill = false;
    bool done = false;
    while (!done) {
      for (int i = 1; i < n.length(); i++) {        
        if(!fill) {
          if (n[i] < n[i-1]) {
            n[i] = '9';
            n[i-1] = n[i-1]-1;
            fill = true;
          }
        } else {
          n[i] = '9';
        }
      }
      if (!fill)  done = true;
      fill = false;
    }

    unsigned long long int aux = strtoull(n.c_str(), NULL, 10);
    output << "Case #" << cnt << ": " << aux <<'\n';
  }
}
