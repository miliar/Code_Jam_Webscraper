//
//  main.cpp
//  1
//
//  Created by 金航宇 on 2017/4/22.
//  Copyright © 2017年 金航宇. All rights reserved.
//

#include <iostream>
using namespace std;
int main(int argc, const char * argv[]) {
    // insert code here...
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int tt;
    int cas=0;
    scanf("%d",&tt);
    double ans;
    int d,n,pos,s;
    while(tt--)
    {
        scanf("%d%d",&d,&n);
        ans=0;
        for(int i=1;i<=n;i++)
        {
            cin>>pos>>s;
            if((d-pos+0.0)/(s+0.0)>ans)ans=(d-pos+0.0)/(s+0.0);
        }
        printf("Case #%d: %.10lf\n",++cas,(d+0.0)/ans);
    }
    return 0;
}
