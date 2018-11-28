#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <cstring>
#include <map>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <bitset>
#define f first
#define s second
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define pb push_back
#define vi vector <int>
#define ld long double
#define pii pair<int, int>
using namespace std;    
const int N = int(3e5), mod = int(1e9)  + 7;
int T,r,o,y,g,b,v;

void solve(){
	int k;
	scanf("%d",&k);
	scanf("%d%d%d%d%d%d",&r,&o,&y,&g,&b,&v);
	if(b == o && o > 0){
		if(k == b + o){
			for(int i = 1; i <= b; i++){
				printf("BO");
			}
			return;
		}
		puts("IMPOSSIBLE");
		return;
	}
	if(g == r && r > 0){
		if(k == g + r){
			for(int i = 1; i <= g; i++){
				printf("GR");
			}
			return;
		}
		puts("IMPOSSIBLE");
		return;
	}
	if(v == y && y > 0){
		if(k == v + y){
			for(int i = 1; i <= v; i++){
				printf("VY");
			}
			return;
		}
		puts("IMPOSSIBLE");
		return;
	}
	if((b <= o && o > 0) || (r <= g && g > 0) || (y <= v && v > 0)){
		puts("IMPOSSIBLE");
		return;
	}
	b -= o;
	r -= g;
	y -= v;
	int n = b + r + y;
	int mx = max(b, max(r,y));
	string ans = "";
	if(mx > n / 2 && (mx > 1)){
		puts("IMPOSSIBLE");
		return;
	}
	if(b == mx){
		while(b > 0){
			ans += 'B';
			b--;
			if(r >= y){
				r--;
				ans += 'R'; 
			}
			else{
				y--;  
				ans += 'Y';
			}
		}
		while(r + y > 0){
			if(r >= y){
				r--;
				ans += 'R';
			}
			else{
				y--;
				ans += 'Y';
			}
		}
	}
	else if(r == mx){
		while(r > 0){
			ans += 'R';
			r--;
			if(b >= y){
				b--;
				ans += 'B'; 
			}
			else{
				y--;  
				ans += 'Y';
			}
		}
		while(b + y > 0){
			if(b >= y){
				b--;
				ans += 'B';
			}
			else{
				y--;
				ans += 'Y';
			}
		}
	}
	else{
		while(y > 0){
			ans += 'Y';
			y--;
			if(r >= b){
				r--;
				ans += 'R'; 
			}
			else{
				b--;  
				ans += 'B';
			}
		}
		while(r + b > 0){
			if(r >= b){
				r--;
				ans += 'R';
			}
			else{
				b--;
				ans += 'B';
			}
		}
	}
	if(o > 0){
		string os = "";
		for(int i = 0; i < o; i++){
			os += "OB";
		}
		string cur = "";
		for(int i = 0; i < ans.size(); i++){
			cur += ans[i];
			if(ans[i] == 'B'){
				cur += os;
				for(int j = i + 1; j < ans.size(); j++){
					cur += ans[j];
				}
				break;
			}
		}
		ans = cur;
	}
	if(g > 0){
		string os = "";
		for(int i = 0; i < g; i++){
			os += "GR";
		}
		string cur = "";
		for(int i = 0; i < ans.size(); i++){
			cur += ans[i];
			if(ans[i] == 'R'){
				cur += os;
				for(int j = i + 1; j < ans.size(); j++){
					cur += ans[j];
				}
				break;
			}
		}
		ans = cur;
	}
	if(v > 0){
		string os = "";
		for(int i = 0; i < o; i++){
			os += "VY";
		}
		string cur = "";
		for(int i = 0; i < ans.size(); i++){
			cur += ans[i];
			if(ans[i] == 'Y'){
				cur += os;
				for(int j = i + 1; j < ans.size(); j++){
					cur += ans[j];
				}
				break;
			}
		}
		ans = cur;
	}
	if(ans.size() != k) cerr << "bad\n";
	cout << ans << endl;
}

int main () {
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++){
		printf("Case #%d: ",tt);
		solve();
	}

return 0;
}