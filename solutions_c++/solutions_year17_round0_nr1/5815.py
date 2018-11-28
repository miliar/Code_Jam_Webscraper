#include <iostream>
#include <vector>
#include <string>
using namespace std;
bool l[1001];

void flip(int i) {
  if(l[i]) l[i] = false;
  else l[i] = true;
}

int main(void) {
  int k, s, t, min;
  cin >> t;
  for(int i=1; i<=t; i++) {
    string str;
    cin >> str;
    min = 0;
    s = str.length();
    cin >> k;
    for(int j=0; j<s; j++) {
      if(str[j]=='+') l[j] = true;
      else l[j] = false;
    }
    for(int j=0; j<=s-k; j++) {
      if(l[j] == false) {
	for(int p=0; p<k; p++) {
	  flip(j+p);
	}
	min ++;
      }
    }
    int p=s-k;
    for(; p<s; p++) {
      if(l[p] == false) {
	break;
      }
    }
    //    cout << min << endl;
    cout << "Case #" << i << ": ";
    if(p!=s) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << min << endl;
    }
  }
  return 0;
}
