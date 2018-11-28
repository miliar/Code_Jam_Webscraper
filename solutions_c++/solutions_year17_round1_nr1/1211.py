#include <bits/stdc++.h>
#include <unordered_map>
#include <unordered_set>

#define pb push_back
#define mkp make_pair
#define bgn begin()
#define end end()
#define all(x) x.bgn,x.end
#define itr(x) x::iterator
#define fst first
#define scd second
#define dlt pop()

using namespace std;

typedef long long int ll;
typedef vector<int> vint;
typedef vector<ll> vlong;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef map<int,int> mii;
typedef map<ll,ll> mll;
typedef queue<int> qint;
typedef queue<ll> qlong;
typedef stack<int> sint;
typedef stack<ll> slong;
typedef queue<pii> qpii;
typedef stack<pii> spii;
typedef vector<pii> vpii;

int mod = 1e9+7;
int NN = 1e6+7;

ll gcd(ll a, ll b){
	return b==0 ? a : gcd(b,a%b);
}

// (1/b)%a where gcd(a,b)=1
ll invmod(ll a, ll b){
	ll x=0, y=1, r, q, m=a;
	while(b){
		r=a%b;
		q=a/b;
		a=b;
		b=r;
		r=x;
		x=y;
		y=r-q*y;
	}
	return (x+m)%m;
}

int main(){
	int t;
	cin>>t;
	for(int z=1; z<=t; z++){
		int r, c;
		cin>>r>>c;
		string str[r];
		for(int i=0; i<r; i++) cin>>str[i];

		for(int i=0; i<r; i++){
			vector<pii> rr;
			for(int j=0; j<c; j++){
				if(str[i][j]!='?'){
					rr.push_back(mkp(j,str[i][j]));
				}
			}

			if(rr.size()){
				for(int j=0; j<rr.size(); j++){
					for(int k=rr[j].fst-1; k>=0; k--){
						if(str[i][k]!='?'){
							break;
						}
						else str[i][k]=rr[j].scd;
					}

					for(int k=rr[j].fst+1; k<c; k++){
						if(str[i][k]!='?'){
							break;
						}
						else str[i][k]=rr[j].scd;
					}
				}
			}
			else{
				if(i>0){
					for(int j=0; j<c; j++){
						str[i][j]=str[i-1][j];
					}
				}
			}
		}

		cout<<"Case #"<<z<<":"<<endl;
		for(int i=r-1; i>0; i--){
			for(int j=0; j<c; j++){
				if(str[i-1][j]=='?'){
					str[i-1][j]=str[i][j];
				}
			}
		}

		for(int i=0; i<r; i++) cout<<str[i]<<endl;
	}
}