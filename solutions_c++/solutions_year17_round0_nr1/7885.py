#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int tt;
    cin>>tt;
    for(int qq=1;qq<=tt;qq++){
        string s;
        int k, flip=0, flag=0;
        cin>>s>>k;
        int len = s.length();
        cout<<"Case #"<<qq<<": ";
        for(int i = 0; i<len;i++){
          if(s[i]=='+')
            continue;
          if(i+k > len){
            flag =1;
            break;
          }
          for(int j=i; j<i+k; j++){
            s[j] = s[j]=='-' ? '+' : '-';
          }
          flip++;
          //cout<<s<<endl;
        }
        if (flag==1)
          cout<<"IMPOSSIBLE"<<endl;
        else
          cout<<flip<<endl;
    }
    return 0;
}
