#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N = 100000 + 10;
const int M = 1000000007;
const double PI = atan(1) * 4;
const int oo = 1000000000;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
#define pb push_back 
#define all(c) (c).begin(),(c).end()
int n,k;
struct range{
	int l,r;
	range(){}
	range(int a, int b){
		l=a;r=b;
	}
	bool operator<(const range &e)const{
		if(r-l==e.r-e.l)
			return l<e.l;
		return r-l<e.r-e.l;
	}
};
set<range>st;
int main(){
	#ifndef ONLINE_JUDGE
		freopen("C-small-2-attempt0.in", "r", stdin);
		freopen("output.txt","w",stdout);
	#endif
	int T;
	cin>>T;
	int t=1;
	while(T--){
		cin>>n>>k;
		st.clear();
		st.insert(range(1,n));
		while(--k){
			range p=*--st.end();
			st.erase(--st.end());
			int l=p.l,r=p.r;
			int md=(l+r)/2;
			if(l<md)
				st.insert(range(l,md-1));
			if(r>md)
				st.insert(range(md+1,r));
		}
		cout<<"Case #"<<t++<<": ";
		int l=(*--st.end()).l;
		int r=(*--st.end()).r;
		int md=(l+r)/2;
		l=md-l;
		r=r-md;
		cout<<max(l,r)<<" "<<min(l,r)<<endl;
	}
	
}


