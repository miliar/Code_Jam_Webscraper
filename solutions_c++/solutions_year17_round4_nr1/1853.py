#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <assert.h>
#include <algorithm>
#include <math.h>
#include <ctime>
#include <functional>
#include <string.h>
#include <stdio.h>
#include <numeric>
#include <float.h>

using namespace std;

int main(int argc, char* argv[]) {
	ifstream inf(argv[1]);

	int T = 0; inf >> T;
	for (int t = 0; t < T; t++) {
		int n, p; inf >> n >> p;
		vector<int> g(n);
		for (int i = 0; i < n; i++) {
			inf >> g[i];
			g[i] = g[i] % p; 
		}

		sort(g.begin(), g.end()); 

		int ans = 0; 

		for (int i = 0; i < g.size(); i++) {
			if (g[i] != 0) break;
			ans++; 
		}

		if (p == 2) {
			int k = n - ans; 
			ans += (k / 2) + (k % 2); 
		}
		else if (p == 3) {
			int n1 = 0, n2 = 0; 
			for (int i = 0; i < n; i++) {
				if (g[i] == 1) n1++;
				if (g[i] == 2) n2++; 
			}
			int maxn = max(n1, n2), minn = min(n1, n2); 
			ans += minn;
			ans += (maxn - minn) / 3; 
			if (((maxn - minn) % 3) != 0)
				ans++;
		}
		else if (p == 4) {
			int n1 = 0, n2 = 0, n3 = 0; 
			for (int i = 0; i < n; i++) {
				if (g[i] == 1) n1++;
				if (g[i] == 2) n2++;
				if (g[i] == 3) n3++;
			}

			int maxn = max(n1, n3), minn = min(n1, n3);
			ans += minn; 
			int diff = maxn - minn; 
			ans += n2 / 2; 
			if (((n2 % 2) == 1) && (diff >= 2)) {
				ans++;
				diff -= 2; 
			}
			ans += diff / 4; 
			if ((diff % 4) != 0) {
				ans++; 
			}
		}
		
		cout << "Case #" << t + 1 << ": " << ans << endl;

	}

	return 0;
}

/*
long long finalResult;
long long ahd, aad, ahk, aak, b, d;
bool cured = false;

long long reduce(long long o, long long d) {
	if (o < d) return 0; 
	return (o - d); 
}

bool solution(int hd, int ad, int hk, int ak, long long& result, bool cured) {
	if (hd <= 0) return false;

	result++; 
	if (result > finalResult) return false;

	long long resultBk = result; 

	// my turn
	if (ad >= hk) {
		finalResult = min(finalResult, result);
		return true;
	}

	long long tempResult = resultBk;
	bool good = false;
	if (solution(hd - ak, ad, hk - ad, ak, tempResult, false)) {
		result = tempResult;
		finalResult = min(finalResult, result);
		good = true;
	}
	
	tempResult = resultBk;
	if (!cured && hd < ahd) {
		if (solution(ahd - ak, ad, hk, ak, tempResult, true)) {
			if (!good) {
				good = true;
				result = tempResult;
				finalResult = min(finalResult, result);
			}
			else {
				if (tempResult < result) {
					result = tempResult;
					finalResult = min(finalResult, result);
				}
			}
		}
	}

	tempResult = resultBk; 
	if (b > 0) {
		if (solution(hd - ak, ad + b, hk, ak, tempResult, false)) {
			if (!good) {
				good = true;
				result = tempResult;
				finalResult = min(finalResult, result);
			}
			else {
				if (tempResult < result) {
					result = tempResult;
					finalResult = min(finalResult, result);
				}
			}
		}
	}

	tempResult = resultBk;
	if (ak > 0 && d > 0) {
		if (solution(hd - reduce(ak, d), ad, hk, reduce(ak, d), tempResult, false)) {
			if (!good) {
				good = true;
				result = tempResult;
				finalResult = min(finalResult, result);
			}
			else {
				if (tempResult < result) {
					result = tempResult;
					finalResult = min(finalResult, result);
				}
			}
		}
	}

	return good;
}


int main(int argc, char* argv[]) {
	ifstream inf(argv[1]);

	int T = 0; inf >> T;
	for (int t = 0; t < T; t++) {
		
		inf >> ahd >> aad >> ahk >> aak >> b >> d;

		finalResult = 0x7fffffffffffffff;

		long long myResult = 0; 

		if (solution(ahd, aad, ahk, aak, myResult, false))
			cout << "Case #" << t + 1 << ": " << finalResult << endl;
			//cout << "Case #" << t + 1 << ": " << myResult << endl;
		else 
			cout << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;

	}

	return 0;
}
*/

