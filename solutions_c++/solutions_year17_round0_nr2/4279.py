#include <cstring>
#include <iostream>
using namespace std;

int main() {
  int nex;
  string stringInput;
  int posToDecree;
  bool failed;

  cin >> nex;

  for(int indEx = 1; indEx <= nex; indEx++) {
    cin >> stringInput;

    posToDecree = 0;
    failed = false;
    for(int i = 1; i < stringInput.size();i++) {
      if(stringInput[i-1] < stringInput[i]) {
	posToDecree = i; 
      } else if(stringInput[i-1] > stringInput[i]) {
	failed = true;
	break;
      }
    }

    if(failed == false) {
      cout << "Case #" << indEx << ": " <<  stringInput << endl;
    } else {
      cout << "Case #" << indEx << ": ";
      for (int i = 0; i < posToDecree; i ++) {
	cout << stringInput[i];
      }
     
      if(posToDecree > 0 or (posToDecree==0 and stringInput[0] != '1')){cout << (char) (stringInput[posToDecree]-1);}
      for (int i = posToDecree+1; i < stringInput.size(); i ++) {
	cout << 9;
      }
      cout << endl;
    }
    
  }   
}
