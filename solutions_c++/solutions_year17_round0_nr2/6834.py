#include <iostream>
#include <cmath>
using namespace std;

int main () {
  int t = 0;
  cin >> t;
  for(int i = 0; i < t; i++) {
    long long int num = 0;
    cin >> num;
    int bits = log10(num) + 1;

    if (bits != 1) {

      //put num into bitsArr
      int* bitsArr = new int[bits];
      for(int j = 0; j < bits ; j++) {
        if(j == 0) {
          bitsArr[bits-1-j] = num % 10;
        }
        else {
          long long int power10 = pow(10, j);
          bitsArr[bits-1-j] = (num / power10) % 10;
        }
      }
      //printing
      // for(int j = 0; j < bits; j++ ){
      //   cout << bitsArr[j] << " ";
      // }
      // cout << endl;

      bool tidy = false;
      while(!tidy) {
        int breakingPt = -1;

        //determine whether it's tidy
        for(int j = bits-1; j > 0; j--) {
          if(bitsArr[j] >= bitsArr[j-1]) {
            tidy = true;
          } 
          else {
            tidy = false;
            breakingPt = j;
            break;
          }
        }

        if(!tidy && breakingPt >= 0) {
          bitsArr[breakingPt-1] -= 1;
          for(int k = breakingPt; k < bits ; k++) {
            bitsArr[k] = 9;
          }
          // for(int j = 0; j < bits; j++ ){
          //   cout << bitsArr[j] << " ";
          // }
          // cout << endl;
        }
        else {
          long long int answer = 0;
          for(int k = 0; k < bits-1; k++ ){
            answer = (answer + bitsArr[k]) * 10;
          }
          answer += bitsArr[bits-1];
          cout << "Case #" << i+1 << ": " << answer << endl;
          break;
        }


        // tidy = true;
      }
    }
    else {
      cout << "Case #" << i+1 << ": " << num << endl;
    }
  }
  return 0;
}