//int vv[100010];
//int lastNum[100010]; 
//int initPos[100010];
//
//int main() {
//	int n, m; cin >> n >> m;
//	set<int> ss; 
//	map<int, int> mm;
//
//	for (int i = 0; i < m; i++) {
//		initPos[i] = 0; 
//		cin >> lastNum[i];
//	}
//	ss.insert(0);
//	for (int i = 0; i < (n - 1); i++) {
//		for (int j = 0; j < m; j++) {
//			int currentNum = 0; cin >> currentNum; 
//			if (currentNum >= lastNum[j]) {
//				lastNum[j] = currentNum;
//			}
//			else {
//				mm[initPos[j]] = max(mm[initPos[j]], i);
//				initPos[j] = i+1;
//				ss.insert(initPos[j]);
//				lastNum[j] = currentNum;
//			}
//		}
//	}
//
//	for (int i = 0; i < m; i++) {
//		mm[initPos[i]] = max(mm[initPos[i]], n - 1); 
//	}
//
//	vector<int> vInitNums; 
//	for (set<int>::iterator iter = ss.begin(); iter != ss.end(); iter++) {
//		vInitNums.push_back(*iter);
//	}
//
//	sort(vInitNums.begin(), vInitNums.end());
//
//	int k = 0; cin >> k; 
//	for (int i = 0; i < k; i++) {
//		int l, r; cin >> l >> r; l--; r--;
//		bool Ok = false;
//		for (int j = 0; j < vInitNums.size(); j++) {
//			if (l < vInitNums[j]) break;
//			if (mm[vInitNums[j]] >= r) {
//				Ok = true;
//				break;
//			}
//		}
//		if (Ok) cout << "Yes" << endl;
//		else cout << "No" << endl;
//	}
//
//
//	return 0; 
//}

/*
int main(int argc, char* argv[]) {
	ifstream inf(argv[1]);

	int T = 0; inf >> T;
	for (int t = 0; t < T; t++) {
		string s; long long n; inf >> s >> n; 

		int l = 1;
		long long num = s.size(); 
		while (true) {
			if (n <= num) {
				break;
			}
			l++;
			n -= num; 
			num *= s.size(); 
		}

		string result; 
		num = 1; 
		for (int i = 0; i < (l - 1); i++) {
			num *= s.size(); 
		}

		for (int i = 0; i < l; i++) {
			int index = n / num; 
			if (n % num > 0) index++; 
			result.push_back(s[index-1]);
			if (n % num > 0)
				n = n % num;
			else
				n = num;
			num /= s.size(); 
			
		}

		cout << "Case #" << t + 1 << ": " << result << endl; 
	}
	 
	return 0; 
}
*/

