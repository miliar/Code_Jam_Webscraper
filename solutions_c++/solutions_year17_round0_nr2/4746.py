#include<iostream>
using namespace std;
int main(){
  int t;
  cin>>t;
  for(int i=1;i<=t;i++){
    long long int x,y;
    cin>>x;
    y=x;
    int digit=0;
    while(x){
      digit++;
      x/=10;
    }
    //cout<<digit<<endl;
    int arr[18];
    for(int j=0;j<digit;j++){
      arr[j]=y%10;
      y/=10;
      //cout<<arr[j];
    }
    //cout<<endl;
    int rev=digit-1;
    int a[digit];
    for(int j=0;j<digit;j++){
      a[j]=arr[rev];
      rev--;
      //cout<<a[j];
    }
    //cout<<endl;
    bool flag=true;
    while(flag){
    if(digit==1){
      //cout<<a[0]<<endl;
      flag=false;
    }
    else{
      for(int j=1;j<digit;j++){
        flag=false;
        if(a[j]<a[j-1]){
          flag=true;
          a[j-1]-=1;
          for(int k=j;k<digit;k++){
            a[k]=9;
          }
          break;
        }
      }

    }
    //cout<<endl;
  }
  for(int j=0;j<digit;j++){
    while(a[j]==0){
      a[j]=a[j+1];
      digit--;
    }
  }
  cout<<"Case #"<<i<<": ";
  for(int j=0;j<digit;j++){
    cout<<a[j];
  }
  cout<<endl;
}

}
