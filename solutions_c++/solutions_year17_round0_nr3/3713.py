#include<iostream>
#include<stdio.h>
#include<string.h>
#include<queue>
using namespace std;
const int N = 2000;

int n , k;

struct node{
    int left , len;
    node(int _left = 0,int _len = 0)
    {
        left = _left;
        len = _len;
    }
    bool operator < (node x) const
    {
        if(len != x.len) return len < x.len;
        return left > x.left;
    }
};



void init()
{
    scanf("%d%d",&n,&k);
}

void work()
{
    int li,ri;
    priority_queue<node>x;
    x.push(node(1,n));
    int q = 0;
    while(k--)
    {
        node y = x.top() , l , r;
        int mid ;
        x.pop();
        q++;
    //    printf("%d %d %d\n",q,y.left,y.len);
        if(y.len % 2 == 1)
        {
            mid = y.left + y.len / 2;
        }
        else
        {
            mid = y.left + y.len / 2 - 1;
        }

        ri = mid - y.left;
        li = y.len - ri - 1;

        l = node(y.left , mid - y.left);
        r = node(mid + 1 , y.left + y.len - 1 - mid);
        if(l.len > 0) x.push(l);
        if(r.len > 0) x.push(r);
    }

    printf("%d %d\n",li,ri);
}

int main()
{
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-small-2-attempt0.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int i = 1;i <= T;i++)
    {
        printf("Case #%d: ",i);
        init();
        work();
    }

    return 0;
}
