#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int n;
string s;
ll val;
ll now;

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);


    scanf("%d",&n);
    for(int cs=1;cs<=n;cs++){
        cin>>s;
        bool ok=1;
        int indx=-1;
        val=0;
        for(int i=1;s[i];i++){
            if(s[i]<s[i-1]) {ok=0; indx=i; break;}
        }

        if(!ok){
            s[indx-1]--;
            for(int i=indx;s[i];i++) s[i]='9';

            ok=1;
            val=0;
            for(int i=1;s[i];i++){
                if(s[i]<s[i-1]) ok=0;
            }
            if(!ok){
                s[0]--;
                for(int i=1;s[i];i++) s[i]='9';
            }
        }
        for(int i=0;s[i];i++) val=val*10+s[i]-'0';
        printf("Case #%d: %lld\n",cs,val);
    }
}
