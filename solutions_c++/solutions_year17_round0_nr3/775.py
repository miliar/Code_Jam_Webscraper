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
ll n,k;

int main(){
    ios_base::sync_with_stdio(0);
    cin>>t;
    rep(z,1,t){
        cin>>n>>k;

        ll pow2 = 1;
        ll seg = n;
        ll cnta = 1,cntb = 0;
        while(k){
            if(k<=pow2){
                if(k <= cntb){
                    seg++;
                }
                k = 0;
            }else{
                k -= pow2;
                pow2 <<= 1;

                if(seg&1){
                    cnta <<= 1;
                    cnta += cntb;
                }else{
                    cntb <<= 1;
                    cntb += cnta;
                }
                seg = (seg-1)/2;
            }
            //printf(">> %lld seg %lld, %d %d\n",k,seg,cnta,cntb);
        }
        cout<<"Case #"<<z<<": "<<seg/2<<" "<<(seg-1)/2<<endl;
    }
    return 0;
}
