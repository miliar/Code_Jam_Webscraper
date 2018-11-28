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
//	  ifstream input("inputA-small.txt");
  ifstream input("A-large.in");
  ofstream output("A-large.out");

  int cnt, CNT;
  std::string s;
  std::string s2;
  std::string s3;
  int l;
  int found;
  int out;

  input >> CNT;


 
  for (cnt = 1; cnt <= CNT; cnt++) {   
    //get case 
    input >> s;
    input >> l;
    printf("%s\n", s.c_str());
    printf("%d\n", l);
     
    out = 0;
    
    for (int i = 0; i < s.length() - l +1; i++) {
      if (s[i] == '-') {
        for (int aux = 0; aux < l; aux++) {
 
          if (s[i + aux] ==  '-')
            s[i + aux] = '+';
          else 
            s[i + aux] = '-';

          
        }
        out++;
      }
      printf("%s\n", s.c_str());
    }

   

    bool impossible = false;
    for (int aux = 0; aux < s.length(); aux++) {
      if(s[aux] == '-') impossible = true;
    }
 
    if (impossible)
      output << "Case #" << cnt << ": IMPOSSIBLE" << '\n';
    else
      output << "Case #" << cnt << ": " << out <<'\n';
  }
}
