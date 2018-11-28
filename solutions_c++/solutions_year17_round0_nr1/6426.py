#include <iostream>
#include <string>
using namespace std;

int main(){
      string str;
      int t,k;
      cin>>t;
      int ll = 0;
      for(int i=1;i<=t;i++){
            cin>>str;
            cin>>k;
            ll = 0;
            int j = 0;
            int flag = 0;
            while(j<str.length()-(k-1)){
                  if(str[j]=='-'){
                        for(int u=0;u<k;u++){
                              if(str[j+u]=='+'){
                                    str[j+u]='-';
                              }else if(str[j+u]=='-'){
                                    str[j+u]='+';
                              }
                        }
                        ll++;
                  }
                  j++;
            }
            //cout<<str<<endl;
            for(int o=str.length()-k;o<str.length();o++){
                  if(str[o]=='-'){
                        flag = 1;
                        break;
                  }
            }
            if(flag==1){
                  cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
            }else{
                  cout<<"Case #"<<i<<": "<<ll<<endl;
            }
      }
}
