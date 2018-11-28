#include <iostream>
using namespace std;
bool is_tidy(int n) {
    while(n) if (n%10 < (n/=10)%10) return 0; return 1;
}
int main() {
  int i, n, t;
  cin >> t;
  for (i=1;i<=t;i++) {
    cin >> n;
    while (!is_tidy(n--));
    cout << "Case #"<< i << ": " << n+1 << '\n';
  }
  return 0;
}
