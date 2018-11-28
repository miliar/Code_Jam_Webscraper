#include <iostream>
#include <string>

using namespace std;

int main ()
{
  //cerr << "Hello bathroom" << endl;

  int T;
  string grill;
  int f;
  int gz;

  cin >> T;
  for(int casei = 0; casei < T; casei++){
    cin >> grill >> f;
    gz = grill.length();
    //cerr << grill << " of  " << gz << " by  " << f << endl;

    int k, counter = 0;
    bool fail = false;

    k = 0;
    while( k < gz && !fail ){
      if( grill[k] == '-' )
	if ( k <= gz-f ){
	  /* flip pancakes  */
	  for(int j=0; j<f; j++ ){
	    grill[k+j] = (grill[k+j]=='-')? '+' : '-' ;
	  }
	  //cerr << "g= " << grill << endl;
	  counter++;
	}
	else {
	  fail = true;
	}
      
      k++;
    }
    
    
    /* Output Line */
    cout << "Case #" << casei+1 << ": ";
    if (fail) cout << "IMPOSSIBLE" << endl;
    else cout << counter << endl;
  }
}

