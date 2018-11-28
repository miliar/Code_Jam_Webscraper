//
//  1.cpp
//  Hello World
//
//  Created by Sri Krishna Vijayapuri on 4/8/17.
//  Copyright © 2017 test. All rights reserved.
//

#include <iostream>
#include <string>
#include <climits>
using namespace std;

int main(){
  int t,k,n,cnt=1;
  cin>>t;
  cin.clear();
  cin.ignore(numeric_limits<streamsize>::max(),'\n');
  while(t--){
    n=0;k=0;
    string str;
    getline(cin,str,' ');
    cin>>k;
    cin.clear();
    cin.ignore(numeric_limits<streamsize>::max(),'\n');
    int i;
    for(i=0;i<(str.length()-k);i++){
      if(str[i] != '+'){
        n++;
        for(int j=0;j<k;j++){
          if(str[j+i]=='+'){
            str[j+i]='-';
          }else{
            str[j+i]='+';
          }
        }
      }
    }
    while(i<(str.length()-1)){
      if(str[i] != str[i+1]){
        break;
      }
      i++;
    }
    if(i==(str.length()-1)){
      if(str[i]=='-'){
        n++;
      }
      cout<<"Case #"<<cnt<<": "<<n<<endl;
    }else{
      cout<<"Case #"<<cnt<<": IMPOSSIBLE"<<endl;
    }
    cnt++;
  }
  return 0;
}
