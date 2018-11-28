#include "bits/stdc++.h"
using namespace std;
#define ll long long
#define sz(a) 			    (int) a.size()
#define all(a) 				a.begin(), a.end()
vector<int> fkk;
int k;
void flip(int a){
	for(int i = 0 ; i < k ; ++i){
		fkk[a] = (fkk[a]? 0 : 1);
		a++; 
	}
}
bool check(){
	for(int i = 0; i < sz(fkk); ++i){
		if(!fkk[i])
			return false;
	}
return true;
}
int main(){
	#ifdef KP
		freopen("a.in","r",stdin);
		freopen("a.out","w",stdout);
	#endif
	int ncases = 1;
	cin >> ncases;
	for(int icase = 1; icase <= ncases; ++icase){
	cout << "Case #" << icase << ": ";
		string one;
		cin >> one;
		cin >> k;
		fkk.clear();
		fkk.resize(sz(one));
		int ans=0;
		for(int i = 0; i < sz(fkk); ++i)
			fkk[i] = (one[i]=='+');
		for(int i = 0; i <= sz(fkk)-k; ++i){
			if(!fkk[i]){
				flip(i);
				ans++;
			}
		}
	if(check())			
		cout << ans << endl;
	else
		cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}