#include <iostream>
#include <string>
using namespace std;
int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    int n=0,k,flag=0;
    string s;
    cin>>s>>k;
    int len;
    len=s.length();
    for(int j=0;j<len;j++){
        if(s[j]=='-'){
            for(int a=0;a<k;a++){
                    if(j+a>len-1){
                        flag=1;
                        break;
                    }
                    if(s[j+a]=='+') s[j+a]='-';
                    else s[j+a]='+';
                 //   cout<<j<<" : "<<s<<endl;
            }
            n++;
        }
        if(flag==1){
            break;
        }
    }
        if(flag==1){
            cout << "Case #" << i << ": "<<"IMPOSSIBLE"<<endl;
            continue;
        }
    cout << "Case #" << i << ": "<< n<<endl;
  }
  return 0;
}
