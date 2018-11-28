#include <iostream>
using namespace std;

int main(){
      string str;
      int t;
      cin>>t;
      for(int w=1;w<=t;w++){
            cin>>str;
            int flag = 0;
            int i = 0;
            while(i<str.length()-1){
                  //cout<<str[i]<<endl;
                  flag = 0;
                  if(str[i]>str[i+1]){
                        for(int k = i+1;k<str.length();k++){
                              str[k] = '9';
                        }
                        str[i] = str[i] - 1;
                        flag = 1;
                        //break;
                  }
                  if(flag==1){
                        i--;
                  }else{
                        i++;
                  }

            }
            str.erase(0,str.find_first_not_of('0'));
            //cout<<str.length()<<endl;
            cout<<"Case #"<<w<<": "<<str<<endl;
            //cout<<str<<endl;
      }
}
