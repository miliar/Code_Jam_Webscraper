#include <iostream>


using namespace std;


bool checker(long int num){
  int next_digit = num%10;
  num = num/10;
  while (num)
  {
      int digit = num%10;
      if (digit > next_digit)
          return false;
      next_digit = digit;
      num = num/10;
  }

  return true;
}

int main(){

  int tc;
  long int n;

  cin >> tc;

  for(int caseno = 1; caseno <= tc; caseno++){

    cin >> n;

    bool isAns = false;
    for(long int num = n; num >= 1; num--){
      isAns = checker(num);
      if(isAns){
        cout << "Case #" << caseno <<  ": " <<  num << endl;
        break;
      }
    }

  }

}
