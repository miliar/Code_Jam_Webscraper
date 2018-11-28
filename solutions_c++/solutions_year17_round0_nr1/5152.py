//  Created by Chlerry in 2017.
//  Copyright (c) 2017 Chlerry. All rights reserved.
//

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <cmath>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;
#define Size 1000010
#define ll long long
#define mk make_pair
#define pb push_back
#define mem(array, x) memset(array,x,sizeof(array))
typedef pair<int,int> P;

int main()
{
    // freopen("in.txt","r",stdin);
    // freopen("out.txt","w",stdout);
    int T;cin>>T;
for(int ca=0;ca<T;ca++)
{
    //cout<<"-----------------"<<endl;
    string s;cin>>s;
    //cout<<s<<endl;
    int k,ans=0;cin>>k;
    //cout<<"k="<<k<<endl;
    for(int i=0;i<=s.size()-k;i++)
    {
        if(s[i]=='-')
        {
            ans++;
            for(int j=0;j<k;j++)
                if(s[i+j]=='+')
                    s[i+j]='-';
                else s[i+j]='+';
            //cout<<s<<endl;
        }
    }
    for(int i=s.size()-k+1;i<s.size();i++)
        if(s[i]=='-')
        {
            ans=-1;
            break;
        }
    if(ans==-1)
        printf("Case #%d: IMPOSSIBLE\n",ca+1);
    else
        printf("Case #%d: %d\n",ca+1,ans);
}
    return 0;
}
