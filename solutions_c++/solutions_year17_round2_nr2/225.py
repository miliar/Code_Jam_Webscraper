#include <bits/stdc++.h>

using namespace std;

string ans, o, g, v;

void choose(int &x, char xc, int &y, char yc){
	if (x > y){
		ans.push_back(xc);
		x--;
	}
	else if (x < y){
		ans.push_back(yc);
		y--;
	}
	else{
		if (ans.front() == xc){
			ans.push_back(xc);
			x--;
		}
		else{
			ans.push_back(yc);
			y--;
		}
	}
}

void solve(int n, int r, int ry, int y, int yb, int b, int rb){
	while (r or y or b){
		if (ans.back() == 'R'){
			if (!y and !b){
				break;
			}

			choose(y, 'Y', b, 'B');
		}
		else if (ans.back() == 'Y'){
			if (!r and !b){
				break;
			}

			choose(r, 'R', b, 'B');
		}
		else if (ans.back() == 'B'){
			if (!r and !y){
				break;
			}

			choose(r, 'R', y, 'Y');
		}
	}
}

bool check(int n, int r, int ry, int y, int yb, int b, int rb){
	int x;

	solve(n, r, ry, y, yb, b, rb);

	if ((int)ans.size() != r + y + b + 1 or ans.front() == ans.back()){
		return false;
	}

	if (o.size()){
		x = find(ans.begin(), ans.end(), 'B') - ans.begin();

		if (x == (int)ans.size()){
			return false;
		}

		ans = ans.substr(0, x) + o + ans.substr(x);
	}

	if (v.size()){
		x = find(ans.begin(), ans.end(), 'Y') - ans.begin();

		if (x == (int)ans.size()){
			return false;
		}

		ans = ans.substr(0, x) + v + ans.substr(x);
	}

	if (g.size()){
		x = find(ans.begin(), ans.end(), 'R') - ans.begin();

		if (x == (int)ans.size()){
			return false;
		}

		ans = ans.substr(0, x) + g + ans.substr(x);
	}

	return true;
}

int main(){
	int n, r, ry, y, yb, b, rb, tc, ic;

	ios::sync_with_stdio(false);

	cin >> tc;
	
	for (ic = 1; ic <= tc; ic++){
		cin >> n >> r >> ry >> y >> yb >> b >> rb;

		if ((ry and b < ry) or (rb and y < rb) or (yb and r < yb)){
			cout << "Case #" << ic << ": IMPOSSIBLE" << endl;
			continue;
		}

		ans = o = v = g = "";

		// Orange = RY
		while (ry){
			o += "BO";
			b--;
			ry--;
		}

		// Violet = RB
		while (rb){
			v += "YV";
			y--;
			rb--;
		}

		// Green = YB
		while (yb){
			g += "RG";
			r--;
			yb--;
		}

		if (r){
			ans = "R";
			r--;

			if (check(n, r, ry, y, yb, b, rb)){
				cout << "Case #" << ic << ": " << ans << endl;
				continue;
			}

			r++;
		}

		if (y){
			ans = "Y";
			y--;

			if (check(n, r, ry, y, yb, b, rb)){
				cout << "Case #" << ic << ": " << ans << endl;
				continue;
			}

			y++;
		}

		if (b){
			ans = "B";
			b--;

			if (check(n, r, ry, y, yb, b, rb)){
				cout << "Case #" << ic << ": " << ans << endl;
				continue;
			}

			b++;
		}

		if ((int)o.size() == n or (int)v.size() == n or (int)g.size() == n){
			ans = o + v + g;
			cout << "Case #" << ic << ": " << ans << endl;
		}
		else{
			cout << "Case #" << ic << ": IMPOSSIBLE" << endl;
		}
	}

	return 0;
}