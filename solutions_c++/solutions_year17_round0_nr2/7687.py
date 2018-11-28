#include "bits/stdc++.h"
using namespace std;
typedef vector<int> VI;
#define sz(a) 			    (int) a.size()
#define all(a) 				a.begin(), a.end()
#define ll long long int
string num;

bool check(){
	for(int i = 1; i < sz(num); ++i){
		if(num[i] < num[i-1])
			return false;
	}
	return true;
}

void findnum(){
	for(int i = sz(num)-2 ; i >=0; --i){
		num[i]--;
		num[i+1] = '9';
		if(check())
			return;
	}
}

int main(){
	#ifdef KP
		freopen("b1.in","r",stdin);
		freopen("b1.out","w",stdout);
	#endif
	int ncases = 1;
	cin >> ncases;
	for(int icase = 1; icase <= ncases; ++icase){
	cout << "Case #" << icase << ": ";
		cin >> num;
		for(int i = sz(num)-1; i > 0; --i){
			if(num[i] >= num[i-1])
				continue;
			else{
				findnum();
		}
	}
		ll ans;
		ans = stoll(num);
		cout << ans << endl;
	}
	return 0;
}	