#include <bits/stdc++.h>
using namespace std;

const int SIZE = 1005;

#define fi first
#define se second

int N,R,O,Y,G,B,V;

bool check(int A, int B) {
	return A > 0 && (A > B || ((A + B) < N && A == B));
}

pair<int, char> arr[3];

string getRep(string st, int n) {
	string ans = "";
	while (n--)  {
		ans += st;
	}
	return ans;
}

string solve() {
	string no = "IMPOSSIBLE";
	if (check(O, B)) {
		return no;
	}
	if (check(V, Y)) {
		return no;
	}
	if (check(G, R)) {
		return no;
	}
	B -= O;
	Y -= V;
	R -= G;
	if (!(B <= Y + R && Y <= R + B && R <= B + Y)) {
		return no;
	}
	arr[0] = make_pair(B, 'B');
	arr[1] = make_pair(Y, 'Y');
	arr[2] = make_pair(R, 'R');
	sort(arr, arr + 3);
	int st = 2;
	string ans = "";
	for (int i = 0; i < B + Y + R; i++) {
		ans += arr[st].se;
		arr[st].fi --;
		int new_st = -1;
		int max_num = -1;
		for (int j = 0; j < 3; j++) {
			if (st != j && arr[j].fi != 0 && max_num <= arr[j].fi) {
				max_num = arr[j].fi;
				new_st = j;
			}
		}
		st = new_st;
	}

	string ret = "";
	for (int i = 0; i < ans.size(); i++) {
		ret += ans[i];

		if (ans[i] == 'B' && O > 0) {
			ret += getRep("OB", O);
			O = 0;
		}
		if (ans[i] == 'Y' && V > 0) {
			ret += getRep("VY", V);
			V = 0;
		}
		if (ans[i] == 'R' && G > 0) {
			ret += getRep("GR", G);
			G = 0;
		}
	}

	if (O > 0) {
		ret += "OB";
	}
	if (V > 0) {
		ret += "VY";
	}
	if (G > 0) {
		ret += "GR";
	}

	return ret;
}

int main() {
	freopen("input1.txt", "r", stdin);
	freopen("output1.txt", "w", stdout);

	int t;
	cin>>t;
	for (int t_id = 1; t_id <= t; t_id++) {
		cin>>N>>R>>O>>Y>>G>>B>>V;
		printf("Case #%d: ", t_id);
		cout<<solve()<<endl;
	}

	return 0;
}
