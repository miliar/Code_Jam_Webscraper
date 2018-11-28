#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <bits/stdc++.h>
using namespace std;

using namespace std;
#define M 1000000007

int main(){
    freopen("B-large.in","r",stdin);
	freopen("out2.txt","w",stdout);
	int t,l,i,j;
    cin>>t;
    string s;
    for(int tt=1;tt<=t;tt++){
        cin>>s;
        l=s.length();
        if(l==1)
            goto out;
        for(i=l-2;i>=0;i--){
            if(s[i]<=s[i+1])
                continue;
            s[i]--;
            for(j=i+1;j<l;j++)
                s[j]='9';
        }
        if(s[0]=='0')
            s=s.substr(1);
        out:
        cout<<"Case #"<<tt<<": "<<s<<endl;
    }
}
