#include <iostream>
#include <string>
using namespace std;

int main(){
  int numTests;
  cin >> numTests;
  for(int testNum = 0; testNum < numTests; testNum++){
    string number;
    cin >> number;
    bool done = false;
    while(!done){
      done = true;
      char lastChar = number[0];
      bool setNinesMode = false;
      for(int i = 1; i < number.length(); i++){
	if(!setNinesMode){
	  if(number[i] < lastChar){
	    done = false;
	    setNinesMode = true;
	    number[i-1]--;
	    number[i] = '9';	  
	  }
	}else{
	  number[i] = '9';
	}
	lastChar = number[i];
      }
    }
    while(number[0] == '0'){
      number.erase(0,1);
    }
    cout << "Case #" << testNum + 1 << ": " << number << endl;
  }
  return 0;
}
