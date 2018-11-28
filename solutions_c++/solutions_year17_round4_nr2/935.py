#include<cstdio>
#include<iostream>
#include<vector>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<map>
using namespace std;
int n,c,m;
vector<int> st[1005];
int c1[1005],c2[1005];
int max(int a, int b)
{

    if(a>b)
    return a;
    else
    return b;
}
int main()
{
    freopen("B-small.in","r",stdin);
    freopen("B-small.out","w",stdout);
    int T,cas=0;scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d%d",&n,&c,&m);
        memset(st,0,sizeof(st));
        memset(c1,0,sizeof(c1));
        memset(c2,0,sizeof(c2));
        for(int i=0;i<m;i++)
        {
            int x,y;
            scanf("%d%d",&x,&y);
            st[y].push_back(x);
            if(i==0)
            c1[x] ++;
            else
            c2[x] ++;
        }
        for(int i=1;i<=c;i++)
        sort(st[i].begin(),st[i].end());
        int ans1=0,ans2=0;
        int d1=st[1].size()-c2[1]-c1[1];
        int d2=st[2].size()-c1[1]-c2[1];
        ans1 = c1[1] + c2[1] + max(max(d1,d2), 0);
        while(1)
        {
            if(c1[1]>0)
            {
                int done=0;
                for(int i=2;i<=1000;i++)
                {
                    if(c1[i]>0&&c2[i]>0)
                    {
                        c2[i] --;
                        done=1;
                        break;
                    }
                }
                if(!done)
                {
                    for(int i=2;i<=1000;i++)
                    if(c2[i]>0)
                    {
                        c2[i] --;
                        break;
                    }
                }
                c1[1] --;
            }
            else if(c2[1]>0)
            {
                int done=0;
                for(int i=2;i<=1000;i++)
                {
                    if(c1[i]>0&&c2[i]>0)
                    {
                        c1[i] --;
                        done=1;
                        break;
                    }
                }
                if(!done)
                {
                    for(int i=2;i<=1000;i++)
                    if(c1[i]>0)
                    {
                        c1[i] --;
                        break;
                    }
                }
                c2[1] --;
                ans2++;
            }
            else
            break;
        }
        int len1=st[1].size()-c2[1]-c1[1],len2=st[2].size()-c1[1]-c2[1];
        if(len1 > len2)
        {
            for(int i=1;i<=1000;i++) swap(c1[i],c2[i]);
        }
        while(1)
        {
            int check=0;
            for(int i=2;i<=1000;i++)
            {
                if(c1[i]>0)
                {
                    check=1;
                    int has=0;
                    for(int j=2;j<=1000;j++)
                    {
                        if(c2[j]>0&&i!=j)
                        {
                            has=1;
                            c2[j]--;
                            break;
                        }
                    }
                    if(!has)
                    {
                        if(c2[i]>0)
                        {
                            c2[i]--;
                            ans2++;
                        }


                    }
                    c1[i]--;
                }
            }
            if(!check)
            break;
        }
        printf("Case #%d: %d %d\n", ++cas, ans1, ans2);

    }
}
