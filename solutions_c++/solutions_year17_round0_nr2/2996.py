#include <iostream>

using namespace std;

long long findTidy(long long N) {
  int digits[20];
  int num=0;
  while (N>0) {
    digits[num]=N%10;
    N/=10;
    num++;
  }
  digits[num]=0;
  long long S=0;
  for(int i=num-1; i>=0; i--) {
    if (digits[i+1]>digits[i]) {
      digits[i+1]--;
      for(int j=0; j<=i; j++) {
	digits[j]=9;
      }
      S/=10;
      i+=2;
    }
    else {
      S*=10;
      S+=digits[i];
    }
  }
    
  
  

  return S;
}



int main() {
  int T;
  cin >> T;

  for(int t=1; t<=T; t++) {
    cout << "Case #" << t << ": ";
    long long n;
    cin >> n;
    cout << findTidy(n) << endl;
  }
  return 0;
}
