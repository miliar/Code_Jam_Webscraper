#include<bits/stdc++.h>
using namespace std;
//1 0 1 0 1 0 1 0 0 1
//1 0 0 0 1 0 1 0 0 1
int main()
{
    int t,n,no=0;
    freopen("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);

    scanf("%d",&t);

    while(t--)
    {
        int tot,k,i,p;
        no++;
        priority_queue <int> q;
        scanf("%d %d",&n,&k);
        q.push(n);
        for(i=0;i<k-1;i++)
        {
            p=q.top();
            q.pop();
            if(p%2)
            {
                q.push(p/2);
                q.push(p/2);
            }
            else
            {
                q.push(p/2);
                q.push(p/2-1);
            }
        }
        p=q.top();
        printf("Case #%d: ",no);
        if(p%2)
        {
            printf("%d %d\n",p/2,p/2);
        }
        else
        printf("%d %d\n",p/2,p/2-1);
        //q.pop();
        //printf("%d\n",tot+d);
    }

}

