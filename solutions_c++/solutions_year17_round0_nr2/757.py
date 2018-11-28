#include <iostream>
#include <cstdio>

#include <cstring>
#include <string>

#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>

#include <queue>
#include <utility>
#include <set>
#include <stack>
#include <vector>
#include <map>

#define YOU using
#define DONT namespace
#define SAY std

YOU DONT SAY;

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<ll,int> pli;
typedef pair<int,ll> pil;
typedef vector<int> vi;
typedef vector<pii> vii;
typedef vector<pll> vll;

#define repp(i,a,b,d) for(int i=a;i<=b;i+=d)
#define rep(i,a,b) repp(i,a,b,1)
#define revv(i,a,b,d) for(int i=a;i>=b;i-=d)
#define rev(i,a,b) revv(i,a,b,1)

#define mp make_pair

#define pb push_back
#define ff first
#define ss second

const int OO = 1e9;
const ll INF = 1e18;

const int irand(int lo,int hi){
	return ((double)rand()/(RAND_MAX + 1.0)) * (hi-lo+1) + lo;
}

const ll lrand(ll lo,ll hi){
	return ((double)rand()/(RAND_MAX + 1.0)) * (hi-lo+1) + lo;
}

//end of macro

int t;
ll n;

int main(){
    ios_base::sync_with_stdio(0);
    cin>>t;
    rep(z,1,t){
        cin>>n;
        int breakpos = 0;

        ll tmp = n;
        int lastdig = 9,cnt=0;;
        while(tmp){
            int dig = tmp%10;
            if(dig > lastdig){
                dig--;
                breakpos = cnt;
            }
            lastdig = dig;
            cnt++;
            tmp/=10;
        }

        rep(i,1,breakpos)n/=10;
        if(breakpos!=0)n--;

        cout<<"Case #"<<z<<": ";
        if(n>0)cout<<n;
        rep(i,1,breakpos)cout<<9;
        cout<<endl;
    }
    return 0;
}
