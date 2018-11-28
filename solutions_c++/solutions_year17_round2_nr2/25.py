#include "bits/stdc++.h"
using namespace std;
#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
static const int INF = 0x3f3f3f3f; static const long long INFL = 0x3f3f3f3f3f3f3f3fLL;
typedef vector<int> vi; typedef pair<int, int> pii; typedef vector<pair<int, int> > vpii; typedef long long ll;
template<typename T, typename U> static void amin(T &x, U y) { if (y < x) x = y; }
template<typename T, typename U> static void amax(T &x, U y) { if (x < y) x = y; }

const int C = 6;
array<int, C> colors = { 1, 1 | 2, 2, 2 | 4, 4, 4 | 1 };
const char *alphabets = "ROYGBV";

int memo[8][8][8][8][8][8][6][6];

bool isok(int x, int y) {
	return (colors[x] & colors[y]) == 0;
}

int naivedp(array<int, C> num, int firstcol, int prevcol) {
	int &r = memo[num[0]][num[1]][num[2]][num[3]][num[4]][num[5]][firstcol][prevcol];
	if (r != -1) return r;
	if (accumulate(num.begin(), num.end(), 0) == 0)
		return r = isok(prevcol, firstcol);
	r = 0;
	rep(c, C) if (num[c] > 0 && isok(prevcol, c)) {
		auto nnum = num;
		-- nnum[c];
		r |= naivedp(nnum, firstcol, c);
	}
	return r;
}

const char *imp = "IMPOSSIBLE";
string naivesolve(array<int, C> num) {
	int sum = accumulate(num.begin(), num.end(), 0);
	int firstcol = -1;
	rep(c, C) if (num[c] > 0) {
		auto nnum = num;
		-- nnum[c];
		if (naivedp(nnum, c, c)) {
			firstcol = c;
			break;
		}
	}
	if (firstcol == -1) return imp;
	int prevcol = firstcol;
	string ans(1, alphabets[firstcol]);
	-- num[firstcol];
	rep(i, sum - 1) {
		rep(c, C) if (num[c] > 0 && isok(prevcol, c)) {
			auto nnum = num;
			-- nnum[c];
			if (naivedp(nnum, firstcol, c)) {
				ans += alphabets[c];
				prevcol = c;
				num = nnum;
				break;
			}
		}
	}
	return ans;
}

bool solve1(array<int, 3> num, string &res) {
	res.clear();
	pair<pair<int,int>,int> v[3];
	while (num[0] != 0 || num[1] != 0 || num[2] != 0) {
		rep(i, 3)
			v[i] = { {num[i],res.empty()||res[0]== "RYB"[i] },i };
		sort(v, v + 3);
		reverse(v, v + 3);
		bool ok = false;
		for(auto p : v) {
			int i = p.second;
			if (num[i] == 0)continue;
			if (res.empty() || res.back() != "RYB"[i]) {
				ok = true;
				-- num[i];
				res += "RYB"[i];
				break;
			}
		}
		if (!ok) return false;
	}
	if (res.front() == res.back()) return false;
	return true;
}

bool solve2(array<int, 6> num, string &res) {
	res.clear();
	vector<string> seqs[6];
	rep(i, 6)
		rep(j, num[i])
			seqs[i].push_back(string(1, alphabets[i]));
	int total = accumulate(num.begin(), num.end(), 0);
	for (auto pairs : vpii{ { 1, 4 }, {3, 0}, {5, 2} }) {
		auto &v = seqs[pairs.first];
		auto &w = seqs[pairs.second];
		while (!v.empty()) {
			if (total == 2) {
				if (w.empty())return false;
				res = v.back() + w.back();
				return true;
			}
			if((int)w.size()<2) return false;
			string t = w.end()[-1] + v.end()[-1] + w.end()[-2];
			v.pop_back();
			w.pop_back();
			w.pop_back();
			w.push_back(t);
			total-=2;
		}
	}
	array<int, 3> num1 = { (int)seqs[0].size(),(int)seqs[2].size(),(int)seqs[4].size() };
	string str;
	if (!solve1(num1, str)) return false;
	for (char c : str) {
		auto &v = seqs[c == 'R' ? 0 : c == 'Y' ? 2 : c == 'B' ? 4 : -1];
		res += v.back();
		v.pop_back();
	}
	return true;
}

int main() {
	memset(memo, -1, sizeof(memo));
	if(0){
		rer(A,0,7)rer(B,0,7)rer(C,0,7){
			if (A + B + C <= 2)continue;
			string res;
			array<int, 3>num1 = { A,B,C };
			bool a = solve1(num1, res);
			array<int, 6> num2 = {A,0,B,0,C,0};
			bool b = naivesolve(num2) != imp;
			if (a != b)
				cerr << A << "," << B << "," << C << ": " << a << " != " << b << "; " << naivesolve(num2) << endl;
		}
	}
	if(0){
		int X = 7;
		rer(a, 0, X)rer(b, 0, X)rer(c, 0, X) rer(d, 0, X)rer(e, 0, X)rer(f, 0, X) {
			array<int, 6>num = { a,b,c,d,e,f };
			if (accumulate(num.begin(), num.end(), 0) <= 2)continue;
			string res;
			bool x = solve2(num, res);
			bool y = naivesolve(num) != imp;
			if (x != y)
				cerr << x << " != "<< y << endl;
			if (x) {
				assert(res.size()== accumulate(num.begin(), num.end(), 0));
				rep(i, res.size()) {
					int x = string(alphabets).find(res[i]);
					int y = string(alphabets).find(res[(i + 1) % res.size()]);
					assert(isok(x, y));
				}
			}
		}
	}
	int T;
	scanf("%d", &T);
	for (int ii = 0; ii < T; ++ ii) {
		int N;
		scanf("%d", &N);
		array<int, C> num;
		for(int &x : num)
			scanf("%d", &x);
		string ans;
		if(!solve2(num, ans))
			ans = imp;
		printf("Case #%d: %s\n", ii + 1, ans.c_str());
	}
	return 0;
}
