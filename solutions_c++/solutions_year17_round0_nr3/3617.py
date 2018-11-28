#include<bits/stdc++.h>
using namespace std;

int v1,v2;

void cal(int n,int k)
{
    priority_queue<int>q;
    int cnt=1;
    q.push(n);
    while(!q.empty())
    {
        int v=q.top();q.pop();
        if(cnt==k)
        {
            while(!q.empty()) q.pop();
            v1=v/2,v2=v/2-(v%2==0);
            return;
        }
        cnt++;
        q.push(v/2);
        q.push(v/2-(v%2==0));
    }

}

int main()
{
    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("output.in", "w", stdout);
    int t,n,k;
    scanf("%d",&t);
    for(int ca=1; ca<=t; ca++)
    {
        fprintf(stderr,"test %d\n",ca);
        fflush(stderr);
        scanf("%d %d",&n,&k);
        cal(n,k);
        printf("Case #%d: %d %d\n",ca,v1,v2);

    }
}
