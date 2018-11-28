#include <bits/stdc++.h>
using namespace std;

int main(){
  int n;
  cin>>n;
  for(int i=0;i<n;i++){
    string str;
    int a,len;
    cin>>str;
    len = str.length();
    bool change=false;
    if(len>1){
      /*if(str[len-1]!='9'){
        str[len-1]='9';
        change=true;
      }
      int shift=2;
      while(change){
        change = false;
        if(len-shift<0)break;
        if(str[len-shift]=='0'){
          str[len-shift]='9';
          change=true;
          shift++;
        }
        else 
          str[len-shift]--;
      }*/
      do{
        change = false;
        for(int j=0;j<len-1;j++){
          if(str[j] > str[j+1]){
            // special case first char is 0
            if(str[j]=='0'){
              int shift=0;
              do{
                change = false;
                if(j-shift<0)break;
                if(str[j-shift]=='0'){
                  str[j-shift]='9';
                  change = true;
                  shift++;
                }
                else str[j-shift]--;
              }while(change);
            }
            else 
              str[j]--;
            
            for(int k=j+1;k<len;k++)
              str[k]='9';
            
            change = true;
          }
        }
      }while(change);
    }
    cout<<"Case #"<<i+1<<": ";
    int index=0;
    while(str[index]=='0')index++;
    for(int j=index;j<len;j++)
      cout<<str[j];
    cout<<endl;
  }
  return 0;
}