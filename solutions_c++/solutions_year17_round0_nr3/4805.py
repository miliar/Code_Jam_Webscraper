#include <bits/stdc++.h>
using namespace std;
int main()
{
int T,x,y=1,n,j,tn;
cin>>T;
while(T--)
{
priority_queue<int>p;
int run;
cin>>n>>j;
p.push(n);
for(int i=0;i<j-1;i++)
    {
        x=p.top();
        p.pop();
            if(x%2!=0)
            {p.push(x/2);p.push(x/2);}
            if(x%2==0)
            {p.push(x/2);p.push(x/2 - 1);}
    }
        tn=p.top();
        if(tn%2!=0)
        {printf("Case #%d: %d %d\n",y,tn/2,tn/2);}
        if(tn%2==0)
        {printf("Case #%d: %d %d\n",y,tn/2,tn/2 - 1);}
        y++;
}
}