#include <bits/stdc++.h>
#define FIO ios_base::sync_with_stdio(0)
#define all(X) X.begin(),X.end()
#define rall(X) X.rbegin(),X.rend()
#define FOR(a,n) for(long long int  a=0;a<n;a++)
#define FORI(a,b,c) for(long long int a=b;a<=c;a++)
#define FORD(a,b,c) for(long long int a=b;a>=c;a--)
#define ITER(a,b) for(auto &a : b)
#define INC(a,b,c,d) for(long long int a=b;a<=c;a+=d)
#define DEC(a,b,c,d) for(long long int a=b;a>=c;a-=d)

#define SORT(a) sort(all(a))
#define RSORT(a) sort(rall(a))
#define MP make_pair
#define PB push_back
#define PF push_front
#define DB pop_back
#define DF pop_front
#define cx first
#define cy second
#define MOD 1000000000+7
#define MADD(a,b) (a+b>=M):a+b-MOD?a+b
#define MDEC(a,b)  MADD(a-b,MOD)


using namespace std;
typedef long long int ll;
typedef long double ld;
typedef pair<ld,ld> point;
typedef pair<point,point> line;

/****** Geometry*****/

pair<bool,point> intersection(line a,line b){
	ld A1 = a.cy.cy - a.cx.cy;
	ld B1 = a.cx.cx - a.cy.cx;
	ld A2 = b.cy.cy - b.cx.cy;
	ld B2 = b.cx.cx - b.cy.cx;
	ld C1 = A1*a.cx.cx + B1*a.cx.cy;
	ld C2 = A2*b.cx.cx + B2*b.cx.cy;
	ld det = A1*B2 - B1*A2;
	if(det==0.0)
		return {false,{{0.0},{0.0}}};
	else return {true,{(B2*C1-B1*C2)/det,(A1*C2-C1*A2)/det}};


}

/****** Geo-End *****/

/******** Math based Functions ******/
ll binpow(ll a, ll b, ll c)
{
    ll r =1 ;
    while (b)
    {
        if (b&1) r*=a;
        a*=a;
        r%=c;
        a%=c;
        b>>=1;
    }
    return r%c;
}

ll inverse(ll a, ll m)
{
    return binpow(a, m-2, m);
}
/*** Math Section Ends***/
class prio{
public:
    bool operator()(pair<ll,ll> a,pair<ll,ll> b){
        return ((a.cy-a.cx+1)-2) < ((b.cy-b.cx+1)-2);
    }
};
priority_queue<pair<ll,ll>,vector<pair<ll,ll> >,prio > Q;
int main()
{
	#ifndef ONLINE_JUDGE
          freopen("in.txt","r",stdin);
          freopen("out.txt","w",stdout);
     #endif
	ll t;
	cin>>t;
	FORI(w,1,t){
		ll n,k,_k=1;
		cin>>n>>k;
		Q.push({1,n+2});
		while(!Q.empty()){

			pair<ll,ll> cur;
			cur = Q.top();
			if(_k==k){
				/*
                    ll ans1 = INT_MIN,ans2= INT_MAX;
                    while(!Q.empty())
                        ans1 = max(ans1,Q.top().second-Q.top().first-1),
                        ans2 = min(ans2,Q.top().second-Q.top().first-1),
                        Q.pop();
                cout<<ans1<<" "<<ans2<<endl;
			 */
			 	ll m = (Q.top().cx+Q.top().cy)/2;
				cout<<"Case #"<<w<<": "<<max(m-Q.top().cx-1,Q.top().cy-m-1)<<" "<<min(m-Q.top().cx-1,Q.top().cy-m-1)<<endl;
				while(!Q.empty())Q.pop();
				break;
			}
			Q.pop();
			ll m  = abs(cur.second+cur.first)/2;

			Q.push({cur.first,m});
			Q.push({m,cur.second});
			_k++;

		}
	}


    return 0;
}
