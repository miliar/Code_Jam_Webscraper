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
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    //std::ios_base::sync_with_stdio(false);
    //cin.tie(0);
    int t,i;
    int a[1000],idx=0;
    for(i=1;i<=1000;i++){
        int ret = i,last=-1,bit=0;
        while(ret!=0){
            int g = ret%10;
            if(last!=-1){
                if(last>=g){}
                else bit=1;
            }
            last = g;
            ret/=10;
        }
        if(bit==0){
            a[idx] = i; idx++;
        }
    }
    int cases=1,n;
    cin>>t;
    while(t--){
        cin>>n;
        int ret = upper_bound(a,a+idx,n) - a;
        cout<<"Case #"<<cases<<": "<<a[ret-1]<<endl;cases++;
    }



    return 0;
}
