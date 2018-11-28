#include<iostream>
#include<string>
using namespace std;
int main(){
  int t;
  cin>>t;
  for(int i=1;i<=t;i++){
    string s;
    int k;
    cin>>s>>k;
    int n=s.length();
    int a[n];
    for(int j=0;j<n;j++){
      if(s.at(j)=='+'){
        a[j]=1;
      }
      else{
        a[j]=0;
      }
    }
    int count=0;
    for(int j=0;j<n;j++){
      if((a[j]==0)&&((j+k)<=n)){

        count++;
        for(int l=j;l<j+k;l++){

          if(a[l]==0){
            a[l]=1;
          }
          else{
            a[l]=0;
          }
        }
      }
    }
    int flag=1;

    //cout<<endl;
    for(int j=n-1;j>=n-k;j--){
      if(a[j]==0){
        cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
        flag=0;
        break;
      }
    }
    if(flag==1){
      cout<<"Case #"<<i<<": "<<count<<endl;
    }
  }
}
