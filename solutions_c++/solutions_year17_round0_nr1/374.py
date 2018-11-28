#include<iostream>
#include<cmath>
#include<string>
#include<assert.h>
#include<vector>
#include<map>

#define F0(i,n) for(i=0; i < n; i++)
#define F1(i,n) for(i=1; i < n; i++)
#define Fxy(i,x,y) for(i=x; i < y; i++)

using namespace std;

int main()
{
  int MAX_SIZE = 1000;
  int c, i, j, K, numCases;
  string s;
  bool possible;
  cin >> numCases;

  F1(c, numCases+1){
    cout << "Case #" << c << ": ";

    cin >> s >> K;
    cerr << "Case #" << c << "-> S: " << s << ", K: " << K << "\n";

    int flips = 0;

    F0(i, s.length()-K+1){
      if (s[i] == '-'){
	flips++;
	Fxy(j,i,i+K){
	  if (s[j] == '+'){
	    s[j] = '-';
	  } else {
	    s[j] = '+';
	  }
	}
	cerr << "after " << flips << " flips we have " << s << "\n";
      }
    }

    possible = true;

    F0(i, s.length()){
      if (s[i] == '-'){
	possible = false;
	break;
      }
    }

    if(possible){
      cout << flips << "\n";
    } else { 
      cout << "IMPOSSIBLE\n";
    }
  }
}
