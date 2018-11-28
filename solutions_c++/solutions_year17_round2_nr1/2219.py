#include <bits/stdc++.h>
using namespace::std;

#define TRACE(x) cerr<<"[[ "<<#x<<" = "<<x<<" ]]"<<endl;
#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__,__VA_ARGS__)
template <typename Arg1> void __f(const char* name, Arg1 && arg1) {
	cerr << name << " : " << arg1 << endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args) {
	const char* comma = strchr(names + 1, ',');
	cerr.write(names, comma - names) << " : " << arg1 << " | "; __f(comma + 1, args...);
}

#else
#define trace(...)
#endif
#define Assert(x,y) {if(x!=y){cerr<<__LINE__ <<"->  Assertion Failed "<<": ("<<#x<<"!="<<y<<") ";TRACE(x);exit(1);}}

#define ll long long
#define LD long double
#define ff first
#define ss second
#define mp make_pair
#define pb push_back

typedef unsigned int uint;
typedef long long int64;
typedef unsigned long long uint64;

#define CASE(tt) printf("Case #%d: ",tt)
#define ln printf("\n")

void Print(auto T){  for(auto x : T){ cout << x << " ";  } }
ll Dist[1005],Speed[1005];
LD Time(ll D,ll Dk,ll Sk){
    return (LD)(D-Dk)/(LD)Sk;
}
LD Solve(){
    ll D,N;
    ll Dk,Sk;
    LD Max = 0.000;
    cin >> D >> N;
    for(int i=0;i<N;i++){
        cin >> Dk >> Sk;
        Max = max(Max,Time(D,Dk,Sk));
    }

    return (LD)D/Max;
}
int main(){

    int T;
    cin >> T;
    for(int tt=1;tt<=T;tt++){
        CASE(tt);
        LD Res = Solve();
        printf("%.10Lf\n",Res);
    }
    return 0;
}