/*
const int SZ = 110; 
const long long INF = 5000000000000;
long long g[SZ][SZ];

long long dp_source[5500][2];
long long dp_dest[5500][2];

int main(int argc, char* argv[]) {
	ifstream inf(argv[1]);

	int T = 0; inf >> T;
	for (int t = 0; t < T; t++) {
		for (int i = 0; i < SZ; i++)
			for (int j = 0; j < SZ; j++)
				g[i][j] = INF; 

		for (int i = 0; i < 5500; i++)
			for (int j = 0; j < 2; j++)
				dp_source[i][j] = INF;

		for (int i = 0; i < 5500; i++)
			for (int j = 0; j < 2; j++)
				dp_dest[i][j] = INF;

		int n, m, k; inf >> n >> m >> k; 
		for (int i = 0; i <= n; i++) {
			g[i][i] = 0; 
		}
		for (int i = 0; i < m; i++) {
			int a, b, gas; inf >> a >> b >> gas; 
			g[a][b] = gas;
			g[b][a] = gas;
		}

		for (int l = 1; l <= n; l++) {
			for (int i = 1; i <= n; i++) {
				for (int j = 1; j <= n; j++) {
					if (g[i][l] == INF || g[l][j] == INF)
						continue;
					g[i][j] = min(g[i][j], g[i][l] + g[l][j]); 
				}
			}
		}

		vector<int> vs, vd; 
		vs.push_back(1); vd.push_back(1); 
		for (int i = 0; i < k; i++) {
			int s, d; inf >> s >> d;
			vs.push_back(s);
			vd.push_back(d);
		}
		dp_dest[0][0] = 0;
		dp_dest[0][1] = INF;
		dp_source[0][0] = INF; 
		dp_source[0][1] = INF; 

		for (int deliver = 1; deliver <= k; deliver++) {
			int preSource = vs[deliver - 1];
			int preDest = vd[deliver - 1];
			int source = vs[deliver];
			int dest = vd[deliver];
			int nxtSource = 0;
			int nxtDet = 0;
			if (deliver < k) {
				nxtSource = vs[deliver + 1];
				nxtDet = vd[deliver + 1];
			}

			if (g[preDest][source] != INF)
				dp_source[deliver][0] = min(dp_source[deliver][0], dp_dest[deliver - 1][0] + g[preDest][source]);

			if (deliver < k && g[source][nxtSource] != INF) {
				dp_source[deliver + 1][1] = min(dp_source[deliver + 1][1], dp_source[deliver][0] + g[source][nxtSource]);
			}

			if (g[preSource][source] != INF)
				dp_source[deliver][1] = min(dp_source[deliver][1], dp_source[deliver - 1][0] + g[preSource][source]); 

			if (g[source][dest] != INF)
				dp_dest[deliver][0] = min(dp_dest[deliver][0], dp_source[deliver][0] + g[source][dest]);

			if (g[preDest][dest] != INF)
				dp_dest[deliver][0] = min(dp_dest[deliver][0], dp_dest[deliver - 1][1] + g[preDest][dest]); 

			if (g[nxtSource][dest] != INF)
				dp_dest[deliver][1] = min(dp_dest[deliver][1], dp_source[deliver+1][1] + g[nxtSource][dest]);
		}

		long long result = -1; 
		if (dp_dest[k][0] != INF)
			result = dp_dest[k][0];

		cout << "Case #" << t + 1 << ": " << result << endl;

	}
	return 0;
}
*/

/*
struct Point {
	long long x, y; 
	Point(long long ax, long long ay) : x(ax), y(ay) {}
};
bool operator <(const Point& p1, const Point& p2) {
	return p1.x < p2.x || (p1.x == p2.x && p1.y < p2.y);
}

bool inRec(long long x, long long y, long long r, long long x1, long long y1, int type) {
	if (type == 1) {
		if (x1 > (x + r) || y1 > (y + r) || x1 < x || y1 < y)
			return false;
	}
	else if (type == 2) {
		if (x1 <(x - r) || y1 >(y + r) || x1 > x || y1 < y)
			return false;
	}
	else if (type == 3) {
		if (x1 <(x - r) || y1 <(y - r) || x1 > x || y1 > y)
			return false;
	}
	else if (type == 4) {
		if (x1 >(x + r) || y1 < (y - r) || x1 < x || y1 > y)
			return false;
	}
	return true;
}

int main(int argc, char* argv[]) {
	ifstream inf(argv[1]);

	int T = 0; inf >> T;
	for (int t = 0; t < T; t++) {
		int n, r; inf >> n >> r; 

		vector<Point> points; 
		for (int i = 0; i < n; i++) {
			long long x, y; inf >> x >> y;
			points.push_back(Point(x, y));
		}

		vector<vector<Point>> pointSet; 
		for (int i = 0; i < points.size(); i++) {
			// case 1
			vector<Point> v1; 
			for (int j = 0; j < points.size(); j++) {
				if (inRec(points[i].x, points[i].y, r, points[j].x, points[j].y, 1)) {
					v1.push_back(points[j]);
				}
			}
			pointSet.push_back(v1);

			// case 2
			vector<Point> v2;
			for (int j = 0; j < points.size(); j++) {
				if (inRec(points[i].x, points[i].y, r, points[j].x, points[j].y, 2)) {
					v2.push_back(points[j]);
				}
			}
			pointSet.push_back(v2);

			// case 3
			vector<Point> v3;
			for (int j = 0; j < points.size(); j++) {
				if (inRec(points[i].x, points[i].y, r, points[j].x, points[j].y, 3)) {
					v3.push_back(points[j]);
				}
			}
			pointSet.push_back(v3);

			// case 4
			vector<Point> v4;
			for (int j = 0; j < points.size(); j++) {
				if (inRec(points[i].x, points[i].y, r, points[j].x, points[j].y, 4)) {
					v4.push_back(points[j]);
				}
			}
			pointSet.push_back(v4);
		}

		size_t result = 0; 
		for (int i = 0; i < pointSet.size(); i++) {
			set<Point> testSet; 
			for (int k = 0; k < pointSet[i].size(); k++) {
				testSet.insert(pointSet[i][k]);
			}
			for (int j = 0; j < pointSet.size(); j++) {
				set<Point> testSetCp = testSet; 
				for (int k = 0; k < pointSet[j].size(); k++) {
					testSetCp.insert(pointSet[j][k]);
				}
				result = max(result, testSetCp.size());
			}
		}

		cout << "Case #" << t + 1 << ": " << result << endl;

	}
	return 0;
}
*/




