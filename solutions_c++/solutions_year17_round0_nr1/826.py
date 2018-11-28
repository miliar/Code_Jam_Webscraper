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
		string str;
		int k;
		cin>>str>>k;
		int n=str.length(), cnt=0;
		for(int i=0; i<n; i++){
			if(str[i]=='-'){
				if(n-i>=k){
					for(int j=i; j<i+k; j++){
						if(str[j]=='-') str[j]='+';
						else str[j]='-';
					}
					cnt++;
				}
			}
		}
		bool h=true;
		for(int i=0; i<n; i++){
			if(str[i]=='-'){
				h=false;
				break;
			}
		}
		if(h) cout<<"Case #"<<z<<": "<<cnt<<endl;
		else cout<<"Case #"<<z<<": IMPOSSIBLE"<<endl;
	}
}