#include <iostream>
#include <string>
using namespace std;
void print(int * counters,int ndigits){
  for(int m=0;m<ndigits;m++){
    cout<<counters[m];
  }
  cout<<endl;
}
bool sorted(int* counters,int ndigits){
  for(int m=0;m<ndigits-1;m++){
    if(counters[m]>counters[m+1]){
      return false;
    }
  }
  return true;
}
int main() {
  int t, K;
  string S;
  cin >> t;
  int* counters;
  for (int i = 1; i <= t; ++i) {
    cin >> S;
    int ndigits=S.size();
    counters=new int[ndigits];
    for(int j=0;j<ndigits;j++){
      counters[j]=S[j]-'0';
    }

    int j=ndigits-1;
    while(!sorted(counters,ndigits)){ 
      //Reducing numbers below me
      for(int k=j-1;k>=0;k--){
        if(counters[k]==0){
          counters[k]=9;
        }
        else{
          if(k==0 || counters[k]>=counters[k-1]){
            counters[k]--;
            //Reset higher numbers
            for(int m=k+1;m<ndigits;m++){
              counters[m]=9;
            }
            break;
          }
        }
      }
    }

    string result="";
    for(int j=0;j<ndigits;j++){
      if(result=="" && counters[j]==0){
        continue;
      }
      result+=('0'+counters[j]);
    }

    if(result==""){
      result="0";
    }
  	cout << "Case #" << i << ": " << result << endl;
  }
  return 0;
}