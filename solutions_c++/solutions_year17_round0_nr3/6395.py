#include<bits/stdc++.h>
using namespace std;
priority_queue<int>Q;
int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int c,t,n,k,u;
    scanf("%d",&t);
    for(c=1;c<=t;c++){
        scanf("%d%d",&n,&k);
        while(!Q.empty()) Q.pop();
        Q.push(n);
        while(--k){
            u=Q.top(),Q.pop();
            if(u&1) Q.push(u/2),Q.push(u/2);
            else Q.push(u/2),Q.push(u/2-1);
        }
        u=Q.top();
        if(u&1) printf("Case #%d: %d %d\n",c,u/2,u/2);
        else printf("Case #%d: %d %d\n",c,u/2,u/2-1);
    }
}
