
/*****************************************
Author: lizi
Email: lzy960601@outlook.com
****************************************/
  
#include<bits/stdc++.h>
  
using namespace std;
  
const double eps=1e-10;
const double pi=3.1415926535897932384626433832795;
const double eln=2.718281828459045235360287471352;
  
#define LL long long
#define IN freopen("cs.in", "r", stdin)
#define OUT freopen("cs.out", "w", stdout)
#define scan(x) scanf("%d", &x)
#define mp make_pair
#define pb push_back
#define sqr(x) (x) * (x)
#define pr(x) printf("Case %d: ",x)
#define prn(x) printf("Case %d:\n",x)
#define prr(x) printf("Case #%d: ",x)
#define prrn(x) printf("Case #%d:\n",x)
#define lowbit(x) (x&(-x))

struct node
{
    int hd,ad,hk,ak,num;
};
int T;

const int cs=200;
int dh,da,kh,ka,b,d;

int main()
{
    IN;OUT;
    scanf("%d",&T);
    for(int _=1;_<=T;_++)
    {
        queue<node> q;
        while(!q.empty())q.pop();
        scanf("%d%d%d%d%d%d",&dh,&da,&kh,&ka,&b,&d);
        struct node bg={dh,da,kh,ka,0};
        q.push(bg);
        int ans=1e9+7;
        while(!q.empty())
        {
            struct node temp = q.front();q.pop();
            if(temp.hd<dh-temp.ak && temp.ak>0)//cure
            {
                struct node nxt=temp;
                nxt.hd=dh;
                nxt.hd-=nxt.ak;
                nxt.num++;
                if(nxt.hd>0 && nxt.num<cs)q.push(nxt);
            }
            if(temp.ad<temp.hk)//buff
            {
                struct node nxt=temp;
                nxt.ad+=b;
                nxt.hd-=nxt.ak;
                nxt.num++;
                if(nxt.hd>0 && nxt.num<cs)q.push(nxt);
            }
            if(temp.ak>0)//debuff
            {
                struct node nxt=temp;
                nxt.ak=max(0,nxt.ak-d);
                nxt.hd-=nxt.ak;
                nxt.num++;
                if(nxt.hd>0 && nxt.num<cs)q.push(nxt);
            }
            if(temp.ad>0)//attack
            {
                struct node nxt=temp;
                nxt.hk-=nxt.ad;
                if(nxt.hk<=0)
                {
                    ans=nxt.num+1;
                    break;
                }
                nxt.hd-=nxt.ak;
                nxt.num++;
                if(nxt.hd>0 && nxt.num<cs)q.push(nxt);
            }
        }
        prr(_);
        if(ans<1e9)printf("%d\n",ans);else printf("IMPOSSIBLE\n");
    }
    return 0;
}
