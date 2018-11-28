#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<vector>
#include<iostream>
#include<string>
#include<string.h>
using namespace std;
int r,o,y,g,b,v;
int n;
char ans[1005];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("b1.out","w",stdout);
    int t,ca=0;
    scanf("%d",&t);
    while(t--)
    {
        vector<char>ans;
        scanf("%d",&n);
        int nn=n;
        //1 1 2 1 2 1
        //0 1 1 1 1 1
        scanf("%d%d%d%d%d%d",&r,&o,&y,&g,&b,&v);
        printf("Case #%d: ",++ca);
        if(r==0&&y==0&&g==0&&v==0)
        {
            if(o==b)
            {
                for(int i=0; i<b; ++i)
                    printf("BO");
                puts("");
            }
            else puts("IMPOSSIBLE");
            continue;
        }
        if(b==0&&y==0&&o==0&&v==0)
        {
            if(g==r)
            {
                for(int i=0; i<g; ++i)
                    printf("GR");
                puts("");
            }
            else puts("IMPOSSIBLE");
            continue;
        }
        if(r==0&&o==0&&g==0&&b==0)
        {
            if(y==v)
            {
                for(int i=0; i<v; ++i)
                    printf("VY");
                puts("");
            }
            else puts("IMPOSSIBLE");
            continue;
        }
        if(r<g||y<v||b<o)
        {
            puts("IMPOSSIBLE");
            continue;
        }
        r-=g;
        y-=v;
        b-=o;
        n=r+y+b;
        if(n==0)
        {
            puts("IMPOSSIBLE");
            continue;
        }
        char last;
        char first;
        if(r>y+b||y>r+b||b>y+r)
        {
            puts("IMPOSSIBLE");
            continue;
        }
        if(r>=y&&r>=b)
        {
            ans.push_back('R');
            r--;
            first=last='R';
        }
        else if(y>=r&&y>=b)
        {
            ans.push_back('Y');
            y--;
            first=last='Y';
        }
        else
        {
            ans.push_back('B');
            b--;
            first=last='B';
        }
        for(int i=1; i<n; ++i)
        {
            if(last=='R')
            {
                for(int i=0; i<g; ++i)
                {
                    ans.push_back('G');
                    ans.push_back('R');
                }
                g=0;
                if(y<b)
                {
                    ans.push_back('B');
                    b--;
                    last='B';
                }
                else if(y>b)
                {
                    ans.push_back('Y');
                    y--;
                    last='Y';
                }
                else if(first=='Y')
                {
                    ans.push_back('Y');
                    y--;
                    last='Y';
                }
                else
                {
                    ans.push_back('B');
                    b--;
                    last='B';
                }
            }
            else if(last=='B')
            {
                for(int i=0; i<o; ++i)
                {
                    ans.push_back('O');
                    ans.push_back('B');
                }
                o=0;
                if(y<r)
                {
                    ans.push_back('R');
                    r--;
                    last='R';
                }
                else if(y>r)
                {
                    ans.push_back('Y');
                    y--;
                    last='Y';
                }
                else if(first=='Y')
                {
                    ans.push_back('Y');
                    y--;
                    last='Y';
                }
                else
                {
                    ans.push_back('R');
                    r--;
                    last='R';
                }
            }
            else
            {
                for(int i=0; i<v; ++i)
                {
                    ans.push_back('V');
                    ans.push_back('Y');
                }
                v=0;
                if(b<r)
                {
                    ans.push_back('R');
                    r--;
                    last='R';
                }
                else if(b>r)
                {
                    ans.push_back('B');
                    b--;
                    last='B';
                }
                else if(first=='R')
                {
                    ans.push_back('R');
                    r--;
                    last='R';
                }
                else
                {
                    ans.push_back('B');
                    b--;
                    last='B';
                }
            }
        }
        if(last=='R')
        {
            for(int i=0; i<g; ++i)
            {
                    ans.push_back('G');
                    ans.push_back('R');
                }
            g=0;
        }
        else if(last=='B')
        {
            for(int i=0; i<o; ++i)
            {
                    ans.push_back('O');
                    ans.push_back('B');
                }
            o=0;
        }
        else
        {
            for(int i=0; i<v; ++i)
     {
                    ans.push_back('V');
                    ans.push_back('Y');
                }
                v=0;
        }
        if(ans.size()==nn)
        {
            for(int i=0;i<ans.size();++i)
                putchar(ans[i]);
        puts("");
        }
        else puts("IMPOSSIBLE");
    }
}
