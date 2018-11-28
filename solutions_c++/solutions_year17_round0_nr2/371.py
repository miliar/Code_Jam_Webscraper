#include<iostream>
#include<cmath>
#include<string>
#include<assert.h>
#include<vector>
#include<map>

#define F0(i,n) for(i=0; i < n; i++)
#define F1(i,n) for(i=1; i < n; i++)
#define Fxy(i,x,y) for(i=x; i<y; i++)

using namespace std;

int main()
{
  const int numSize = 19;
  int c,i,j,N,numCases;
  cin >> numCases;

  F1(c, numCases+1){
    cout << "Case #" << c << ": ";

    int num[numSize];
    F0(i,numSize){
      num[i] = -1;
    }

    string numstring;
    cin >> numstring;

    F0(i,numstring.length())
      num[i] = numstring[i] - '0';

    bool solved = false;

    while(!solved){
      solved = true;
      F1(i,numSize){
	if (num[i] == -1)
	  break;
	if (num[i] < num[i-1]){
	  solved = false;
	  num[i-1]--;
	  Fxy(j,i,numSize){
	    if(num[j] == -1)
	      break;
	    num[j] = 9; 
	  }
	}
      }
    }

    i = 0;
    string ans = "";
    while(num[i] == 0)
      i++;
    Fxy(i,i,numSize){
      if(num[i] == -1)
	break;
      ans += to_string(num[i]);
    }
    cout << ans << "\n";
  }
}
