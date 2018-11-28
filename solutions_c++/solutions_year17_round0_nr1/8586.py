#include <bits/stdc++.h>
/*#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <set>*/
#define pb push_back
#define ll long long int
#define ull unsigned long long int
#define gcd(a,b)    __gcd(a,b)
#define sz sizeof
#define INF 1000000000000000000LL
#define ms memset
#define FOR(i,N) FORR(i, 0, N)
#define FORR(i,a,b) FOTR(i, a, b, 1)
#define FOTR(i,a,b,c) for(int i=(a);i<(b);i+=(c))

using namespace std;

#define dbg(args...) {string s(#args);s+=',';cout<<"-->";debugger::call(s.begin(), s.end(), args);cout<<"\n";}
#define dbg_A(A, N) {cout<<#A<<"=(";FOR(i,N)cout<<A[i]<<" ";cout<<"\b)\n";}
struct debugger{
    typedef string::iterator si;
    static void call(si it, si ed){}
    template<typename T, typename ... aT>
    static void call(si it, si ed, T a, aT&... rest){
        string b;
        for(;*it!=',';++it) if(*it!=' ')b+=*it;
        cout << b << "=" << a << " ";
        call(++it, ed, rest...);
    }
};

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    std::ios_base::sync_with_stdio(false);
    cin.tie(0);
    ll t,i,k,cases=1;
    string s;
    cin>>t;
    while(t--){
        cin>>s>>k;
        int bit=0;
        ll ans=0;
        for(i=0;i<s.length();i++){
            if(i+k>s.length()) break;
            if(s[i]=='+') continue;
            ans++;
            for(ll cnk=0,j=i;cnk<k;j++,cnk++){
                if(s[j]=='+') s[j] = '-';
                else s[j] = '+';
            }
        }
        for(i=0;i<s.length();i++){
            if(s[i]=='-') bit=1;
        }
        cout<<"Case #"<<cases<<": ";
        if(bit==1) cout<<"IMPOSSIBLE"<<endl;
        else cout<<ans<<endl;
        cases++;
    }



    return 0;
}
