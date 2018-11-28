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
int n,m;
string str;

int bitt[1005];
void update(int x, int v){
    repp(i,x,n,i&-i)bitt[i] += v;
}
int query(int x){
    int ret = 0;
    revv(i,x,1,i&-i)ret += bitt[i];
    return ret;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin>>t;
    rep(z,1,t){
        cin>>str>>m;
        n = str.size();

        rep(i,1,n)bitt[i] = 0;
        if(str[0] == '-')update(1,1);
        rep(i,1,n-1){
            if(str[i] == '-' && str[i-1] == '+')update(i+1,1);
            else if(str[i] == '+' && str[i-1] == '-')update(i+1,-1);
        }
//        rep(i,1,n)cout<<query(i);cout<<endl;

        int cnt = 0;
        rep(i,0,n-m){
            if(query(i+1) % 2 == 1){
                cnt++;
                update(i+1,1);
                update(i+m+1,-1);
            }
        }

        bool possible = true;
        rep(i,n-m+1,n-1){
            if(query(i+1) % 2 == 1){
                possible = false;
                break;
            }
        }
//        rep(i,1,n)cout<<query(i);cout<<endl;

        cout<<"Case #"<<z<<": ";
        if(possible)cout<<cnt<<endl;
        else cout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
