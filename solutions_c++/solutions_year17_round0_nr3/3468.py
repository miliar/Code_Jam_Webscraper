#include<iostream>
#include<fstream>
using namespace std;

int main() {
  ifstream myInput;
  ofstream myOutput;
  myInput.open("C-small-2-attempt0.in");
  myOutput.open("outputc.txt");
  int T;
  myInput >> T;
  for(int testCase=1; testCase<T+1; testCase++) {
    long long int N;
    long long int K;
    myInput>>N>>K;
    int base = 0;
    long long int maxMax = 1;
    while(K > 1<<base) {
      if(N/2 == (N-1)/2) {
        maxMax += 1<<base;
      }
      K -= 1<<base;
      base++;
      N = N>>1;
    }
    if(K <= maxMax) {
      if(N%2 == 0) {
        myOutput<<"Case #"<<testCase<<": "<<N/2<<" "<<N/2 - 1<<endl;
      } else {
        myOutput<<"Case #"<<testCase<<": "<<N/2<<" "<<N/2<<endl;
      }
    } else {
      N--;
      if(N%2 == 0) {
        myOutput<<"Case #"<<testCase<<": "<<N/2<<" "<<N/2 - 1<<endl;
      } else {
        myOutput<<"Case #"<<testCase<<": "<<N/2<<" "<<N/2<<endl;
      }
    }
  }
}
