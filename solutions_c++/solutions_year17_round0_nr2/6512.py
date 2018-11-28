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

  string s;

  for(int i=0; i<T; i++){
    cin >> s;
    for(int j=s.length()-1; j>0; j--){
      if(s[j-1] > s[j]){
	int k=j-1;
	while(s[k]=='0'){
	  k--;
	}
	s[k] = s[k] - 1;
	for(int l=k+1; l<s.length(); l++){
	  s[l] = '9';
	}
      }
    }
    if(s[0]=='0'){
      s.erase(0,1);
    }
    cout << "Case #" << i+1 << ": " << s  << endl; 

  }

  return 0;
}


