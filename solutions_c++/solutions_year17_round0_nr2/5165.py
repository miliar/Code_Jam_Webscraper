#include<iostream>
#include<vector>

using namespace std;

int main() {
  int T;
  long long int N;
  cin>>T;
  for (int i=1;i<=T;i++) {
    cin>>N;
    long long int minimum=9; //minimum digit found in front for last X digits;
    long long int remain=N, mod=0, digit=1, result=0; //calculate the module and remain for each digit after divide by 10, digit for the digit on certain number
    while (remain>0) {
      mod=remain%10;
      remain=remain/10;
      if (minimum>=mod) {
        minimum=mod;
        result+=mod*digit;
      }
      else {
        result=mod*digit-1; //reset last X digits to 9
        minimum=mod-1;
      }
      digit*=10; //increase digit
    }
    cout<<"Case #"<<i<<": "<<result<<endl;
  }
  return 0;
}
