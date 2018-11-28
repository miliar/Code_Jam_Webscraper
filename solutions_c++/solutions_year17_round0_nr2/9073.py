#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;



string solve(string digs) {
	int eqrun = 0;
  int stop = 0;
  string eqval = "";
  long ans = 0;
  char *end;
  char *end2;
  int endok = 0;

  if (digs.length()>1) {
    for (int i = 1; i<digs.length(); i++) {
      if ((digs[i]) > (digs[i-1])) {
        eqrun=0;
        eqval = "";
        endok = 1;
        continue;
      }
      else if ((digs[i]) == (digs[i-1])) {
        eqrun++;
        if (eqrun>0) {
          eqval = eqval+digs[i];
          //printf("%s and num=%d\n",eqval.c_str(),eqval.length());
          endok = 1;
        }
        continue;
      }
      else {
        for (int j = i; j<digs.length();j++) {
          eqval += digs[j];
        }
        ans = strtol(digs.c_str(),&end,10) - (strtol(eqval.c_str(),&end2,10)+1);
        endok = 0;
        return (to_string(ans));
      }

    }
    
  }
  
  return digs;


}


int main(void) {
    /* number of test cases */
    unsigned short int t;
    // int c, n, tmp;
    string digs;

    cin >> t;

    for(int i=1; i <= t; i++) { //loops for each case
        cin >> digs;
        
        cout << "Case #" << i << ": " << solve(digs) << endl;
    }

    return 0;
}

