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
#define ff first
#define ss second
#define mp make_pair
#define pb push_back

typedef unsigned int uint;
typedef long long int64;
typedef unsigned long long uint64;
#define CASE(tt) printf("Case #%d: ",tt)
#define ln printf("\n")
string Solve(){
    int N;
    int R,O,Y,G,B,V;
    cin >> N;
    cin >> R >> O >> Y >> G >> B >> V;
    vector< pair<int,char> > Arr {mp(R,'R'),mp(Y,'Y'),mp(B,'B')};
    sort(Arr.begin(),Arr.end());
    string res(N,'0');
    if(R>N/2 || Y>N/2 || B>N/2)
        return "IMPOSSIBLE";
    int r=Arr[0].ff+Arr[1].ff;
    int l=r-Arr[2].ff,idx=0;
    bool ok = true;
    string Res(N,'0');
    while(l--)
    {
        if(ok){
            Res[idx++] = Arr[1].second;
            Arr[1].ff--;
            ok=0;
        }
        else{
            Arr[0].ff--;
            Res[idx++] = Arr[0].ss;
            ok=1;
        }
    }
    //cout << Arr[0].ff << " " << Arr[0].ss << endl;
    //cout << Arr[1].ff << " " << Arr[1].ss << endl;
    //cout << Arr[2].ff << " " << Arr[2].ss << endl;
    for(int i=1;i<=Arr[2].ff;i++){
        Res[idx++] = Arr[2].ss;
        if(Arr[1].ff==0)
            Res[idx++] = Arr[0].ss;
            else
        {
            Res[idx++] = Arr[1].ss;
            Arr[1].ff--;
        }
    }
    return Res;
}
int main(){

    int T;
    cin >> T;
    for(int tt=1;tt<=T;tt++){
        CASE(tt);
        string Res = Solve();
        cout << Res << endl;
    }
    return 0;
}
