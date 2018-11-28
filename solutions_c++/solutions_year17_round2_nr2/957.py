#include <iostream>
#include <string>
#include <vector>
#include <assert.h>

using namespace std;

typedef long long ll;
typedef pair<char, int> PCI;

#define fi first
#define se second
#define mp make_pair
#define pb push_back

int T, N, R, O, Y, G, B, V;

int findPos(string s) {
	if (s[0] == 'B') return 0;
	for(int i = 1; i < s.size(); i ++) {
		if (s[i] == 'Y' || s[i] == 'B')
			if (s[i-1] != 'R')
				return i;
	}
	if (s[0] == 'Y') return 0;
	assert(false);
	return -1;
}

int countY(string s) {
	int sum = 0;
	for(int i = 0; i < s.size(); i ++)
		if (s[i] == 'Y') sum++;
	return sum;
}

int countB(string s) {
	int sum = 0;
	for(int i = 0; i < s.size(); i ++)
		if (s[i] == 'B') sum++;
	return sum;
}

int countR(string s) {
	int sum = 0;
	for(int i = 0; i < s.size(); i ++)
		if (s[i] == 'R') sum++;
	return sum;
}

void solve() {
	if (B == O && (R+Y+G+V) == 0) {
		for (int i = 0; i < B; i ++) cout << "BO";
		return;
	}
	if (Y == V && (R+B+G+O) == 0) {
		for (int i = 0; i < Y; i ++) cout << "YV";
		return;
	}
	if (R == G && (B+Y+O+V) == 0) {
		for (int i = 0; i < R; i ++) cout << "RG";
		return;
	}
	if (B <= O && O > 0) {
		cout << "IMPOSSIBLE";
		return;
	}
	if (Y <= V && V > 0) {
		cout << "IMPOSSIBLE";
		return;
	}
	if (R <= G && G > 0) {
		cout << "IMPOSSIBLE";
		return;
	}
	//at least three colors
	int BB = B - O, YY = Y - V, RR = R - G; //BB,YY,RR>=1
	if (BB > YY+RR || YY > BB+RR || RR > BB+YY) {
		cout << "IMPOSSIBLE";
		return;
	}
	string result;
	if (YY > BB) for (int i = 0; i < max(YY,BB) - min(YY,BB); i ++) result.pb('Y');
	else for (int i = 0; i < max(YY,BB) - min(YY,BB); i ++) result.pb('B');
	for (int i = 0; i < min(YY,BB); i ++) result.append("YB");
	for (int i = 0; i < RR; i ++) {
		result.insert(findPos(result), "R");
	}
	string tmp;
	size_t found;
	//replace B with BOB...
	if (O > 0) {
		tmp.clear();
		for (int i = 0; i < O; i ++)
			tmp.append("BO");
		tmp.append("B");
		found = result.find("B");
		assert(found != string::npos);
		result.replace(found, 1, tmp);
	}
	//replace Y with YVY...
	if (V > 0) {
		tmp.clear();
		for (int i = 0; i < V; i ++)
			tmp.append("YV");
		tmp.append("Y");
		found = result.find("Y");
		assert(found != string::npos);
		result.replace(found, 1, tmp);
	}
	//replace G with RGR...
	if (G > 0) {
		tmp.clear();
		for (int i = 0; i < G; i ++)
			tmp.append("RG");
		tmp.append("R");
		found = result.find("R");
		assert(found != string::npos);
		result.replace(found, 1, tmp);
	}
	//check...
	assert(result.size() == N);
	found = result.find("RR");
	assert(found == string::npos);
	found = result.find("BB");
	assert(found == string::npos);
	found = result.find("YY");
	assert(found == string::npos);
	assert(Y == countY(result));
	assert(B == countB(result));
	assert(R == countR(result));
	//only when small: check...
	//assert(result[0] != result[result.size() - 1]);
	cout << result;
	return;
}

int main() {
	cin >> T;
	for (int i = 0; i < T; i ++) {
		cin >> N >> R >> O >> Y >> G >> B >> V;
		printf("Case #%d: ", i + 1);
		solve();
		cout << endl;
	}
	return 0;
}
