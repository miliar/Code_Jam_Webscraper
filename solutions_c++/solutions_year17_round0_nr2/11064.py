#include <iostream>
using namespace std;

int main(){
  int abc;
  cin >> abc;
  int cba = 0;
  int arr[abc];
  for (int i = 0; i < abc; i++) {
    bool run = true;
    int x = 1;
    int number;
    int digit;
    cin >> number;
    int backup = number;
    while(run == true){
      int numarr[3];
      int timer = 0;
      while (number != 0 && timer < 3){
        digit = number%10;
        number /= 10;
        numarr[timer] = digit;
        timer++;
      }
      number = backup;
      if(number == 1000 && number != 100 && number > 111){
        arr[0 + cba] = 999;
        //cout << 999 << endl;
        cba++;
        run = false;
        break;
      }
      if(numarr[2] <= numarr[1] && numarr[1] <= numarr[0] && number >= 111 && number < 1000 && number != 100 || (number > 111 && number < 99)){
        arr[0+cba]=(numarr[2]*100) + (numarr[1]*10) + numarr[0];
        //cout << numarr[2] << numarr[1] << numarr[0] << endl;
        cba++;
        run = false;
        break;
      }
      if(numarr[1] <= numarr[0] && number < 111 && number > 9  && number != 100 && number < 99){
        arr[0+cba]=(numarr[1]*10) + numarr[0];
        //cout << numarr[1] << numarr[0] << endl;
        cba++;
        run = false;
        break;
      }
      if(number == 100 || (number < 111 && number > 99)){
        arr[0 + cba] = 99;
        //cout << 999 << endl;
        cba++;
        run = false;
        break;
      }
      if(number == 99){
        arr[0 + cba] = 99;
        //cout << 999 << endl;
        cba++;
        run = false;
        break;
      }
      if(number < 10 && number != 100 && number < 99){
        arr[0+cba]=number;
        //cout << number << endl;
        cba++;
        run = false;
        break;
      }
      else{
        number = number - x;
        x++;
      }
    }
  }
  int ujn = 0;
  for (int l = 0; l != abc; l++) {
    cout << "Case #" << l+1 << ": " << arr[ujn];
    ujn++;
    if(l != abc-1){
      cout << endl;
    }
  }
  return 0;
}
