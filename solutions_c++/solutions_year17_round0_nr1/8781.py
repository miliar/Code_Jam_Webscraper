#include<iostream>
#include<cstdio>
#include<cstring>
#include<map>
#include<queue>
using namespace std;
int n,k,now;
char st[15];
map<int,int> p;
queue<int> q;
int bfs(){
    if (now==0){
        p[now]=0; return 1;
    }
    while (q.size()) q.pop();
    q.push(now);
    p[now]=0;
    while (q.size()){
        int u=q.front(); q.pop();
        int t=1<<k; t--;
        while (t<(1<<n)){
            int v=t^u;
            t=t<<1;
            if (p.count(v)) continue;
            p[v]=p[u]+1;
            if (v==0) return 1;
            q.push(v);
        }
    }
    return 0;
}
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T; cin>>T;
    for (int tt=1;tt<=T;tt++){
        scanf("%s",st);
        p.clear();
        n=strlen(st);
        scanf("%d",&k);
        now=0;
        for (int i=0;i<n;i++){
            if (st[i]=='-') now+=1<<i;
        }
        printf("Case #%d: ",tt);
        if (bfs()) printf("%d\n",p[0]); else
        printf("IMPOSSIBLE\n");
    }
}
