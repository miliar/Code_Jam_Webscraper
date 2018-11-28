#include<iostream>
#include<string>
using namespace std;
int main() {
  int T;
  int K;
  string S;
  cin>>T;
  char base = '-'+'+';
  for (int t=1;t<=T;t++) {
    cin>>S>>K;
    int sum=0;
    for (int i=0;i<S.length()-K+1;i++){
      if (S[i]=='-') {
	sum++;
	for (int j=0;j<K;j++){
	  S[i+j] = base-S[i+j];
	}
      }
    }
    for (int i=0;i<S.length();i++) {
      if (S[i]=='-') {
	sum = -1;
      }
    }
    cout<<"Case #"<<t<<": ";
    if (sum==-1){
      cout<<"IMPOSSIBLE"<<endl;
    } else {
      cout<<sum<<endl;
    }
  }
}
