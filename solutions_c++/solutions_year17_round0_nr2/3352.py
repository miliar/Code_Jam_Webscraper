#include <bits/stdc++.h>
using namespace std;
int main(){
    //freopen("B-large.in","r",stdin);
    //freopen("B-large-out.txt","w",stdout);
    int T,len,n;
    string s;
    cin>>T;
    for(int ca=1;ca<=T;ca++){
        cin>>s;
        len=s.size();int be=(int)(s[len-1]-'0');
        for(int i=len-2;i>=0;i--){
            int en=(int)(s[i]-'0');
            if(en>be){
                s[i]=(en-1)+'0';
                for(int j=i+1;j<len;j++)s[j]='9';
            }
            be=(int)(s[i]-'0');
        }
        long long ans=0;
        for(int i=0;i<len;i++)ans=ans*10+(long long)(s[i]-'0');
        printf("Case #%d: %I64d\n",ca,ans);
    }
}
