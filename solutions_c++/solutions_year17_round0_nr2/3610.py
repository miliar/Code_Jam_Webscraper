#include<iostream>
#include<string>
using namespace std;
int main() {
  int T;
  long long N;
  cin>>T;
  for (int t=1;t<=T;t++) {
    cin>>N;
    long long fact = 10;
    while (fact <= N) {
      if (N%fact < (N%(fact*10))/10) {
	N /=fact;
	N *=fact;
	N--;
      }
      fact*=10;
    }
    cout<<"Case #"<<t<<": "<<N<<endl;
  }
}
