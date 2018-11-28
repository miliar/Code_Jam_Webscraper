#include <iostream>
#include <iomanip>
#include <string>
#include <limits.h>
#include <math.h>
#include <vector>
#include <algorithm>
#include <map>
#include <stack>
#include <numeric>
#include <cfloat>

using namespace std;

int main(int argc, char* argv[]){
  int T;
  cin >> T;

  for(int i=0; i<T; i++){
    string s;
    int T;
    cin >> s >> T;

    int count = 0;
    for(int j=0; j<s.length()-T+1; j++){
      if(s[j] == '-'){
	for(int k=j; k<j+T; k++){
	  if(s[k]=='-'){
	    s[k]= '+';
	  }
	  else{
	    s[k] = '-';
	  }
	}
	count++;
      }
    }
    for(int j=s.length()-T+1; j<s.length(); j++){
      if(s[j]=='-'){
      count = -1;
      }
    }
    if(count == -1){
      cout << "Case #" << i+1 << ": " << "IMPOSSIBLE"  << endl; 
    }
    else{
      cout << "Case #" << i+1 << ": " << count  << endl;
    }
  }

  return 0;
}


