
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int tc=1; tc<=T; tc++) {
    string num;
    cin >> num;
    if (num[0] == '0') cerr << "Leading zeros!!!" << endl;
    int i=0,j=0,n=(int)num.size();
    while (j<n) {
      if (num[i] > num[j]) break;
      else if (num[i] < num[j]) i=j;
      j++;
    }
    cout << "Case #" << tc << ": ";
    if (j == n) cout << num << endl;
    else {
      num[i] -= 1;
      for (int k=i+1; k<n; k++) {
        num[k] = '9';
      }
      long long ans = stoll(num);
      cout << ans << endl;
    }
  }
}
