#include<bits/stdc++.h>
using namespace std;
string s;
int main(void){
    //freopen("123.in","r",stdin);
    //freopen("out.out","w",stdout);
    long long i,j,n,m,T,A,B,ca=1,t;
    cin>>T;
    while(T--){
        cin>>s;
        n=s.size();
        while(true){
            m=1;
            for(i=0;i<n-1;i++){
                if(s[i]>s[i+1]){
                    m=0;
                    s[i]=s[i]-1;
                    for(j=i+1;j<n;j++){
                        s[j]='9';
                    }
                    break;
                }
            }
            if(m==1) break;
        }
        A=0;
        for(i=0;i<n;i++){
           A*=10;
           A+=s[i]-'0';
        }
        printf("Case #%lld: %lld\n",ca++,A);
    }
}
