#include <bits/stdc++.h>
using namespace std;

#define ll long long

vector<int> V;

bool allowed(int index, int x){
	for(int i = index; i < V.size(); i++){
		if(V[i] > x)	return true;
		else if(V[i] < x)	return false;
	}
	return true;
}

void solve(){

	V.clear();

	ll n, ans = 0;
	cin>>n;

	while(n){
		V.push_back(n % 10);
		n /= 10;
	}

	reverse(V.begin(), V.end());

	bool all9s = false;

	for(int i = 0; i < V.size(); i++){
		if(all9s == true){
			ans *= 10LL;
			ans += 9;
			continue;
		}
		for(int j = 9; j >= 0; j--){
			if(allowed(i, j)){
				ans *= 10;
				ans += j;
				if(V[i] > j)	all9s = true;
				break;
			}
		}
	}

	cout<<ans<<endl;
}

int main(){
	int t;
	cin>>t;
	for(int big = 1; big <= t; big++){
		cout<<"Case #"<<big<<": ";
		solve();
	}
}