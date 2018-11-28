#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

int ntest;
LL n,k;
void solve(int test){
	cout << "Case #" << test+1 << ": ";
	cin >> n >> k;
	int i = 1;
	while( (1LL<<i) <= k ) i++;
	i--;
	LL already = (1LL<<i) - 1;
	LL ppRM = k - already;
	LL slotSz =  (n-already)/(already+1) ;
	LL nUp = (n-already)%(already+1);	
	if( ppRM <= nUp ){
		LL sz = (slotSz+1);
		if( sz&1) cout << (sz-1)/2  << " " << (sz-1)/2 << endl;
		else cout << (sz-1)/2+1  << " " << (sz-1)/2 << endl;
	}else{
		LL sz = slotSz;
		if( sz&1) cout << (sz-1)/2  << " " << (sz-1)/2 << endl; 
		else cout << (sz-1)/2+1  << " " << (sz-1)/2 << endl;
	}	
}

int main(){
	freopen("C-large.in","r",stdin);
	freopen("test.out","w",stdout);
	cin >> ntest;
	for(int test=0; test<ntest; test++){
		solve(test);
	}
	return 0;
}
