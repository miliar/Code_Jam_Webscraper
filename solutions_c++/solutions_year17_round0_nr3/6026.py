#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <math.h>

using namespace std;

bool myfunction (int i,int j) { return (i<j); }

string convertInt2Str(long long number)
{
   stringstream ss;
   ss << number;
   return ss.str();
}


int main() {
 // cin >> noskipws; 
vector<int> numbersToCalc;
  int t, N, K;
  int y,z;
  int power, no;
  int tempNum, other;
  float temperFloat;
  int max, min;
  long long numberInt;
  string number, ans;
  char c;
  bool calced;
  char dummy; //for new line read in
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
 
  for (int caseNo = 1; caseNo <= t; ++caseNo) {
  	cin >> N;
  	cin >> K;
    
    temperFloat = (K+1);
    power = 0;
    
    while(temperFloat > 1){
      temperFloat /= 2;
      ++power;
    }
 //   cout << power << endl;

    no= N;
    for(int i =0; i < power; ++i){
      no -= pow(2,i);
    }

    tempNum = (no /( pow(2,power)));
    other = no - pow(2,power)*(tempNum);

    if(other >= (K-(pow(2,power-1)-1))){
      y = tempNum + 1;
    }else{
      y = tempNum;
    }

    if(other >= (pow(2,power-1) + (K-(pow(2,power-1)-1)))){
      z = tempNum +1;
    }else{
      z= tempNum;
    }


    		
  	

   cout << "Case #" << caseNo << ": " << y << " " << z <<endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
}