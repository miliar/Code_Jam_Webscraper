//created by missever

#include<bits/stdc++.h>
#define MAX 1000000007
using namespace std;
typedef long long LL;

char s[10005],g[10005];

bool ff(char a,char b,char c,int aa,int bb,int cc)
{
    if(bb > aa) swap(aa,bb),swap(a,b);
    if(cc > bb) swap(cc,bb),swap(c,b);
    if(bb > aa) swap(aa,bb),swap(a,b);
    if(bb + cc < aa) return false;
    int k = 0;
    while(aa)
    {
        while(bb >= cc && bb > 0 && aa > 0)
        {
            s[k++] = a;
            aa--;
            s[k++] = b;
            bb--;
        }
        while(cc > bb && cc > 0 && aa > 0)
        {
            s[k++] = a;
            aa--;
            s[k++] = c;
            cc--;
        }
    }
    while(bb || cc)
    {
        while(bb >= cc && bb > 0)
        {
            s[k++] = b;
            bb--;
        }
        while(cc > bb && cc > 0)
        {
            s[k++] = c;
            cc--;
        }
    }
    s[k] = 0;
    return true;
}

bool solve(string p,int a,int A,int b,int B,int c,int C)
{
    int i,j,k;
    a -= A;
    b -= B;
    c -= C;
    if(!ff(p[0],p[2],p[4],a,b,c)) return false;
    k = strlen(s);
    bool va,vb,vc;
    va = vb = vc = true;
    j = 0;
    for(i = 0;i < k; i++)
    {
        if(s[i] == p[0] && va)
        {
            for(int r = 0;r < A; r++)
            {
                g[j++] = p[0];
                g[j++] = p[1];
            }
            va = 0;
        }
        if(s[i] == p[2] && vb)
        {
            for(int r = 0;r < B; r++)
            {
                g[j++] = p[2];
                g[j++] = p[3];
            }
            vb = 0;
        }
        if(s[i] == p[4] && vc)
        {
            for(int r = 0;r < C; r++)
            {
                g[j++] = p[4];
                g[j++] = p[5];
            }
            vc = 0;
        }
        g[j++] = s[i];
    }
    g[j] = 0;
    return true;
}

int main(){
    //freopen("B-large.in","r",stdin);
    //freopen("B-small-attempt.out","w",stdout);
    int t,n,i,j;
    int a,b,c,ab,ac,bc;
    scanf("%d",&t);
    for(int cas = 1;cas <= t; cas++)
    {
        scanf("%d",&n);
        scanf("%d%d%d%d%d%d",&a,&ab,&b,&bc,&c,&ac);
        printf("Case #%d: ",cas);
        if((ab < c || ab == 0) && (ac < b || ac == 0) && (bc < a || bc == 0))
        {
            if(!solve("RGYVBO",a,bc,b,ac,c,ab)) printf("IMPOSSIBLE\n");
            else printf("%s\n",g);
        }
        else if(ab == c && a + b + ac + bc == 0)
        {
            j = 0;
            for(i = 0;i < c; i++)
            {
                g[j++] = 'O';
                g[j++] = 'B';
            }
            g[j] = 0;
            printf("%s\n",g);
        }
        else if(ac == b && a + c + ab + bc == 0)
        {
            j = 0;
            for(i = 0;i < b; i++)
            {
                g[j++] = 'V';
                g[j++] = 'Y';
            }
            g[j] = 0;
            printf("%s\n",g);
        }
        else if(bc == a && c + b + ac + ab == 0)
        {
            j = 0;
            for(i = 0;i < a; i++)
            {
                g[j++] = 'R';
                g[j++] = 'G';
            }
            g[j] = 0;
            printf("%s\n",g);
        }
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
