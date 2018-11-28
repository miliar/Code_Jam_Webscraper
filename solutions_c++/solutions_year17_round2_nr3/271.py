//
//  main.cpp
//  1
//
//  Created by 金航宇 on 2017/4/22.
//  Copyright © 2017年 金航宇. All rights reserved.
//

#include <iostream>
using namespace std;

double ans;
int n,q;
double d[150][150];
int e[150],s[150],ui,vi;
int main(int argc, const char * argv[]) {
    // insert code here...
    freopen("1.txt","r",stdin);
    freopen("1.out","w",stdout);
    int tt;
    int cas=0;
    scanf("%d",&tt);
    while(tt--)
    {
        cin>>n>>q;
        for(int i=1;i<=n;i++)cin>>e[i]>>s[i];
        for(int i=1;i<=n;i++)for(int j=1;j<=n;j++)cin>>d[i][j];
        
        for(int j=1;j<=n;j++)for(int i=1;i<=n;i++)if(i!=j)for(int k=1;k<=n;k++)if(k!=j&&k!=i)
        {
            if(d[i][j]>=0&&d[j][k]>=0&&(d[i][k]<0||d[i][k]>d[i][j]+d[j][k]))
            {
                d[i][k]=d[i][j]+d[j][k];
            }
        }
        for(int i=1;i<=n;i++)for(int j=1;j<=n;j++)
        {
            if(d[i][j]>0&&d[i][j]<=e[i])d[i][j]=d[i][j]/(s[i]+0.0);
            else d[i][j]=-1;
        }
        for(int j=1;j<=n;j++)for(int i=1;i<=n;i++)if(i!=j)for(int k=1;k<=n;k++)if(k!=j&&k!=i)
        {
            if(d[i][j]>=0&&d[j][k]>=0&&(d[i][k]<0||d[i][k]>d[i][j]+d[j][k]))
            {
                d[i][k]=d[i][j]+d[j][k];
            }
        }
        
        printf("Case #%d: ",++cas);
        for(int i=1;i<=q;i++)
        {
            cin>>ui>>vi;
            printf(" %.10lf",d[ui][vi]);
        }
        cout<<endl;
    }
    return 0;
}
