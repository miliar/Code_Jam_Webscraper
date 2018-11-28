#include <cmath>
#include <cstdio>
#include <map>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <stack>
using namespace std;
#define REP(I,N)   FOR(I,0,N)
#define pb push_back
#define LL long long
#define ff first
#define ss second
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out2.txt","w",stdout);
    int tcase;
    cin>>tcase;
    for(int j=1; j<=tcase; j++)
    {
        LL m,n;
        cin>>m;
        n=m;
        //cout<<m<<endl;
        vector<int>v;
        while(n)
        {
            v.push_back(n%10);
            n/=10;
        }
        reverse(v.begin(),v.end());
        int f=1,s=0;
        for(int i=v.size()-2; i>=0; i--)
        {
           if(v[i]>v[i+1])
           {
            v[i]-=1;
            for(int l = i + 1;l<v.size();l++)
                v[l]=9;
           }
        }
        long long d = 0;
        for(int c:v)
        {
            if(c==-1)
                c=0;
            d = d*10 + c;
        }
        cout<<"Case #"<<j<<": "<<d<<endl;

    }
    return 0;
}


