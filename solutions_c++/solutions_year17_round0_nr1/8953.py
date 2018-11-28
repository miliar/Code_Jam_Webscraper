#include <vector>
#include <string.h>
#include <iostream>
using namespace std;
bool verificar(string s){
  for (int i =0; i< s.size();++i){
    if(s[i]=='-'){
      return false;
    }
  }
  return true;
}
int main(){
  int t;
  cin>>t;
  for(int y=0; y<t;++y){
    string s;
    int k, cont=0, respuesta=0, numeroMenor=0;
    cin>>s;
    cin>>k;
    for (int i=0; i< s.size(); ++i)
      {
        if (s[i]=='+'){
          cont++;
        }else{
          if (i+k<=s.size()){
            for (int j=i;j<i+k;j++){
              if(s[j]=='-'){
                s[j]='+';
              }else{
                s[j]='-';
              }
            }
            respuesta++;
          }
          }

        }
      if(verificar(s))
      cout<<"Case #"<<y+1<<": "<<respuesta<<endl;
      else
      cout<<"Case #"<<y+1<<": IMPOSSIBLE"<<endl;
  }

  return 0;
}
