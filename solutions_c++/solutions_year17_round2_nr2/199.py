#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <string>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <map>
#include <queue>
#include <vector>
#define LL long long
#define CLR(a,x) memset(a,x,sizeof(a))
using namespace std;
const char ch[10]={'*','R','B','Y','G','O','V'};
template <typename T>inline void read(T &x)
{
    x=0;bool f=false;char ch=getchar();
    while (ch<'0'||'9'<ch) {if (ch=='-') f=!f;ch=getchar();}
    while ('0'<=ch&&ch<='9') {x=x*10+ch-'0';ch=getchar();}
    if (f) x=-x;
}
int n,m,t,a[10],ans[2000],r,o,y,g,b,v;
int main()
{
    #ifdef VGel
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    #endif // VGel
    int T_T;read(T_T);
    for (int T=1;T<=T_T;T++)
    {
        read(n);read(r);read(o);read(y);read(g);read(b);read(v);
//        cout<<r<<" "<<o<<" "<<y<<" "<<g<<" "<<b<<" "<<v<<endl;
        printf("Case #%d: ",T);
        if (b<o||r<g||y<v) {printf("IMPOSSIBLE\n");continue;}
        b-=o;r-=g;y-=v;
        if (o!=0&&b==0)
        {
            if (r||y||g||v) {printf("IMPOSSIBLE\n");continue;}
            while (o--) {printf("OB");}
            putchar('\n');continue;
        }
        if (g!=0&&r==0)
        {
            if (o||y||b||v) {printf("IMPOSSIBLE\n");continue;}
            while (g--) {printf("GR");}
            putchar('\n');continue;
        }
        if (v!=0&&y==0)
        {
            if (r||o||g||b) {printf("IMPOSSIBLE\n");continue;}
            while (v--) {printf("VY");}
            putchar('\n');continue;
        }

        a[1]=r;a[2]=b;a[3]=y;
        m=0;
        bool flag=true;
        if (a[1]>0) {ans[++m]='R';a[1]--;t=1;}
            else if (a[2]>0) {ans[++m]='B';a[2]--;t=2;}
                else {ans[++m]='Y';a[3]--;t=3;}
        while (a[1]>0 || a[2]>0 || a[3]>0)
        {
            int x=t+1,y=t-1;
            if (x>3) x=1; if (y==0) y=3;
            if (a[x]==0 && a[y]==0) {flag=false; break;}
            if (a[x]>a[y] || a[x]==a[y] && ch[x]==ch[1]) ans[++m]=ch[x],a[x]--,t=x;
                else ans[++m]=ch[y],a[y]--,t=y;
        }
        if (ans[1]==ans[m]) flag=false;

        if (!flag) printf("IMPOSSIBLE\n");
        else
        {
            bool fr=true,fb=true,fy=true;
            for (int i=1; i<=m; i++)
            {
                printf("%c",ans[i]);
                if (ans[i]=='B')
                {
                    if (fb)
                    {
                        while(o--) printf("OB");
                    }
                    fb=false;
                }
                else if (ans[i]=='R')
                {
                    if (fr)
                    {
                        while(g--) printf("GR");
                    }
                    fr=false;
                }
                else if (ans[i]=='Y')
                {
                    if (fy)
                    {
                        while(v--) printf("VY");
                    }
                    fy=false;
                }
            }
            putchar('\n');
        }
    }
    return 0;
}
