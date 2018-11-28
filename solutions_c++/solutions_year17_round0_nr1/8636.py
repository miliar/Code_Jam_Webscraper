#include <bits/stdc++.h>

using namespace std;

string s,ss;

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out","w",stdout);
    int t;

    scanf("%d", &t);
    for(int cs=1; cs<=t; cs++){
        int k;
        cin>>s>>k;
        ss=s;
        int mn=0;
        for(int i=0; i<s.size() && mn<100000000; i++){
            if(s[i]=='-'){
                    if(i>s.size()-k){
                        mn=100000000;
                        break;
                    }
                    mn++;
                for(int j=i; j-i+1<=k; j++){
                    if(s[j]=='-')s[j]=='+';
                    else s[j]='-';
                }

            }
        }
        int mnn=0;
        for(int i=ss.size()-1; i>=0 && mnn<100000000;  i--){
            if(ss[i]=='-'){
                mnn++;
                if(i<k-1){
                    mnn=100000000;
                    break;
                }
                for(int j=i; i-j+1<=k; j--){
                    if(ss[j]=='-')ss[j]='+';
                    else ss[j]='-';

                }
            }

        }
        int ans=min(mnn,mn);
        if(ans==100000000)printf("Case #%d: IMPOSSIBLE\n", cs);
        else printf("Case #%d: %d\n", cs, ans);
    }

}
