#include <bits/stdc++.h>
using namespace std;

int getint() {
	char c = ' ';
	for(; c < '0' || c > '9'; c = getchar());
	int ret = 0;
	for(; c >= '0' && c <= '9'; c = getchar()) ret = ret * 10 + c - '0';
	return ret;
}

#define INF (1000000001)

const int N = 1010;
int n, r, o, y, g, b, v;
vector<string> R, B, Y;
int answer[N];

bool cmp(const vector<string> &a, const vector<string> &b) {
	return a.size() > b.size();
}

bool violate(char x, char y) {
	if(y == 'R' || y == 'B' || y == 'Y') swap(x, y);
	if(!(x == 'R' || x == 'B' || x == 'Y')) return true;
	if(x == 'R') return y == 'O' || y == 'V' || y == 'R';
	if(x == 'B') return y == 'G' || y == 'V' || y == 'B';
	if(x == 'Y') return y == 'G' || y == 'O' || y == 'Y';
	return false;
}

void solve() {
	R.clear(), B.clear(), Y.clear();
	string tmp;
	if(g) {
		for(tmp = ""; r && g; --r, --g) tmp += "RG";
		if(r) --r, tmp += "R";
		R.push_back(tmp);
	}
    for(; r; --r) R.push_back("R");
	if(o) {
		for(tmp = ""; b && o; --b, --o) tmp += "BO";
		if(b) --b, tmp += "B";
		B.push_back(tmp);
	}
    for(; b; --b) B.push_back("B");
	if(v) {
		for(tmp = ""; y && v; --v, --y) tmp += "YV";
		if(y) --y, tmp += "Y";
		Y.push_back(tmp);
	}
	for(; y; --y) Y.push_back("Y");

    if(o || g || v) {
        puts("IMPOSSIBLE");
        return;
    }

	vector<vector<string> > a;
	a.push_back(R);
	a.push_back(B);
	a.push_back(Y);
	sort(a.begin(), a.end(), cmp);

	string ans = "";
	int n = a[0].size() + a[1].size() + a[2].size();
    int block = 0;
    for(int i = 0; i < 3; ++i) block += (a[i].size() > 0);
    if(block == 0) {
        puts("");
        return;
    }
    if(block == 1) {
        if(n == 1) cout << a[0].back();
        else puts("IMPOSSIBLE");
        return;
    }
    if(block == 2) {
        while(n) {
            sort(a.begin(), a.end(), cmp);
            ans += a[0].back();
            if(a[1].size()) ans += a[1].back();
            if(a[0].size()) a[0].pop_back();
            if(a[1].size()) a[1].pop_back();
            n = a[0].size() + a[1].size() + a[2].size(); 
        }
    } else if(block == 3) {
        vector<string> data;
        for(int i = 0; i < 3; ++i)
            for(auto str : a[i]) data.push_back(str);
        memset(answer, 255, sizeof(answer));
        // cout << n << endl;
        // cout << data.size() << endl;
        for(int i = 0, x = 0; i < n; ++i, x = (x + 2) % n) {
            while(answer[x] != -1) x = (x + 1) % n;
            // cout << "x = " << x << endl;
            answer[x] = i;
        }
        // for(int i = 0; i < n; ++i) cout << answer[i] << ' ';
        // cout << endl;
        ans = "";
        for(int i = 0; i < n; ++i) ans += data[answer[i]];
    }

	n = ans.size();
	for(int i = 0; i < n - 1; ++i) {
		char l = ans[(i - 1 + n) % n],
			x = ans[i],
			r = ans[(i + 1 + n) % n];
		if(violate(x, l) || violate(x, r)) {
			puts("IMPOSSIBLE");
			return;
		}
	}
	cout << ans << endl;
}

int main() {
	int testcases = getint();
	for(int testindex = 1; testindex <= testcases; ++testindex) {
		printf("Case #%d: ", testindex);
		n = getint();
		r = getint();
		o = getint();
		y = getint();
		g = getint();
		b = getint();
		v = getint();
		solve();
	}
	return 0;
}

