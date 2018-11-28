#include "bits/stdc++.h"
using namespace std;
typedef long long int int64;

char no[30];
int64 _no ;
int64 T;

void save(){
  memset(no , 0 , sizeof no);
  for(int64 i=0 ; _no ; i++){
    no[i] = _no%10;
    _no/=10;
  }
  return;
}

void presult(){
  int64 i = 30;
  while(!no[i--]);
  while(i>=0&&no[i]>=no[i+1]) i-- ;
  while(i>=0&&no[i]<no[i+1]){
    i++; no[i]--;
  }
  i--;
  for(;i>=0;i--) no[i] = 9;
  int64 ans = 0 ;
  int64 j=0;
  while( no[j++] );
  for(j--; j>=0 ; j-- )
  ans = ans*10 + no[j] ;
  cout<<ans<<endl;
}

int main(){
//  freopen("input.txt" , "r" , stdin);
//  freopen("output1.txt" , "w" , stdout) ;
  cin>>T;
  for(int64 i=1; i<=T ; i++){
    cout<<"Case #"<<i<<": ";
    cin>>_no;
    save();
    presult();
  }

}
