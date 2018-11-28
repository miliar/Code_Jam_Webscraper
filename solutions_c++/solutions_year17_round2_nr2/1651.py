#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<queue>
using namespace std;
typedef pair<int,char> A;
priority_queue <A> q;
char help[7]="ROYGBV";
int a[6];
int main()
{
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    A temp,temp1;
    int t,i,j,k,sum,n,mem;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%d",&n);
        for(i=0;i<6;i++)
        {
            scanf("%d",&temp.first);
            a[i]=temp.first;
            temp.second=help[i];
            if(temp.first)
            q.push(temp);
        }
        sort(a,a+6);
        printf("Case #%d: ",k);
        if(a[0]+a[1]+a[2]+a[3]+a[4]<a[5])
        {
            printf("IMPOSSIBLE\n");
            while(!q.empty())
                q.pop();
            continue;
        }
        while(!q.empty())
        {
            temp=q.top();
            q.pop();
            if(temp.second==mem)
            {
                temp1=q.top();
                q.pop();
                printf("%c",temp1.second);
                mem=temp1.second;
                temp1.first--;
                if(temp1.first)
                    q.push(temp1);
                q.push(temp);
                continue;
            }
            printf("%c",temp.second);
            mem=temp.second;
            temp.first--;
            if(temp.first)
                q.push(temp);
        }
        printf("\n");
    }
    return 0;
}
