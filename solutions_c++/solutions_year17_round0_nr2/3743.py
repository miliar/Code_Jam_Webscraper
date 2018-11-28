#include <iostream>
#include <string>
using namespace std;
string s;

void check(int a) {
  if(s[a] < s[a-1]) {
    for(int m=a; m<s.size(); m++)
      s[m] = '9';
    s[a-1]--;
  }
}

int main() {
  int t;
  //u_int64_t k, n;
  cin >> t;
  for (int i = 1; i <= t; i++) {
    cin >> s;
    int size = s.size();
    for(int j = size -1; j > 0; j--) {
      check(j);
    }
    s.erase(0, s.find_first_not_of('0'));
    cout << "Case #" << i << ": " << s << endl; 
  }
  return 0;
}