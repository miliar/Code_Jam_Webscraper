#include<iostream>
#include<stdint.h>
#include<map>

using namespace std;

bool tidy_num(uint64_t n){
  int p=9;
  int d;
  while(n>0){
    d=n%10;
    //cout<<"d:"<<d<<" p:"<<p<<endl;
    if(d>p){
      //cout<<"d>p"<<endl;
      return false;
    }
    else{
      // do nothing
      //cout<<"d<=p"<<endl;
    }
    n=n/10;
    p=d;
  }
  return true;
}

int main(){
  int t;
  cin>>t;

  map<uint64_t, int> dp;
  uint64_t max;

  uint64_t n1;
  cin>>n1;

  while(n1>0){
    if(tidy_num(n1)==true){
      cout<<"Case #1: "<<n1<<endl;
      dp[n1]=1;
      max=n1;
      break;
    }
    else{
      n1--;
    }
  }

  for(int i=1;i<t;i++){

    uint64_t n;
    cin>>n;
    if(dp[n]==1){
      cout<<"Case #"<<i+1<<": "<<n<<endl;
    }
    else if(n>max){
      while(n>0){
        if(tidy_num(n)==true){
          cout<<"Case #"<<i+1<<": "<<n<<endl;
          dp[n]=1;
          max=n;
          break;
        }
        else{
          n--;
        }
      }
    }
    else{
      while(n>0){
        if(tidy_num(n)==true){
          cout<<"Case #"<<i+1<<": "<<n<<endl;
          dp[n]=1;
          break;
        }
        else{
          n--;
        }
      }
    }

  }


  return 0;
}
