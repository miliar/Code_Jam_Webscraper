#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<string>
#include<algorithm>

#define pb push_back
#define ll long long
#define REP(a,b) for(int(a)=0;(a)<(b); (a)++)
using namespace std;




void solve(int test){
	ll n, t;
	cerr<<t<<endl;
	scanf("%lli%lli",&n,&t);

	vector<ll> hp;
	hp.pb(n);
	make_heap(hp.begin(), hp.end());
	int fr;
	REP(a,t-1){
		fr = hp.front();
		pop_heap(hp.begin(), hp.end());
		hp.pop_back();
		if(fr %2 ==1){
			hp.pb(fr/2); push_heap(hp.begin(), hp.end());
			hp.pb(fr/2); push_heap(hp.begin(), hp.end());
		}else{
			hp.pb(fr/2); push_heap(hp.begin(), hp.end());
			hp.pb(fr/2-1); push_heap(hp.begin(), hp.end());
		}
	}
	fr = hp.front();
	ll lv,pr;
		if(fr %2 ==1){
			lv = fr/2;
			pr = fr/2;
		}else{
			lv = fr/2;
			pr = fr/2-1;
		}

	printf("Case #%i: %lli %lli\n",test, lv, pr);
	

			

}


int main(){
	int t;
	scanf("%i",&t);
	REP(a,t) solve(a+1);
	return 0;
}
