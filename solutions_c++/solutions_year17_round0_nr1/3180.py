#include <bits/stdc++.h>

#define st first 
#define nd second 
using namespace std;

typedef long long LL;

int n,m;
char st[10000];
bool f[10000];

void solve(int cs){
    scanf("%s %d",st,&n);
    memset(f,0,sizeof(f));
    int l=strlen(st);
    m=0;
    bool cur=0;
    bool ans=1;
    for (int i=0;i<l;++i){
        if (f[i]) cur=!cur;
        if (cur) st[i]=(st[i]=='+')?('-'):('+');
        if (st[i]=='-') {
        cur=!cur,++m,f[i+n]=!f[i+n]; 
        if (i+n>l) {ans=0; break;}
        }
    }
    printf("Case #%d: ",cs);
    if (ans) printf("%d\n",m);
        else printf("IMPOSSIBLE\n");
}

int main(){
    int tot;
    scanf("%d",&tot);
    for (int i=1;i<=tot;++i) solve(i);
}
