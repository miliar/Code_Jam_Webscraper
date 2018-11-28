//
//  1.cpp
//  Hello World
//
//  Created by Sri Krishna Vijayapuri on 4/7/17.
//  Copyright © 2017 test. All rights reserved.
//

#include <iostream>
#include <string>
#include <sstream>
#include <climits>
using namespace std;

int main(){
  int t,cnt=1,d=0,i=0,j=0;
  stringstream ss;
  cin>>t;
  cin.clear();
  cin.ignore(numeric_limits<streamsize>::max(),'\n');
  
  while(t--){
    //str="";out="";
    string str,out;
    getline(cin,str);
    d=str[0]-'0';
    if(str.length()==1){
      cout<<"Case #"<<cnt++<<": "<<d<<endl;
    }else{
      i=0;j=0;
      while((i<str.length()-1) && ((str[i]-'0')<=(str[i+1]-'0'))){
        if((str[i]-'0')<(str[i+1]-'0')){
          j++;
        }
        i++;
      }
      if(i<(str.length()-1)){
      if(j==0){
        if(str[j] != '1'){
          ss.clear();ss.str("");
          ss<<str[j]-'1';
          out+=ss.str();
        }else{
          //don't add anything since it is '0';
        }
        i=1;
      }else{
        out+=str.substr(0,i);
        ss.clear();ss.str("");
        ss<<str[i]-'1';
        out+=ss.str();
        i++;
      }
      while(i<str.length()){
        out+='9';i++;
      }
      }else{
        out=str;
      }
      cout<<"Case #"<<cnt++<<": "<<out<<endl;
    }
  }
  return 0;
}
