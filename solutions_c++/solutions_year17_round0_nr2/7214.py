#include <iostream>
#include <string>

using namespace std;

int main() {
  int T;
  cin>>T;

  for (int k = 0; k < T; k++) {
    string num;
    cin>>num;
    int sz = num.size();
    int last = -1;
    string ans = num;
    for (int i = sz - 2; i >= 0; i--) {
      if (num[i] > num[i + 1]) {
        last = i;
        num[i]--;
      }
    }
    if (last != -1) {
      string n9 = "";
      for (int i = 0; i < (sz - last - 1); i++) {
        n9 += "9";
      }
      if (last > 0 || (last == 0 && num[0] != '0')) {
        ans = num.substr(0, last + 1) + n9;
      } else {
        ans = n9;
      }
    }
    cout << "Case #"<<(k+1)<<": "<<ans<<endl;
  }

}
