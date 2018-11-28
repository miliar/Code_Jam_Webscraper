#include<iostream>
#include<fstream>
using namespace std;

int main() {
  ifstream myInput;
  ofstream myOutput;
  myInput.open("B-large.in");
  myOutput.open("outputb.txt");
  int T;
  myInput >> T;
  for(int testCase=1; testCase<T+1; testCase++) {
    long long int N;
    int lastUpdate = 0;
    int cnt =0;
    myInput>>N;
    long long int aux = N;
    if (N<10) {
      myOutput<<"Case #"<<testCase<<": "<<N<<endl;
    } else {
      string ans = "";
      myOutput<<"Case #"<<testCase<<": ";
      while(aux>=10) {
        cnt++;
        if(aux%10 < (aux/10)%10) {
          lastUpdate =cnt;
          aux-=10;
        }
        aux/=10;
      }
      for(int i = 0; i<lastUpdate; i++) {
        ans =  to_string(9) + ans;
        N/=10;
      }
      if(lastUpdate!=0) {
        N--;
        if(N>0) {
          ans = to_string(N%10) + ans;
          N/=10;
        }
      }
      while(N>0) {
        ans = to_string(N%10) + ans;
        N/=10;
      }
      myOutput<<ans<<endl;
    }
  }
}
