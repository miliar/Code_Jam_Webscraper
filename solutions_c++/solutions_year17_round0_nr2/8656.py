#include <iostream>
#include<ctype.h>

using namespace std;

int main() {
  int cases;
  cin >> cases;

  for (int c = 0; c < cases; ++c) {
    string num;
    cin >> num;
    int dupindex = -1;
    int switchindex = -1;
    int len = num.length();

    for (int i = 0; i < len - 1; ++i) {
      int cur = num.at(i) - '0';
      int nxt = num.at(i+1) - '0';
      if (cur == nxt) {
	if (dupindex == -1) {
	  dupindex = i;
	}
      }      
      else if(cur > nxt) {
	switchindex = i;
	break;
      } else {
	dupindex = -1;
      }
    }
    if (switchindex > -1) {
      if (dupindex > -1) {
	switchindex = dupindex;
      }
      for (int j = switchindex + 1; j < len; ++j) {
	num[j] = '9';
      }
      if (switchindex == 0 && num[0] == '1') {
	  num = num.substr(1);
      } else {
	num[switchindex] = num[switchindex] - 1;
      }
    }
    cout<<"Case #"<<c+1<<": "<<num<<endl;
  }
  return 0;
}
