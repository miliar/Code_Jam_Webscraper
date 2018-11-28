#include <bits/stdc++.h>

#define REP(i, n) for(int i = 0; i < n; i++)

using namespace std;

typedef long double ld;
typedef long long ll;

int n;
int r, o, y, g, b, v;
int tc;


void print_multi(char a, char b, size_t n){
	REP(i, n)cout << a << b;
	cout << a;
}

bool check_special_case(int r, int g, int a, int b, int c, int d, char x, char y){
	if(r == g && r > 0){
		if(a > 0 || b > 0 || c > 0 || d > 0){
			cout << "Case #"<<tc<<": IMPOSSIBLE"<<endl;
		} else{
			cout << "Case #"<<tc<<": ";
			REP(i, r)cout << x << y;
			cout<<endl;
		}
		return true;
	}
	return false;
}

// r - g
// b - o
// y - v
void testcase(int tcn){
	tc = tcn;
	cin >> n >> r >> o >> y >> g >> b >>v;

	if(check_special_case(r, g, b, o, y, v, 'R', 'G'))return;
	if(check_special_case(b, o, r, g, y, v, 'B', 'O'))return;
	if(check_special_case(y, v, b, o, r, g, 'Y', 'V'))return;

	r-=g;
	b-=o;
	y-=v;

	n = r+b+y;

	if(r < 0 || b < 0 || y < 0 || r > n/2 || b > n/2 || y > n/2){
		cout << "Case #"<<tcn<<": IMPOSSIBLE"<<endl;
		return;
	}

	vector<pair<int, char>> abc = {{r, 'R'}, {b, 'B'}, {y, 'Y'}};
	sort(abc.begin(), abc.end(), [](auto && x, auto && y){return x.first > y.first;});

	vector<char> ret(n, abc[2].second);

	int x = abc[0].first;
	char c = abc[0].second;
	size_t i = 0;

	for(;x > 0; --x, i+=2){
		ret[i] = c;
	}

	x = abc[1].first;
	c = abc[1].second;

	for(;x > 0; --x, i+=2){
		if(i >= n)i=1;
		ret[i] = c;
	}



	bool okr = (g == 0);
	bool okb = (o == 0);
	bool oky = (v == 0);

	cout << "Case #"<<tcn<<": ";

	for(auto && c : ret){
		if(c == 'R' && !okr){
			print_multi('R', 'G', g);
			okr = true;
		} else if(c == 'B' && !okb){
			print_multi('B', 'O', o);
			okb = true;
		} else if(c == 'Y' && !oky){
			print_multi('Y', 'V', v);
			oky = true;
		} else {
			cout << c;
		}
	}

	cout << endl;

}

int main(){
	int T;
	cin >> T;
	REP(i, T){
		testcase(i+1);
	}
	return 0;

}