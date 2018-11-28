#include <iostream>
#include <vector>
using namespace std;
typedef unsigned long int UL;
vector<int> seperate_into_digits(UL value){
    vector<int> digits ;
    for( ;value > 0 ;value /= 10) digits.push_back(value%10);
    return digits;
}
int main(){
  int T;
  UL N, new_N = 0, divider = 10;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    cout << "Case #" << t << ": ";
    cin >> N;
    vector<int> digits = seperate_into_digits(N);
    for (int i = 0; i < digits.size() - 1; i++) {
      if (digits[i] < digits[i + 1] || digits[i] == 0) {
        for (int j = 0; j <= i; j++)
          digits[j] = 9;
        digits[i + 1] -= 1;
      }
    }
    reverse(digits.begin(), digits.end()) ;
    int i = 0;
    while(digits[i] == 0) i++;
    for (;i < digits.size();i++) {
      cout << digits[i];
    }
    cout << endl;
  }
}
