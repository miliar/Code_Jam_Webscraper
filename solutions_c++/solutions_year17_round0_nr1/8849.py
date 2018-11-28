#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
string s;
int k;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    int t;
    cin>>t;
    int T=t;
    while(t--){
        cin>>s>>k;
        int cnt=0;
        for(int i=0;i<=s.size()-k;i++){
            if(s[i]=='-'){
                cnt++;
                for(int j=i;j<i+k;j++){
                    if(s[j]=='-') s[j]='+';
                    else s[j]='-';
                }
            }
        }
        int flag=0;
        for(int i=0;i<s.size();i++){
            if(s[i]=='-')
                flag=1;
        }
        cout<<"Case #"<<T-t<<": ";
        if(flag) cout<<"IMPOSSIBLE"<<endl;
        else cout<<cnt<<endl;
    }

    return 0;
}
