#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;

int main(){

  int t;
  cin >> t;

  for(int T=1;T<=t;T++){
    string N;
    bool check = true;
    int cnt =-1 ;
    cin >> N;

    int len = N.size();

    if(len == 1){
      cout << "Case #" << T << ": " << N << endl;
      continue;
    }
    for(int i=0 ;i<len-1;i++){
      if(N[i]>N[i+1]){
        N[i] = N[i] - 1;
        N[i+1] = '9';
        cnt = i;
        break;
      }
    }
    if(cnt!=-1){
      for(int i=cnt+1 ; i<len ;i++)
        N[i] = '9';
    }
    for(int i=0 ; i<len-1;i++){
      if(N[i]>N[i+1]){
        check = false;
        break;
      }
    }
    if(!check){
      for(int j=0 ; j<len-1;j++)
        for(int i = 0 ;i<len -1;i++){
          if(N[i]>N[i+1]){
            N[i] = N[i]-1;
            N[i+1] = '9';
          }
        }
    }

    cout << "Case #" << T << ": " ;
    for(int i=0 ;i<len;i++)
      if(N[i]-'0')
        cout << N[i];
    cout << endl;

  }


  return 0;
}
