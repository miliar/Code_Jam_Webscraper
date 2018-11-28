//
//  main.cpp
//  test1
//
//  Created by Lingsong Zeng on 3/2/17.
//  Copyright © 2017 Lingsong Zeng. All rights reserved.
//




#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<stack>
#include<cstdio>
#include<string>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
int main(){
    int t,cas=0;
    cin>>t;
    while(t--){
        string s;
        int k;
        cin>>s>>k;
        int ans=0;
        for(int i=0;i<s.size();i++)
        if(s[i]=='-')
        {
            ans++;
            if(i+k>s.size()){
                ans=-1;
                break;
            }
            for(int j=0;j<k;j++)
            {
                if(s[i+j]=='+')
                    s[i+j]='-';
                else
                    s[i+j]='+';
            }
        }
        printf("Case #%d: ",++cas);
        if(ans>=0)
            cout<<ans<<endl;
        else
            cout<<"IMPOSSIBLE"<<endl;
    }
}