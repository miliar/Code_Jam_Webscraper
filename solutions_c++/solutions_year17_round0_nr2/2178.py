#include<bits/stdc++.h>
using namespace std;

int n,T,cs;
string s;

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.ou","w",stdout);
    scanf("%d",&T);
    while(T--){
        cin>>s;
        n=s.length();
        for(int i=0; i<n; ++i){
            if(i+1<n&&s[i+1]<s[i]){
                while(i>0&&s[i]==s[i-1])--i;
                s[i]=s[i]-1;
                for(int j=i+1; j<n; ++j)s[j]='9';
                break;
            }
        }
        if(s[0]=='0')s=s.substr(1,n-1);
        printf("Case #%d: ",++cs);
        cout<<s<<'\n';
    }
}
