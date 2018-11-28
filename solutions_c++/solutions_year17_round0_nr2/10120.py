#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <cstdio>
#include <fstream>
#include <stdlib.h>
#include <string>
#include <algorithm>
#include <stack>
#include <sstream>
#include <cmath>

using namespace std; 

bool limits_check_out(float n);
bool are_numbers_increasing(float n);
float compute(float n);

string dataSetType = "small";

int main(int, char*[]) {

	string line;
	vector<float> cases;
	int first = 1;
	int numberOfCases = 0;
	ifstream infile("B-small-attempt0.in");
	while ( getline(infile, line) ) {
    float value = strtof((line).c_str(), 0);
    if (first == 1) { 
      numberOfCases = value;
      first = 0; 
    }
    else { 
      cases.push_back(value);
    }
	}

	if (! ((1 <= numberOfCases) && (numberOfCases <= 100)) ) {
      exit(EXIT_SUCCESS);
	}
  for (int currCaseNum = 1; currCaseNum <= numberOfCases; currCaseNum = currCaseNum + 1) {
    float n = cases[currCaseNum-1];
	  if( !(limits_check_out(n)) ) {
	  	continue;
	  }
  
    float lastTidyNum = compute(n);
  
    cout << "Case #" << currCaseNum << ":  " << lastTidyNum << "\n" << std::flush;
  
  }

}

float compute(float n){

  float tidyNum = 0;

  for (float currN = 1; currN <= n; currN = currN + 1) {
    if ( are_numbers_increasing(currN) ){
      tidyNum = currN;
    }
  }

  return tidyNum;
}

bool are_numbers_increasing(float n) {

  float tN = n;
  int lastDigit = 0;
  std::stack<int> sd;

  while (tN > 0){
    int digit = fmod(tN, 10);
    tN /= 10;
    sd.push(digit);
  }

  while (!sd.empty()){
    int nextDigit = sd.top();
    sd.pop();
     if ( !(nextDigit >= lastDigit ) ) {
       return false;
     }
     lastDigit = nextDigit;
  }


  return true;
}

bool limits_check_out(float n) {

  //1 ≤ N ≤ 1000.
  if (dataSetType.compare("small") == 0) {
    if (!((1 <= n) && (n <= 1000))) {
      return 0;
    }
  }
  //1 ≤ N ≤ 10^18.
  if (dataSetType.compare("large") == 0) {
    double hl = 10e18;
    if (!((1 <= n) && (n <= hl))) {
      return 0;
    }
  }

  return 1;
}
