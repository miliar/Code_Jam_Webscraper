#include<bits/stdc++.h>
using namespace std;
int n,k;
string s;

char invert(char k){
    if(k=='+') return '-';
    else return '+';
}

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);


    scanf("%d",&n);
    for(int cs=1;cs<=n;cs++){
        cin>>s;
        int ans=0;
        scanf("%d",&k);

        for(int j=0;j<s.size()-k+1;j++){
            if(s[j]=='-'){
                ans++;
                for(int p=j;p<j+k;p++){
                    s[p]=invert(s[p]);
                }
            }
        }

        bool ok=1;
        for(int i=s.size()-k;i<s.size();i++){
            if(s[i]!='+') ok=0;
        }
        printf("Case #%d: ",cs);
        if(ok==0) printf("IMPOSSIBLE");
        else printf("%d",ans);
        printf("\n");
    }
}
