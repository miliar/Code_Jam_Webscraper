#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <deque>
#include <assert.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <stdio.h>
#include <string.h>
#include <utility>
#include <math.h>
#include <bitset>
#include <iomanip>

using namespace std;

#define F(i , a , b) for(int (i) = (a) ; (i) <= (b) ; (i)++)
#define pb push_back
#define ll long long
#define E(a) cerr << #a << " = " << a << '\n'
#define X first
#define Y second
#define INF 10000000000000
#define int long long
const int MAX_N = 100000 + 10 , mod = 1000000007;

void solve(){
	vector<pair<pair<int,int>,int>  > v;
	vector<int> va,vb;
	int n , ac, aj , x , y , ta = 720  , tb = 720 , ans=1; cin >> ac >> aj;

	for(int i =0 ; i<ac ; i++){
		cin >> x >> y;
		v.pb({ {x,y}  ,  'A'});
		ta -= y-x; 
	}
	for(int i =0 ; i<aj ; i++){
		cin >> x >> y;
		v.pb({ {x,y}  ,  'B'});
		tb -= y-x;
	}
	sort(v.begin() , v.end());

	for(int i =0 ;i<(int)v.size()-1 ; i++){
		if(v[i].Y == v[i+1].Y){
			if(v[i].Y == 'A'){
				va.pb(v[i+1].X.X - v[i].X.Y);
			}
			else{
				vb.pb(v[i+1].X.X - v[i].X.Y);
			}
			ans += 2;
		}
		else{
			ans ++;
		}

	}

	ans += 2;
	E(ans);
	sort(va.begin() , va.end());
	sort(vb.begin() , vb.end());
	for(auto i : va){
		if(ta >= i){
			ta -= i;
			ans -= 2;
		}
	}
	for(auto i : vb){
		if(tb >= i){
			tb -= i;
			ans -= 2;
		}
	}	
	char c1 = v[0].Y;
	char c2 = v[v.size()-1].Y;

	if(v[0].Y == 'A'){
		if(ta >= v[0].X.X) ta -= v[0].X.X , ans--;
		else c1 = 'B';
	}
	else{
		if(tb >= v[0].X.X) tb -= v[0].X.X , ans--;
		else c1 = 'A';
	}
	if(v[v.size()-1].Y == 'A'){
		if(ta >= 24*60-v[v.size()-1].X.Y) ta -= 24*60-v[v.size()-1].X.X , ans--;
		else c2 = 'B';
	}
	else{
		if(tb >= 24*60-v[v.size()-1].X.Y) tb -= 24*60-v[v.size()-1].X.X , ans--;
		else c2 = 'A';
	}
	if(c1 == c2) ans --;
	cout << ans <<  endl;
}
void clr(){

}

int32_t main(){
    
        freopen("input.txt" , "r" , stdin);
        freopen("output.txt" , "w" , stdout);
    //    cout << setprecision(10) << fixed;
    ios::sync_with_stdio(0); cin.tie() ; cout.tie();

    int T ; cin >> T;
    for(int _ = 1 ; _ <= T ; _++){
    	clr();
    	cout << "Case #" << _ << ": ";
    	solve();
    }
    
    
    return 0;
}
