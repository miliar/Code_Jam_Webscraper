#include <iostream>  
#include <array>
using namespace std;

int main() {
  int t;
  int n;
  cin >> t; 

  for (int i = 1; i <= t; ++i) {
    cin >> n;
    int tidy = 1;

    for (int j = 1; j <= n;  j++) {
        int number = j;
        int orig = number;

        bool flag = true;
        int max = number % 10;
        do {
            int digit = number % 10;
            
            if (digit <= max) {
                max = digit;
            } else {
                flag = false;
            }
            number /= 10;
        } while (number > 0);
        
        if (flag) {
            tidy = orig;
        }
    }
    
    cout << "Case #" << i << ": " << tidy << endl;
  }
  return 0;
}