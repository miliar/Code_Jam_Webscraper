#include<bits/stdc++.h>
using namespace std;
const int N=1020;
char s[N];
long long ans;

int main(){
    int _,k;
    freopen("A-large.in","r",stdin);
    freopen("1000.out","w",stdout);
    scanf("%d",&_);
    for(int Case=1;Case<=_;Case++){
        scanf("%s%d",s,&k);
        int len=strlen(s);
        int ans=0,Flag=0;
        for(int i=0;i<len;i++){
            if(s[i]=='-'&&i+k-1<len){
                ans++;
                for(int j=i;j<=i+k-1;j++){
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
            }
            else if(s[i]=='-')
                Flag=1;
        }
        printf("Case #%d: ",Case);
        if(Flag==1)
            puts("IMPOSSIBLE");
        else
            printf("%d\n",ans);
    }
    return 0;
}
