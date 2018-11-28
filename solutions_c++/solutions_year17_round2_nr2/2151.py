#include<bits/stdc++.h>

using namespace std;


void raspored(int a, char ca, int b, char cb, int c, char cc) {
	string v[a];
	int i;
	for (i = 0; i < a; i++){
		v[i] = "";
		v[i] += ca;
	}
	i = 0;
	while (b){
		v[i] += cb;
		b--;
		i++;
		i %= a;
	}
	while (c){
		v[i] += cc;
		c--;
		i++;
		i %= a;
	}
	for (i = 0; i < a; i++){
		cout << v[i];
	}
	cout << endl;
}

int main(){
	int n, r, o, y, g, b, v, t;
	cin >> t;
	for (int c = 1; c <= t; c++) {
		cin >> n >> r >> o >> y >> g >> b >> v;
		if (max(r, max(y, b)) > r + y + b - max(r, max(y, b))) {
				cout << "Case #"<<c<<": IMPOSSIBLE" << endl;
			continue;
		}
		//cout << r << ' ' << y << ' '<< b << endl;
		cout << "Case #"<<c<<": ";
		if (r >= y && r >= b){
			raspored(r, 'R', y, 'Y', b, 'B');
			continue;
		}
		if (y >= r && y >= b){
			raspored(y, 'Y', r, 'R', b, 'B');
			continue;
		}
		if (b >= y && b >= r){
			raspored( b, 'B', r, 'R', y, 'Y');
			continue;
		}
	}	
	return 0;
}
