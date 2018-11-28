//
//  main.cpp
//  test1
//
//  Created by Lingsong Zeng on 3/2/17.
//  Copyright © 2017 Lingsong Zeng. All rights reserved.
//



#include<stdio.h>
#include<iostream>
#include<string.h>
#include<queue>
#include<set>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;
int a[105];
bool cmp2(int x,int y){
    return x%2<y%2;
}
int main(){
    int t,cas=0;
    cin>>t;
    while(t--){
        printf("Case #%d: ",++cas);
        int n,p;
        cin>>n>>p;
        for(int i=0;i<n;i++)
            cin>>a[i];
        if(p==2){
            sort(a,a+n,cmp2);
            int ans=0,leftover=0;
            for(int i=0;i<n;i++){
                if(leftover==0){
                    ans++;
                    leftover=(p-(a[i]%p))%p;
                }else{
                    if(leftover>=a[i])
                        leftover-=a[i];
                    else{
                        a[i]-=leftover;
                        leftover=(p-(a[i]%p))%p;
                    }
                }
            }
            cout<<ans<<endl;
        }
        if(p==3){
            int b[5]={0};
            int ans=0;
            for(int i=0;i<n;i++)
            {
                if(a[i]%3==0)
                    ans++;
                else
                    b[a[i]%3]++;
            }
            ans+=min(b[1],b[2]);
            int left=max(b[1],b[2])-min(b[1],b[2]);
            ans+=(left+2)/3;
            cout<<ans<<endl;
        }
        if(p==4){
            
        }
    }
}