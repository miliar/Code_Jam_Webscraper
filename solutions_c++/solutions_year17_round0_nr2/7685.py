#include <iostream>
#include <string>

using namespace std;

int main() {
  int t;
  cin >> t;
  for (int test=1;test<=t;test++) {
    cout << "Case #" << test << ": ";
    string n;
    cin >> n;
    for (int i=n.length()-2;i>=0;i--)
      if(n[i]>n[i+1]) {
        n[i] = n[i]-1;
        for (int j=i+1;j<n.length();j++)
          n[j] = '9';
      }
    if (n.length()>1 && n[0]=='0') n = n.substr(1);
    cout << n << endl;
  }
  return 0;
}