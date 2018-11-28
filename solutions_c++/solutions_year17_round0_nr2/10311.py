#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

bool tidy(ll n){
	while(n>9){
		int x, y;
		x=n%10;
		y=(n%100)/10;
		if(y>x)
			return false;
		n/=10;	
	}
	return true;
}

int main(){
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int t;
	cin >> t;
	for(int i=0; i<t; i++){
		ll x;
		cin >> x;
		while(tidy(x) == false)
			x--;
		
		cout << "Case #" << i+1 << ": " << x << "\n";	
	}
	
	return 0;		
}
