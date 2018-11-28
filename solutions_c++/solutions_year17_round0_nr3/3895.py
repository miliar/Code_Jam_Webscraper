#include <stdio.h>
#include <algorithm>
#include <queue>
using namespace std;

priority_queue<int> que;
void solve (int x,int y)
{
    int i,a,b,t;

    que.push(x);

    for(i=1;i<=y;i++){
        t=que.top();

        a=t/2;
        b=t/2 - (t%2?0:1);

        que.pop();
        que.push(a);
        que.push(b);
    }

    printf("%d %d\n",a,b);

    while(!que.empty())
        que.pop();
    return ;
}
int main (void)
{
    int i,T,x,y;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);

    for(i=0;i<T;i++){
        scanf("%d %d",&x,&y);
        printf("Case #%d: ",i+1);
        solve(x,y);
    }

    return 0;
}
