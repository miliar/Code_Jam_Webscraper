#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<climits>
#include<cmath>
#include<utility>
#include<set>
#include <queue>
#define ull unsigned long long
#define ll long long
#define pii pair<int,int>
#define pb(x) push_back(x)
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%lld",&x)
#define M(x,i) memset(x,i,sizeof(x))
#define F(i,a,n) for(int i=(a);i<(n);++i)
#define FD(i,a,n) for(int i=(a);i>=(n);--i)
using namespace std;
int main()
{
    freopen("inp.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t;
    cin>>t;
    F(p,1,t+1){
        string s;
        int k;

        cin>>s>>k;

        int len = s.length();

        int ans = 0;
        FD(i,len-1,k-1){
            if(s[i] == '-'){
                ans++;
                FD(j,i,i-k+1){
                    s[j] = (s[j] =='-')?'+':'-';
                }
            }
        }

        F(i,0,len){
            if(s[i] == '-'){
                ans = -1;
            }
        }

        if(ans>=0){
            cout<<"Case #"<<p<<": "<<ans<<endl;
        } else {
            cout<<"Case #"<<p<<": IMPOSSIBLE"<<endl;
        }
            
    }
}


                


            
