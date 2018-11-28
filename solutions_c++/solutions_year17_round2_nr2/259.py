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
int n,r,o,y,g,b,v;
int x[2000];
int main(int argc, const char * argv[]) {
    // insert code here...
    freopen("1.txt","r",stdin);
    freopen("1.out","w",stdout);
    int tt;
    int cas=0;
    scanf("%d",&tt);
    while(tt--)
    {
        printf("Case #%d: ",++cas);
        cin>>n;
        cin>>r>>o>>y>>g>>b>>v;
        int r0=r,o0=o,y0=y,g0=g,b0=b,v0=v;
        //   1  2  3  4  5  6
        bool f=0;
        if(o>b||g>r||v>y)f=1;
        //if((o>0&&o==b)||(g>0&&g==r)||(v>0&&v==y))f=1;
        int m=n-2*o-2*g-2*v;
        if(b-o>m/2||r-g>m/2||y-v>m/2)f=1;
        if(r>0){x[1]=1;r--;}
        else if(y>0){x[1]=3;y--;}
        else if(b>0){x[1]=5;b--;}
        for(int i=2;i<=n;i++)
        {
            if(x[i-1]==2){x[i]=5;b--;continue;}
            if(x[i-1]==4){x[i]=1;r--;continue;}
            if(x[i-1]==6){x[i]=3;y--;continue;}
            if(x[i-1]==1)if(g>0){x[i]=4;g--;continue;}
            if(x[i-1]==3)if(v>0){x[i]=6;v--;continue;}
            if(x[i-1]==5)if(o>0){x[i]=2;o--;continue;}
            if(x[i-1]==1)
            {
                if(y-v>b-o||(y-v==b-o&&x[1]==3)){x[i]=3;y--;continue;}
                else{x[i]=5;b--;continue;}
            }
            if(x[i-1]==3)
            {
                if(b-o>r-g||(b-o==r-g&&x[1]==5)){x[i]=5;b--;continue;}
                else {x[i]=1;r--;continue;}
            }
            if(x[i-1]==5)
            {
                if(r-g>y-v||(r-g==y-v&&x[1]==1)){x[i]=1;r--;continue;}
                else {x[i]=3;y--;continue;}
            }

        }/*
        for(int i=1;i<=n;i++)
        {
            if(x[i]==1)cout<<"R";
            if(x[i]==2)cout<<"O";
            if(x[i]==3)cout<<"Y";
            if(x[i]==4)cout<<"G";
            if(x[i]==5)cout<<"B";
            if(x[i]==6)cout<<"V";
        }*/
        //cout<<endl;
        if(r<0||o<0||y<0||g<0||b<0||v<0||x[1]==x[n])f=1;
        if(x[n]%2==0&&x[1]%2==0)f=1;
        if((x[n]-x[1]+6)%6==1||(x[n]-x[1]+6)%6==5)f=1;
        if(f) cout<<"IMPOSSIBLE"<<endl;
        else
        {
            for(int i=1;i<=n;i++)
            {
                if(x[i]==1)cout<<"R";
                if(x[i]==2)cout<<"O";
                if(x[i]==3)cout<<"Y";
                if(x[i]==4)cout<<"G";
                if(x[i]==5)cout<<"B";
                if(x[i]==6)cout<<"V";
            }
            cout<<endl;
        }
    }
    return 0;
}
