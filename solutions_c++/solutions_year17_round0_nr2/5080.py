#include <iostream>
#include <string>

using namespace std;
void main() {
	int t;
	cin >> t;

	for (int i = 0; i < t; ++i) {
    string s; cin >> s;
    int len = s.length();
    int firstOccurence = -1;
    int save = -1;
		for (int c = 0; c < len; c++) {
      int sc = s[c] - '0';
      if(sc > save){
      // that's a new number
          firstOccurence = c;
          save = sc;
      } else if(sc < save){
          int replace = s[firstOccurence] - '0';
          replace--;
          s[firstOccurence] = replace + '0';
          for(int j = firstOccurence+1; j < len; ++j){
              s[j] = '9';
          }
          break;
      }
		}
    if(s[0] == '0' && s.compare("0") != 0){s = s.substr(1);}
                cout << "Case #" << i+1 << ": " << s << endl;
	}
}