/*
const int maxLen = 1000010; 

int a[maxLen][21];
int nums[maxLen];

int main() {
	int n; cin >> n; 
	for (int i = 0; i < n; i++) {
		cin >> nums[i]; 
	}
	
	for (int i = 0; i < maxLen; i++) {
		nums[i] = 0x7fffffff;
	}

	for (int pos = 0; pos < n; pos++) {
		a[pos][0] = nums[pos];
	}

	for (int j = 1; j <= 21; j++) {
		for (int i = 0; i<=)
	}






	for (int len = 1; len <= maxLength; len++) {
		int step = p2[len - 1]; 
		for (int pos = 0; pos < n; pos++) {
			int pos1 = pos; 
			int pos2 = pos + step; 

			a[pos][len] = a[pos][len - 1]; 
			if (pos2 < n) {
				a[pos][len] = min(a[pos][len], a[pos2][len - 1]); 
			}
		}
	}

	int m; cin >> m;
	for (int i = 0; i < m; i++) {
		int i1, i2; cin >> i1 >> i2; 
		int range = i2 - i1 + 1; 
		int k = log(range) / log(2);
		int num = min(a[i1 - 1][k], a[i2 - 1 - p2[k] + 1][k]); 
		cout << num << endl;
	}

	return 0; 
}
*/

/*
int main() {
	int n, k; cin >> n >> k;

	vector<int> walks(n); 
	for (int i = 0; i < n; i++) {
		cin >> walks[i]; 
	}

	if (n == 1) {
		if (walks[0] >= k) {
			cout << 0 << endl;
			cout << walks[0] << endl;
		}
		else {
			cout << k - walks[0] << endl;
			cout << k << endl;
		}
	}
	else {
		int ans = 0; 
		vector<int> steps(n); steps[0] = walks[0];
		for (int i = 1; i < n; i++) {
			int sum = steps[i - 1] + walks[i]; 
			if (sum < k) {
				ans += (k - sum);
			}
			int needWalk = 0; 
			if (steps[i - 1] >= k) {
				needWalk = 0; 
			}
			else {
				needWalk = k - steps[i - 1]; 
			}
			steps[i] = max(needWalk, walks[i]);
		}

		int ans2 = 0; 
		vector<int> steps2(n); steps2[n-1] = walks[n-1];
		for (int i = n - 2; i >= 0; i--) {
			int sum = steps2[i + 1] + walks[i];
			if (sum < k) {
				ans2 += (k - sum); 
			}
			int needWalk = 0; 
			if (steps2[i + 1] >= k) {
				needWalk = 0; 
			}
			else {
				needWalk = k - steps2[i + 1];
			}
			steps2[i] = max(needWalk, walks[i]); 
		}

		if (ans < ans2) {
			cout << ans << endl;
			for (int i = 0; i < steps.size(); i++) {
				cout << steps[i] << " ";
			}
			cout << endl;
		}
		else {
			cout << ans2 << endl;
			for (int i = 0; i < steps2.size(); i++) {
				cout << steps2[i] << " ";
			}
			cout << endl;
		}
	}

	return 0; 
}
*/

