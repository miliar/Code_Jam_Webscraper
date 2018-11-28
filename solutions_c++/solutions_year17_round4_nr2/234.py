#include <bits/stdc++.h>

using namespace std;

#define pb push_back
typedef long long LL;
int n,c,m;
int p[1100],b[1100];
int cntBuyer[1100], cntSeater[1100];

bool good(int x){
	int carry=0;
	for(int i=1; i<=n; i++){
		if( cntSeater[i] - carry > x  ) return false;
		carry = x - (cntSeater[i] - carry);
	}
	return true;
}

int attempt(int x){
	int res = 0;
	for(int i=1; i<=n; i++){
		if( cntSeater[i] > x  ) res +=  cntSeater[i] - x;
	}
	return res;
}

void solve(int test){
	cout << "Case #" << test + 1 << ": ";
	memset(cntBuyer,0,sizeof cntBuyer);
	memset(cntSeater,0,sizeof cntSeater);
	cin>> n >> c >> m;
	for(int i=0; i<m; i++){
		cin >> p[i] >> b[i];
		cntBuyer[b[i]]++;
		cntSeater[p[i]]++;
	}
	int low =0, high = m;
	for(int i=1; i<=c; i++){
		low = max(low,cntBuyer[i]);
	}	
	for(int i=0; i<100; i++){
		int mid = (low+high)/2;
		if(good(mid)) high = mid;
		else{
			low = mid;
		}
	}
	if(!good(low)) low++;
	cout << low <<" " << attempt(low) << endl;
}

int ntest;
int main(){
	freopen("B-large.in","r",stdin);
	//freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	cin >> ntest;
	for(int test=0; test<ntest; test++){
		solve(test);
	}
	return 0;
}
