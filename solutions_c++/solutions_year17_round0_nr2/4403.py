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
string f(int x){
    stringstream ss;
    ss<<x;
    return ss.str();
}
int main()
{
    freopen("inp.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t;
    cin>>t;
    F(p,1,t+1){
        int ans=1;
        int n;
        cin>>n;

        FD(i,n,1){
            int flg = 0;
            string s = f(i);
            int len = s.length();
            F(i,1,len){
                if(s[i]<s[i-1]){
                    flg = 1;
                    break;
                }
            }

            if(flg ==0 ){
                ans = i;
                break;
            }
        }

        cout<<"Case #"<<p<<": "<<ans<<endl;
    }
}
            