/* 550 500 v2 */
/*
int g[200][200];
int dx[4] = { 1, 0, -1, 0 }; 
int dy[4] = { 0, -1, 0, 1 };

class RotatingBot {
public:
	int minArea(vector<int> moves) {
		int x = 100, y = 100; g[x][y] = 1; 
		int minx = 200, miny = 200, maxx = 0, maxy = 0; 

		for (int i = 0; i < moves.size(); i++) {
			int id = i % 4; 
			for (int j = 0; j < moves[i]; j++) {
				x += dx[id]; 
				y += dy[id];
				if (g[x][y] != 0) return -1;
				g[x][y] = 1; 

				minx = min(minx, x);
				miny = min(miny, y);
				maxx = max(maxx, x);
				maxy = max(maxy, y);
			}
		}


	}
};

int main() {
	RotatingBot cls;

	int a[] = { 1,1,1,1 };
	vector<int> vec(a, a + sizeof(a) / sizeof(int)); 
	cout << cls.minArea(vec) << endl;
	return 0;
}
*/

/*
int nums[21][21];

int n, m; 

map<pair<int, int>, int> cols;

bool solution() {
	for (int i = 0; i < n; i++) {
		vector<int> needChange;

		for (int j = 0; j < m; j++) {
			if (nums[i][j] != (j + 1)) {
				needChange.push_back(j);
			}
		}
		if (needChange.size() == 0) continue;
		if (needChange.size() == 2) {
			if (cols.find(make_pair(needChange[0], needChange[1])) != cols.end()) {
				return false;
			}
			cols[make_pair(needChange[0], needChange[1])] = 1; 
			continue;
		}
		return false;
	}
	return true;
}


int main(int argc, const char* argv[]) {
	cin >> n >> m; 

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			int num = 0; cin >> num;
			nums[i][j] = num; 
		} 
	}

	bool ordered = true;
	for (int i = 0; i < n; i++) {
		vector<int> needChange;

		for (int j = 0; j < m; j++) {
			if (nums[i][j] != (j + 1)) {
				needChange.push_back(j);
			}
		}

		if (needChange.size() != 0) {
			ordered = false;
		}
	}

	if (ordered) {
		cout << "YES" << endl;
		return 0;
	}

	for (int i = 0; i < n; i++) {
		vector<int> needChange;

		for (int j = 0; j < m; j++) {
			if (nums[i][j] != (j + 1)) {
				needChange.push_back(j);
			}
		}

		if (needChange.size() == 2) {
			// elements

			int nn = nums[i][needChange[0]];
			nums[i][needChange[0]] = nums[i][needChange[1]];
			nums[i][needChange[1]] = nn;
			cols[make_pair(needChange[0], needChange[1])] = 1; 
			bool poss = solution();
			if (poss) {
				cout << "YES" << endl;
				return 0;
			}

			// columns
			cols.clear();
			for (int j = 0; j < n; j++) {
				if (j == i) continue;
				int nn = nums[j][needChange[0]];
				nums[j][needChange[0]] = nums[j][needChange[1]];
				nums[j][needChange[1]] = nn;
			}
			cols[make_pair(needChange[0], needChange[1])] = 1;
			poss = solution();
			if (poss) {
				cout << "YES" << endl;
				return 0;
			}

			cout << "NO" << endl;
			return 0;

			// columns
		}
	}

	cout << "NO" << endl; 

	return 0;
}
*/

/*
int main() {
	OrderOfOperations cls; 
	char* pstr[] = {
		"11101",
		"00111",
		"10101",
		"00000",
		"11000"
	}; 

	vector<string> vs; 
	for (int i = 0; i < (sizeof(pstr) / sizeof(char*)); i++) {
		vs.push_back(pstr[i]); 
	}

	cout << cls.minTime(vs) << endl; 

	
	return 0; 
}
*/

/*
int main(int argc, char* argv[]) {
	ifstream inf(argv[1]);
	int TC = 0; inf >> TC;

	for (int tc = 1; tc <= TC; tc++) {


		cout << "Case #" << tc << ": " << bestAns << endl;;

	}

	return 0;
}
*/

