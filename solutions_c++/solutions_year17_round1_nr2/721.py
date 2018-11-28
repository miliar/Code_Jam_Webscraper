//
//  main.cpp
//  test1
//
//  Created by Lingsong Zeng on 3/2/17.
//  Copyright © 2017 Lingsong Zeng. All rights reserved.
//



/**
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;
int a[2],b[2][8];
int main(){
    int t,cas=0;
    cin>>t;
    while(t--){
        printf("Case #%d: ",++cas);
        int n,p;
        cin>>n>>p;
        for(int i=0;i<n;i++)
            cin>>a[i];
        for(int i=0;i<n;i++)
            for(int j=0;j<p;j++)
                cin>>b[i][j];
        int c[8];
        if(n==1){
            int ans=0;
            for(int i=0;i<p;i++){
                bool flag=false;
                int left=b[0][i]*10/11;
                int right=b[0][i]*10/9;
                while(left*11<b[0][i]*10)left++;
                while(right*9>b[0][i]*10)right--;
                int down=left/a[0];
                while(down*a[0]<left)down++;
                int up=right/a[0];
                while(up*a[0]>right)up--;
                if(up<down||up<=0)flag=false;
                else flag=true;
                if(flag){
                    ans++;
                    continue;
                }
            }
            cout<<ans<<endl;
            continue;
        }
        int ans=0;
        for(int i=0;i<p;i++)
            c[i]=i;
        do{
            vector<pair<int,int> >d;
            for(int i=0;i<p;i++)
                d.push_back(make_pair(b[0][i],b[1][c[i]]));
            int tmp=0;
            for(int i=0;i<p;i++){
                bool flag=false;
                int left1=d[i].first*10/11,left2=d[i].second*10/11;
                int right1=d[i].first*10/9,right2=d[i].second*10/9;
                while(left1*11<d[i].first*10)left1++;
                while(right1*9>d[i].first*10)right1--;
                while(left2*11<d[i].second*10)left2++;
                while(right2*9>d[i].second*10)right2--;
                int down1=left1/a[0];
                while(down1*a[0]<left1)down1++;
                int up1=right1/a[0];
                while(up1*a[0]>right1)up1--;
                int down2=left2/a[1];
                while(down2*a[1]<left2)down2++;
                int up2=right2/a[1];
                while(up2*a[1]>right2)up2--;
                int down=max(down1,down2);
                int up=min(up1,up2);
                if(up<down||up<=0)flag=false;
                else flag=true;
                if(flag){
                    tmp++;
                    continue;
                }
            }
            ans=max(ans,tmp);
        }while(next_permutation(c,c+p));
        cout<<ans<<endl;
    }
}*/


#include<set>
#include<map>
#include<queue>
#include<vector>
#include<string>
#include<cstring>
#include<iostream>
using namespace std;
const int inf=1e9;
int g[1005][1005],f[1005][1005],p[1005],a[1005],b[1005],c[1005][1005];
pair<int,int> d[1005][1005];
int s,t,n;
int maxflow()
{
    queue<int>q;
    memset(f,0,sizeof(f));
    int mf=0;
    while(1)
    {
        memset(a,0,sizeof(a));
        while(!q.empty())q.pop();
        q.push(s);
        a[s]=inf;
        while(!q.empty())
        {
            int u=q.front();q.pop();
            if(u==t)
                break;
            for(int v=1;v<=n;v++)
                if(!a[v]&&f[u][v]<g[u][v])
                {
                    p[v]=u;
                    a[v]=min(a[u],g[u][v]-f[u][v]);
                    q.push(v);
                }
        }
        if(a[t]==0)
            break;
        for(int u=t;u!=s;u=p[u])
        {
            f[p[u]][u]+=a[t];;
            f[u][p[u]]-=a[t];
        }
        mf+=a[t];
    }
    return mf;
}
int main()
{
    int tests,cas=0;
    cin>>tests;
    while(tests--)
    {
        printf("Case #%d: ",++cas);
        memset(p,0,sizeof(p));
        memset(g,0,sizeof(g));
        int m,p;
        cin>>m>>p;
        for(int i=0;i<m;i++)
            cin>>b[i];
        for(int i=0;i<m;i++)
            for(int j=0;j<p;j++)
                cin>>c[i][j];
        s=0;
        t=1+m*p;
        for(int j=0;j<m;j++)
            for(int k=0;k<p;k++)
                d[j][k].first=d[j][k].second=0;
        for(int j=0;j<m;j++)
        for(int i=0;i<p;i++){
            int left=c[j][i]*10/11;
            int right=c[j][i]*10/9;
            while(left*11<c[j][i]*10)left++;
            while(right*9>c[j][i]*10)right--;
            int down=left/b[j];
            while(down*b[j]<left)down++;
            int up=right/b[j];
            while(up*b[j]>right)up--;
            d[j][i].first=down,d[j][i].second=up;
        }
        for(int i=0;i<p;i++)
            if(d[0][i].second>0&&d[0][i].second>=d[0][i].first)
                g[0][1+i]=1;
        for(int i=1;i<m;i++)
            for(int j=0;j<p;j++)
                for(int k=0;k<p;k++)
                    if(d[i][j].second>0&&d[i][j].second>=d[i][j].first&&d[i-1][k].second>0&&d[i-1][k].second>=d[i-1][k].first){
                        int x1=d[i][j].first,y1=d[i][j].second,x2=d[i-1][k].first,y2=d[i-1][k].second;
                        if(x1>y2||x2>y1)continue;
                        g[(i-1)*p+k+1][i*p+j+1]=1;
                }
        for(int i=0;i<p;i++)
            if(d[m-1][i].second>0&&d[m-1][i].second>=d[m-1][i].first)
                g[(m-1)*p+i+1][t]=1;
        n=1+m*p;
        cout<<maxflow()<<endl;
    }
}
