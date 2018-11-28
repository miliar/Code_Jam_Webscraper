#include <iostream>
using namespace std;

bool lSorted (int a) {
  int n = a;
  int next_digit = n%10;
  n /= 10;
  while (n) {
    int currdigit = n%10;
    if (currdigit > next_digit) {
      return false;
    }
    n /= 10;
    next_digit = currdigit;
  }
  return true;

}

int main()  {
  int t;
  cin >> t;
  int arr[100];
  for (int i = 1; i <= t; i++)
    cin >> arr[i];
  for (int i = 1; i <= t; i++)  {
    for (int x = arr[i]; x >= 0; x--) {
      if (lSorted(x) == true) {
        cout << "Case #" << i << ": " << x << endl;
        break;
      }
    }
  }
  return 0;
}
