#include<iostream>

using namespace std;

void solveOneProblem(int caseNum){
  cout << "Case #" << caseNum << ": ";

  long N;
  cin >> N;
  long origN = N;
  int dig[20];
  int numDigits = 0;
  while(N > 0){
    for(int i = numDigits; i > 0; i--)
      dig[i] = dig[i-1];
    dig[0] = N%10;
    N /= 10;
    numDigits++;
  }

  int i = 0;
  while(i < numDigits-1 && dig[i] <= dig[i+1])
    i++;
  //cout << origN << ", " << numDigits << ", " << i << endl;

  if(i == numDigits - 1 || origN < 10){
    cout << origN << endl;
    return;
  }

  int old = dig[i];
  while(i > 0 && dig[i-1] == old)
    i--;
  dig[i]--;
  i++;
  while(i < numDigits){
    dig[i] = 9;
    i++;
  }

  bool init0 = true;
  for(int i = 0; i < numDigits; i++){
    if(init0 && dig[i] == 0){
      init0 = false;
      continue;
    }
    cout << dig[i];
  }
  cout << endl;
}

  

int main(){
  int T;
  cin >> T;

  for(int i = 0; i < T; i++)
    solveOneProblem(i+1);
}
