#include<bits/stdc++.h>
using namespace std;

priority_queue<pair<int,int> > Q;

int main()
{
    FILE *f,*g;
    f = fopen("in.txt","r");
    g = fopen("out.txt","w");
    int t,i,x,y,n,k;
    fscanf(f,"%d",&t);
    int t1 = t;
    while(t--)
    {
        fscanf(f,"%d %d",&n,&k);
        if(n%2==1)
        {
            Q.push(make_pair(n/2,n/2));
        }
        else
        {
            Q.push(make_pair(n/2-1,n/2));
        }
        for(i=1;i<=k-1;i++)
        {
            x = Q.top().first;
            y = Q.top().second;
            Q.pop();
            if(x%2==1)
            {
                Q.push(make_pair(x/2,x/2));
            }
            else
            {
                Q.push(make_pair(x/2-1,x/2));
            }
            if(y%2==1)
            {
                Q.push(make_pair(y/2,y/2));
            }
            else
            {
                Q.push(make_pair(y/2-1,y/2));
            }
        }
        fprintf(g,"Case #%d: %d %d\n",t1-t,Q.top().second,Q.top().first);
        while(!Q.empty())
        {
            Q.pop();
        }
    }
    return(0);
}
