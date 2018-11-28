#include <stdio.h>
#include <queue>
#include <algorithm>

using namespace std;

priority_queue<int> qu;
int main()
{
    freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
    int t,T,i,n,k,a,b,count,x,y,temp;
    scanf("%d", &T);
    for(t=1; t<=T; t++)
    {
        count=0;
        printf("Case #%d: ", t);
        scanf("%d %d",&n,&k);
        a = (n-1)/2;
        b = n-1-a;
        //printf("%d %d\n", a, b);
        if(k==1)
            printf("%d %d\n",max(a,b),min(a,b));
        else
        {
            qu.push(a);
            qu.push(b);
            count++;
            while(!qu.empty())
            {
                x = qu.top();qu.pop();
                a = (x-1)/2;
                b = x-1-a;
                if(a >=0 && b >=0)
                {
                    qu.push(a);
                    qu.push(b);
                    count++;
                }
                if(count == k)
                {
                    printf("%d %d\n",max(a,b),min(a,b));
                    break;
                }
                y = qu.top();qu.pop();
                a = (y-1)/2;
                b = y-1-a;
                if(a >=0 && b >=0)
                {
                    qu.push(a);
                    qu.push(b);
                    count++;
                }
                if(count == k)
                {
                    printf("%d %d\n",max(a,b),min(a,b));
                    break;
                }
            }

        }
        while(!qu.empty()) qu.pop();

    }
    return 0;
}
