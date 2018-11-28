#include<bits/stdc++.h>
using namespace std;
const int maxn=1e3;

char s[maxn+5];
int k;

char flip(char c){
    if(c=='+')return '-';
    return '+';
}

int work(){
    int n=strlen(s);
    int i=0;
    int cnt=0;
    while(i+k<=n){
        while(i+k<=n&&s[i]=='+')i++;
        if(i+k<=n){
            for(int j=i;j<i+k;j++){
                s[j]=flip(s[j]);
            }
            cnt++;
        }
//        cout<<i<<endl;
    }

//    printf("%s\n",s);

    for(int i=0;i<n;i++)if(s[i]=='-')return -1;
    return cnt;
}

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;scanf("%d",&T);
    for(int t=1;t<=T;t++){
        printf("Case #%d: ",t);
        scanf("%s%d",s,&k);
        int ans=work();
        if(ans==-1)puts("IMPOSSIBLE");
        else printf("%d\n",ans);
//        cout<<work()<<endl;
    }
}
