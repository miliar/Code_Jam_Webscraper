#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  int T,K;
  string S;
  bool ispossible;
  cin>>T;
  for (int i=1;i<=T;i++) {
    cin>>S>>K;
    int l=S.length();
    vector<int> subfine(l+1); //dynamic programming recording the number of flips for current position;
    subfine[0]=0; //starting from 0;
    for (int j=1;j<=l-K+1;j++) { //last possible position of flipping is l-K+1;
      if (S[j-1]=='+') subfine[j]=subfine[j-1];
      else { //when equal to '-', flip
        subfine[j]=subfine[j-1]+1;
        for (int k=0;k<K;k++) {
         S[j+k-1]=((S[j+k-1]=='+')?'-':'+'); //flip sign
        }
      }
    }
    ispossible=true;
    for (int j=1;j<K;j++) { //check for remaining elements
      if (S[l-K+j]=='-') {
        cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
        ispossible=false;
        break;
      }
      subfine[l-K+j+1]=subfine[l-K+j];
    }
    if (ispossible) {
      cout<<"Case #"<<i<<": "<<subfine[l]<<endl;
    }
    subfine.clear(); 
  }
  return 0;
}
