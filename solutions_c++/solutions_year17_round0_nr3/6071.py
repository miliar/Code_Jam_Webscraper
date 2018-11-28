#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<stack>
#include<queue>
#include<vector>
#include<set>
#include<map>
#include<string>
using namespace std;
typedef long long ll;



int main()
{
    //freopen("C-small-2-attempt0.in","r",stdin);
   // freopen("C-large.out-1.txt", "w", stdout);
    int t;
    scanf("%d",&t);
    for(int ca=1;ca<=t;ca++)
    {
        priority_queue<int> q;
        int n,k;
        scanf("%d%d",&n,&k);
        if(n==k)
        {
            printf("Case #%d: 0 0\n",ca);
            continue;
        }
        int l,r;
        q.push(n);
        while(k--)
        {
            int p=q.top();
            q.pop();
            if(p%2)
            {
                l=r=p/2;
                q.push(l);
                q.push(r);
            }
            else
            {
                l=p/2-1;
                r=p/2;
                q.push(l);
                q.push(r);
            }
        }
        printf("Case #%d: %d %d\n",ca,r,l);
    }
    return 0;
}
