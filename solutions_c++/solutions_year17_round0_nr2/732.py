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
        printf("Case #%d: ",++cas);
        long long n;
        cin>>n;
        string s=to_string(n);
        int len=(int)s.size();
        for(int i=len;i>=0;i--){
            bool f=true;
            for(int j=1;j<i;j++)
                if(s[j]<s[j-1])
                    f=false;
            if(!f)continue;
            if(i==len){
                cout<<s<<endl;
                break;
            }
            if(s[i]<s[i-1]+1)
                continue;
            s[i]=s[i]-1;
            for(int j=i+1;j<len;j++)
                s[j]='9';
            int j=(int)s.size()-1;
            reverse(s.begin(),s.end());
            while(s[j]=='0'&&j>0)
            {
                s.pop_back();
                j--;
            }
            reverse(s.begin(),s.end());
            cout<<s<<endl;
            break;
        }
    }
}