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
    int Ac, Aj;
    cin >> Ac >> Aj;
    
    vector<int> C(100), D(100), J(100), K(100);
    for(int j=0; j<Ac; j++){
      cin >> C[j] >> D[j];
    }
    for(int j=0; j<Aj; j++){
      cin >> J[j] >> K[j];
    }
    if(Ac==2 && C[1] < C[0]){
      swap(C[0], C[1]);
      swap(D[0], D[1]);      
    }
    if(Aj==2 && J[1] < J[0]){
      swap(J[0], J[1]);
      swap(K[0], K[1]);            
    }

    if(Ac==0){
      if(Aj==1){
	cout << "Case #" << i+1 << ": " << 2 << endl;
	continue;
      }
      else{
	if(K[1] - J[0] <= 720 || K[0]+1440-J[1] <= 720){
	  cout << "Case #" << i+1 << ": " << 2 << endl;
	  continue;
	}
	else{
	  cout << "Case #" << i+1 << ": " << 4 << endl;
	  continue;
	}
      }
    }
    else if(Aj==0){
      if(Ac==1){
	cout << "Case #" << i+1 << ": " << 2 << endl;
	continue;
      }
      else{
	if(D[1] - C[0] <= 720 || D[0]+1440-C[1] <= 720){
	  cout << "Case #" << i+1 << ": " << 2 << endl;
	  continue;
	}
	else{
	  cout << "Case #" << i+1 << ": " << 4 << endl;
	  continue;
	}
      }
    }
    else{
      cout << "Case #" << i+1 << ": " << 2 << endl;
      continue;      
    }

  }

  return 0;
}


