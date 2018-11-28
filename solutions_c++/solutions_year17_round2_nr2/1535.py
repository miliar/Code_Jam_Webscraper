#include<iostream>
#include<string>
#include<fstream>
using namespace std;

int n, r, o, y, g, b, v;
		
int f1(string &res){
	while(o > 0){
		if(b == 0)
			return 0;
		b--;
		res += 'B';
		res += 'O';
		o--;
	}
	if(res.length() > 0 && res.length() < n){
		if(b == 0)
			return 0;
		b--;
		res += 'B';
	}
	while(g > 0){
		if(r == 0)
			return 0;
		r--;
		g--;
		res += "RG";
	}
	if(res.length() > 0 && res[0] == 'B' && res[res.length() - 1] == 'G'){
		if(r == 0)
			return 0;
		r--;
		res += "R";
	}
	while(v > 0){
		if(y == 0)
			return 0;
		y--;
		v--;
		res += "YV";
	}
	if(res.length() > 0 && res[res.length() - 1] == 'V' && res[0] != 'Y'){
		if(y == 0)
			return 0;
		y--;
		res += 'Y';
	}
	return 1;
}

int f2(string &res){
	int k[3];
	k[0] = r;
	k[1] = b;
	k[2] = y;
	string s = "RBY";
	int m1 = -1, m2 = -1, m3 = -1;
		for(int i = 0; i < 3; i++){
			if(m1 == -1 || k[i] >= k[m1]){
				m3 = m2;
				m2 = m1;
				m1 = i;
			}else if(m2 == -1 || k[i] >= k[m2]){
				m3 = m2;
				m2 = i;
			}else if(m3 == -1 || k[i] >= k[m3])
				m3 = i;
		}
	if(res.length() == 0){
		for(int i = 0; i < k[m1]; i++){
			res += s[m1];
			if(k[m2] > 0){
				res += s[m2];
				k[m2]--;
			}else if(k[m3] > 0){
				res += s[m3];
				k[m3]--;
			}else{
				return 0;
			}
		}
		for(int i = 0; i < k[m3]; i++){
			res = res.substr(0, 2 * i + 1) + s[m3] + res.substr(2 * i + 1);
		}
		return 1;
	}
	return 1;
}

int main(){
	int t;
    freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);

	cin >> t;
	for(int i = 0 ;i < t; i++){
		
		cin >> n >> r >> o >> y >> g >> b >> v;
		string ans = "";
		if(f2(ans) == 0)

			cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << i + 1 << ": " << ans << endl;
	}
	return 0;
}