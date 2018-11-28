#include <bits/stdc++.h>

#define i64 long long
#define u64 unsigned long long
#define i32 int
#define u32 unsigned int

#define pii pair<int, int>
#define pll pair<long long, long long>

#define ld long double
#define defmod 1000000007

#define mati64(a,b) vector<vector<i64>>(a, vector<i64>(b, 0));
using namespace std;

unordered_map<int, string> d[3][3][1001][1001];
string fail = "-1";
string hae(int n, int ek, int la, int r, int y, int b){
	//cout << "taalla " << r << " " << y << " " << b << endl;
	if(n == 0)
		return "";
	if(d[ek][la][r][y].count(b))
		return d[ek][la][r][y][b];
	if(n == 1){
		if(r){
			if(ek == 0 || la == 0)
				return "-1";
			return "R";
		}
		else if(y){
			if(ek == 1|| la == 1)
				return "-1";
			return "Y";
		}
		else if(b){
			if(ek == 2 || la == 2)
				return "-1";
			return "B";
		}
	}
	if(la == 0){
		if(y+b == 0)
			return fail;
		string ans = fail;
		if(y){
			ans = hae(n-1, ek, 1, r, y-1, b);
			if(ans.compare(fail) != 0)
				ans = ans+'Y';
		}
		if(b && ans.compare(fail) == 0){
			ans = hae(n-1, ek, 2, r, y, b-1);
			if(ans.compare(fail) != 0)
				ans = ans+'B';
		}
		
		d[ek][la][r][y][b] = ans;
	}
	if(la == 1){
		if(r+b == 0)
			return fail;
		string ans = fail;
		if(r){
			ans = hae(n-1, ek, 0, r-1, y, b);
			if(ans.compare(fail) != 0)
				ans = ans+'R';
		}
		if(b && ans.compare(fail) == 0){
			ans = hae(n-1, ek, 2, r, y, b-1);
			if(ans.compare(fail) != 0)
				ans = ans+'B';
		}
		
		d[ek][la][r][y][b] = ans;
	}

	if(la == 2){
		if(y+r == 0)
			return fail;
		string ans = fail;
		if(y){
			ans = hae(n-1, ek, 1, r, y-1, b);
			if(ans.compare(fail) != 0)
				ans = ans+'Y';
		}
		if(r && ans.compare(fail) == 0){
			ans = hae(n-1, ek, 0, r-1, y, b);
			if(ans.compare(fail) != 0)
				ans = ans+'R';
		}
		
		d[ek][la][r][y][b] = ans;
	}

	return d[ek][la][r][y][b];
}
void solve1(){
	int n, r, o, y, g, b, v;
	cin >> n >> r >> o >> y >> g >> b >> v;

	string ans = "IMPOSSIBLE";
	
	if(r)
		ans = 'R'+hae(n-1, 0, 0, r-1, y, b);
	else if(y)
		ans = 'Y'+hae(n-1, 1, 1, r, y-1, b);
	else if(b)
		ans = 'B'+hae(n-1, 2, 2, r, y, b-1);

	if(ans.compare('R'+fail) == 0||ans.compare('Y'+fail) == 0||ans.compare('B'+fail) == 0)
		cout << "IMPOSSIBLE" << endl;
	else
		cout << ans << endl;

}

int main(){
	srand(time(0));
	cin.sync_with_stdio(0);
	cin.tie(0);
	
	int tests;
	cin >> tests;
	for(int i = 1; i <= tests; ++i){
		cout << "Case #" << i << ": ";
		solve1();
	}
	return 0;
}
