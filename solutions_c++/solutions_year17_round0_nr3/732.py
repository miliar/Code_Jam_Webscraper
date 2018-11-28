#include <bits/stdc++.h>
#define LL long long
#define pb push_back
#define mp make_pair
#define fi first
#define sc second
using namespace std;

LL T,n,m,x,y;

void solve(LL a, LL b, LL cntA, LL cntB, LL sum, LL num){
//	cout<<endl<<a<<" "<<b<<" "<<cntA<<" "<<cntB<<" "<<sum<<" "<<num<<endl;
	if(num<=sum){
		LL lowBound = sum/2;
		num -= lowBound;
		if(num<=cntA) x = a;
		else x = b;
		if(cntA>(cntA+cntB)/2 && cntA-(cntA+cntB)/2>=num) y = a;
		else y = b;
		cout<<x<<" "<<y<<endl;
		return;
	}
	x = y = 0;
	if(a%2==0){
		x += cntA;
		y += cntA;
	}
	else{
		y += cntA*2;
	}
	if(b%2==0){
		x += cntB;
		y += cntB;
	}
	else{
		y += cntB*2;
	}
	if(b%2==0) solve(b/2, b/2-1, y, x, sum*2+1, num);
	else solve(b/2+1, b/2, x, y, sum*2+1, num);
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>T;
	for(int tc=1;tc<=T;tc++){
		cin>>n>>m;
		printf("Case #%d: ", tc);
		if(n%2==0) solve(n/2, n/2-1, 1, 1, 1, m);
		else solve(n/2, n/2, 1, 1, 1, m);
	}
	return 0;
}
