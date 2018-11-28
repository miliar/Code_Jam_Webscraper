#include <cstring>
#include <iostream>
using namespace std;

int main() {
  int nex;
  string stringPlusMinus;
  int sizePale;
  bool nonSol;
  int howMany = 0;
  
  cin >> nex;

  for(int indEx = 1; indEx <= nex; indEx++) {

     howMany = 0;
    cin >> stringPlusMinus;
    cin >> sizePale;
    cerr << stringPlusMinus << " " <<  stringPlusMinus.size() << " " << sizePale << endl;
    for(int i = 0; i <= stringPlusMinus.size()-sizePale;i++) {
      if(stringPlusMinus[i] == '-'){
	for(int j = i; j < i + sizePale; j++) {
	   if(stringPlusMinus[j] == '+'){
	     stringPlusMinus[j] = '-';
	   } else {
	     stringPlusMinus[j] = '+';
	   }
	}
	howMany++;
	cerr << stringPlusMinus << " " <<  howMany << endl;
      }
    }

    nonSol = false;
    for(int i = stringPlusMinus.size()-sizePale+1; i < stringPlusMinus.size();i++) {
      if(stringPlusMinus[i] == '-'){
	nonSol = true;
      }
    }
    
    if(nonSol) {
      cout << "Case #" << indEx << ": IMPOSSIBLE" << endl;
    } else {
      cout << "Case #" << indEx << ": " << howMany << endl;
    }
  }
}
