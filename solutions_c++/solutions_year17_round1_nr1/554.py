#include <iostream>

using namespace std;

main() {
  int T;
  cin >> T;
  for (int t=1; t<=T; t++) {
    int R, C;
    cin >> R >> C;
    string x[25];
    for (int i=0; i<R; i++)
      cin >> x[i];
    int first_non_empty = 0;
    
    bool empty = true;
    while (empty) {
      for (int j=0; j<C; j++)
	if (x[first_non_empty][j] != '?')
	  empty = false;
      if (empty) first_non_empty++;
    }

    for (int i=first_non_empty; i< R; i++) {
      int j=0;
      while (j<C && x[i][j] == '?') j++;
      if (j<C) { // x[i][j] first non-empty
	for (int k=0; k<j; k++) x[i][k] = x[i][j];
	for (int k=j+1; k<C; k++)
	  if (x[i][k] == '?') x[i][k] = x[i][k-1];
	
      } else { // row i empty
	x[i] = x[i-1];
      };
    };

    // fill first empty rows
    for (int i=0; i<first_non_empty; i++)
      x[i]=x[first_non_empty];
    
    cout << "Case #" << t << ":" << endl;
    for (int i=0; i<R; i++)
      cout << x[i] << endl;
  }
};