/*
struct Rec {
	vector<int> line; 
};
bool operator<(Rec rec1, Rec rec2) {
	for (int i = 0; i < rec1.line.size(); i++) {
		if (rec1.line[i] < rec2.line[i]) return true; 
	}
	return false; 
}

vector<Rec> numbers; 
int n; 

bool solve(int pos, int recNum) {
	bool result = false; 
	if (pos == 0) {
		if (numbers[0].line[0] == numbers[1].line[0]) {
			for (int i = 0; i < n; i++) {
				arr[0][i] = numbers[0].line[i]; 
				arr[i][0] = numbers[1].line[i]; 
			}
			result = solve(1, 2); 
		}
		else {
			for (int i = 0; i < n; i++) {
				arr[i][0] = numbers[0].line[i]; 
			}
			result = solve(1, 1); 
		}
	}
	else {
		if (arr[0][pos] == -1) {

		}
		else {

		}
	}
}

int main(int argc, char* argv[]) {
	ifstream inf(argv[1]);
	int TC = 0; inf >> TC;

	for (int tc = 1; tc <= TC; tc++) {
		inf >> n; 
		memset(arr, -1, sizeof(arr)); 

		numbers.clear(); 
		for (int i = 0; i < n - 1; i++) {
			Rec rec; 
			for (int j = 0; j < n; j++) {
				int n = 0; inf >> n; 
				rec.line.push_back(n); 
			}
			numbers.push_back(rec);
		}

		sort(numbers.begin(), numbers.end()); 




		cout << "Case #" << tc << ": " << ans << endl; 
	}

	return 0;
}
*/

/*
string add(string& s1, string& s2) {
	string result; 

	int over = 0; 
	for (int i = 0; i < max(s1.size(), s2.size()); i++) {
		int a = 0, b = 0; 
		if (i < s1.size()) {
			a = s1[s1.size() - i - 1] - '0'; 
		}
		if (i < s2.size()) {
			b = s2[s2.size() - i - 1] - '0'; 
		}

		int tr = a + b + over; 
		result.insert(result.begin(), '0' + (tr % 10)); 
		over = tr / 10; 
	}
	if (over > 0) result.insert(result.begin(), '0' + over); 
	return result; 
}

int main(int argc, char* argv[]) {
	ifstream inf(argv[1]);
	int TC = 0; inf >> TC; 

	for (int tc = 1; tc <= TC; tc++) {
		string s; inf >> s; 
		if (s == "0") {
			cout << "Case #" << tc << ": INSOMNIA" << endl; 
		}
		else {
			vector<bool> digits(10, false); 
			string now = s; 
			while (true) {
				for (int i = 0; i < now.size(); i++) {
					digits[now[i] - '0'] = true; 
				}

				bool allVisited = true;
				for (int i = 0; i < digits.size(); i++) {
					if (!digits[i]) {
						allVisited = false;
						break;
					}
				}
				if (allVisited) {
					cout << "Case #" << tc << ": " << now << endl;
					break;
				}

				now = add(now, s); 
			}
		}
	}

	return 0;
}
*/

/*
int main(int argc, char* argv[]) {
	ifstream inf(argv[1]); 

	int T = 0; inf >> T;
	for (int t = 1; t <= T; t++) {
		int row, col; inf >> row >> col; 
		vector<string> grid; 
		for (int i = 0; i < row; i++) {
			string str; inf >> str; 
			grid.push_back(str);
		}

		bool impossible = false; 
		int ans = 0; 
		for (int r = 0; r < row && !impossible; r++) {
			for (int c = 0; c < col && !impossible; c++) {
				if (grid[r][c] == '.') continue;
				bool b1 = false, b2 = false, b3 = false, b4 = false; 
				for (int i = 0; i < c; i++) {
					if (grid[r][i] != '.') {
						b1 = true;
						break;
					}
				}
				for (int i = c + 1; i < col; i++) {
					if (grid[r][i] != '.') {
						b2 = true;
						break;
					}
				}
				for (int i = 0; i < r; i++) {
					if (grid[i][c] != '.') {
						b3 = true;
						break;
					}
				}
				for (int i = r + 1; i < row; i++) {
					if (grid[i][c] != '.') {
						b4 = true;
						break;
					}
				}

				if (!b1 && !b2 && !b3 && !b4) {
					impossible = true;
				}
				else if (!b1 && grid[r][c] == '<') {
					ans++; 
				}
				else if (!b2 && grid[r][c] == '>') {
					ans++;
				}
				else if (!b3 && grid[r][c] == '^') {
					ans++;
				}
				else if (!b4 && grid[r][c] == 'v') {
					ans++;
				}
			}
		}


		cout << "Case #" << t << ": ";
		if (impossible) cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl; 
	}

	return 0;
}
*/


