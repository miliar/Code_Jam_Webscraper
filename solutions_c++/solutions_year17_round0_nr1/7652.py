/*
  @author Himanshu Dixit
  Codejam Problem A
 */
#include<iostream>
#include<algorithm>
#include<string>
#include<math.h>
#include<vector>
#include<stack>
using namespace std;
/*
  Check if the cookie is complete happy
 */
bool cH(string Str){
  // Run the loop
  for(long long int i = 0; i < Str.length(); i++) {
    if(Str[i] == '-')
      return false;
  }
  return true;
}

int main() {
  long long int T;
  cin >> T;
  for(long long int z = 0; z < T; z++){
    string Str;
    cin >> Str;
    long long int K;
    cin >> K;

    
    unsigned long long int minim = 0;
    for(unsigned long long int i=0; i<Str.length() && (i+K)<=Str.length(); i++){
      if(Str[i]=='-'){
	for(long long int j = i; j < i + K; j++){
	  if(Str[j] == '-')
	    Str[j] = '+';
	  else
	    Str[j] = '-';
	}
	// Increment the min number
	minim++;
      }
    }
    // Print it in standards
    cout << "Case #" << z+1 << ": ";
    if(minim>=0 && cH(Str))
      cout << minim;
    else
      cout << "IMPOSSIBLE";
    // End the line
    cout << endl;
  }
  return 0;
}
