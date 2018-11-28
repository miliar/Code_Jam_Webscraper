#include<stdio.h>
#include<math.h>
#include<queue>
#include<string.h>
#include<iostream>
using namespace std;
struct Node{
    int len;
    int index;
    Node(int l=0,int i=0)
    {
        len=l;
        index=i;
    }
    bool operator < (const Node &a) const {
        if(len==a.len)
            return index>a.index;
        return len<a.len;//最小值优先
    }
};
priority_queue<Node>Q;
int main()
{
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-small-2-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    int ca=1;
    while(t--)
    {
        int n,k;
        scanf("%d%d",&n,&k);
        while(!Q.empty())Q.pop();
        Q.push(Node(n,1));
        k--;
        Node tmp;
        while(k--)
        {
            tmp=Q.top();Q.pop();
            Q.push(Node((tmp.len-1)/2,tmp.index));
            Q.push(Node(tmp.len/2,tmp.index+(tmp.len+1)/2));
        }
        tmp=Q.top();
        printf("Case #%d: %d %d\n",ca++,tmp.len/2,(tmp.len-1)/2);
    }
    return 0;
}
