#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(void) {
  typedef unsigned long long ll;
  ll t, i, j, k, p, q;
  cin >> t;
  for(i=1; i<=t; i++) {
    string str;
    cin >> str;
    if(str.length()==1) {
      cout << "Case #" << i << ": " << str << endl;
      continue;
    }
    p = str.length();
    for(j=0; j<p-1; j++) {
      if(str[j+1] < str[j]) {
	if(str[j]!='1') {
	  cout << "Case #" << i << ": ";
	  for(q=j; q!=0; q--){
	    if(str[q-1]!=str[j]) break;
	  }
	  for(k=0; k<q; k++) {
	    cout << str[k];
	  }
	  printf("%c", str[q]-1);
	  for(k=q+1; k<p; k++) {
	    cout << '9';
	  }
	  cout << endl;
	}
	else {
	  cout << "Case #" << i << ": ";
	  for(k=0; k<p-1; k++) {
	    cout << '9';
	  }
	  cout << endl;
	}
	break;
      }
      if(j==p-2) {
	cout << "Case #" << i << ": " << str << endl;
      }
    }
  }
}
