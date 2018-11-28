#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int tree[1005];
char ss[1005];
int n;
inline int lowbit(int x)
{
    return x&-x;
}
void add(int x,int val)
{
    for(int i=x; i<=n; i+=lowbit(i))
        tree[i]+=val;
}
int  get(int x)
{
    int sum=0;
    for(int i=x; i; i-=lowbit(i))
        sum+=tree[i];
    return sum;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("outputA.txt","w",stdout);
    int t;
    int cnt=1;
    cin>>t;
    while(t--)
    {
        memset(tree,0,sizeof tree);
        scanf("%s",ss+1);
        int k;
        cin>>k;
        int len =strlen(ss+1);
        n=len;
        for(int i=1; i<=len; i++)
            if (ss[i]=='-')
            {
                add(i,1);
                add(i+1,-1);
            }
//        for(int i=1;i<=len;i++)
//            printf("%d ",get(i));
//        printf("\n");
        int num=0;
        for(int i=1; i<=len-k+1; i++)
        {
            if (get(i)%2==0)continue;
            else
            {
                num++;
                add(i,+1);
                add(i+k,-1);
            }
        }
        int flag=0;
        for(int i=1; i<=len; i++)
        {
            if (get(i)%2!=0)
            {
                flag=1;
                break;
            }
        }
        printf("Case #%d: ",cnt++);
        if (flag )printf("IMPOSSIBLE\n");
        else printf("%d\n",num);
    }



    return 0;
}
//896521 183995