/*
int main(int argc, char* argv[]) {
	long long *l = new long long();


	return 0;
}
*/

/*
4.6.3
*/
/*
int totalUsedTime = 0; 
vector<string> process; 

struct Rec {
	int id = 0, times = 0; 
	Rec(int aid, int atimes) : id(aid), times(atimes) {}
};
bool operator<(Rec &rec1, Rec &rec2) {
	return rec1.times < rec2.times;
}1

void solution(vector<Rec> times) {
	sort(times.begin(), times.end());
	int n = times.size(); 
	vector<bool> overRiver(n, false); 
	while (n > 0) {
		if (n == 1 || n == 2) {
			int usedTime = 0; 
			string pro; 
			for (int i = 0; i < times.size(); i++) {
				if (!overRiver[i]) {
					usedTime = max(usedTime, times[i].times);
					if (!pro.empty()) pro.push_back(' ');
					char buf[10] = { 0 };
					sprintf(buf, "%d", times[i].times);
					pro += buf;
					overRiver[i] = true;
				}
			}
			n = 0; 
			totalUsedTime += usedTime;
			process.push_back(pro);
		}
		else {
			if (overRiver[0] == false && overRiver[1] == false) {
				// go
				totalUsedTime += times[1].times;
				char buf[100] = { 0 };
				sprintf(buf, "%d %d", times[0].times, times[1].times);
				process.push_back(buf);
				overRiver[0] = true;
				overRiver[1] = true;
				// back
				totalUsedTime += times[0].times;
				memset(buf, 0, sizeof(buf));
				sprintf(buf, "%d", times[0].times);
				process.push_back(buf);
				overRiver[0] = false;
			}
			else {
				bool gotSlowest = false;
				int p1 = 0, p2 = 0;
				for (int i = times.size() - 1; i >= 0; i--) {
					if (!overRiver[i]) {
						if (gotSlowest) {
							p2 = i; 
							break;
						}
						else {
							gotSlowest = true;
							p1 = i; 
						}
					}
				}
				if (2 * times[1].times > times[p2].times + times[0].times) {
					// go 
					char buf[100] = { 0 };
					sprintf(buf, "%d %d", times[0].times, times[p1].times);
					process.push_back(buf);
					overRiver[p1] = true;
					overRiver[0] = true;
					totalUsedTime += times[p1].times;
					// back
					memset(buf, 0, sizeof(buf));
					sprintf(buf, "%d", times[0].times);
					process.push_back(buf);
					overRiver[0] = false;
					totalUsedTime += times[0].times;
				}
				else {
					// go 
					char buf[100] = { 0 };
					sprintf(buf, "%d %d", times[p2].times, times[p1].times);
					process.push_back(buf);
					overRiver[p1] = true;
					overRiver[p2] = true;
					totalUsedTime += times[p1].times;
					// back
					memset(buf, 0, sizeof(buf));
					sprintf(buf, "%d", times[1].times);
					process.push_back(buf);
					overRiver[1] = false;
					totalUsedTime += times[1].times;
				}
			}
			n -= 1;
		}
	}
}

int main() {
	int TC = 0; cin >> TC;
	bool blank = false; 
	for (int tc = 1; tc <= TC; tc++) {
		int num = 0; cin >> num; 
		vector<Rec> times; 
		for (int i = 0; i < num; i++) {
			int d = 0; cin >> d; 
			times.push_back(Rec(i+1, d)); 
		}

		if (blank) cout << endl; 
		blank = true;

		solution(times);
		cout << totalUsedTime << endl; totalUsedTime = 0; 
		for (int i = 0; i < process.size(); i++) cout << process[i] << endl; 
		process.clear();
	}
	return 0; 
}
*/