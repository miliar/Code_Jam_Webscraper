// Author: Krzysztof Bochenek
// Email:  kpbochenek@gmail.com
// --------------------------------
#include <stdio.h>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <math.h>
#include <algorithm>
#include <string>
#include <iostream>

typedef long long int ll;
typedef unsigned long long ull;

using namespace std;

int main() {

  int T;
  int N, R, O, Y, G, B, V;
  
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> N >> R >> O >> Y >> G >> B >> V;

    int half = N / 2;
    if (R > half || Y > half  || B > half) {
      cout << "Case #" << t+1 << ": IMPOSSIBLE" << endl;
    } else {
      int A[3] = {R, Y, B};
      char C[3] = {'R', 'Y', 'B'};

      if (A[1] > A[0]) {
	swap(A[1], A[0]);
	swap(C[1], C[0]);
      }
      if (A[2] > A[0]) {
	swap(A[2], A[0]);
	swap(C[2], C[0]);
	
      }
      
      cout << "Case #" << t+1 << ": ";
      for (int i=0; i<A[0]; ++i) {
	cout << C[0];
	if (A[1] > 0) {
	  cout << C[1];
	  A[1]--;
	}
	if (A[2] > 0) {
	  if (i + A[2] == A[0]) {
	    cout << C[2];
	    A[2]--;
	  }
	}
      }
      cout << endl;
    }
  }

  return 0;
}
