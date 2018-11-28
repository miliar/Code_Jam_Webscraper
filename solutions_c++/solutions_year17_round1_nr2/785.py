#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
#include <stack>

#define IN_FILE "B-large.in"
#define OUT_FILE "outL.txt"

using namespace std;

typedef long long ll;
typedef long double ld;

int r[55];
int ing[55][55];
int sel[55];
pair<int, int> ip[55][55];
ll ans;
stack< pair<pair<int,int>, pair<int, int>> > st;

void dfs(int n, int p) {
	for (int i = p - 1; i >= 0; i--) {
		if(ip[0][i].first!=-1)
			st.push(make_pair(make_pair(0, i), ip[0][i]));
	}
	while (!st.empty()) {
		pair<pair<int, int>, pair<int, int>> focus = st.top();
		st.pop();
		int fi = focus.first.first;
		pair<int, int> fint = focus.second;
		sel[fi] = focus.first.second;
		if (fi == n - 1) {
			for (int i = 1; i < n; i++)
				for (int j = sel[i]; j < p - 1; j++)
					ip[i][j] = ip[i][j + 1];
			ans++;
			while (!st.empty() && st.top().first.first)
				st.pop();
		}
		else {
			for (int i = p-ans-1; i >=0; i--) {
				int newf = max(fint.first, ip[fi + 1][i].first);
				int news = min(fint.second, ip[fi + 1][i].second);
				if (newf <= news)
					st.push(make_pair(make_pair(fi+1,i), make_pair(newf, news)));
			}
		}
	}
}

int main() {
	ios::sync_with_stdio(0);
	ifstream xin(IN_FILE);
	ofstream xout(OUT_FILE);
	cin.rdbuf(xin.rdbuf());
	cout.rdbuf(xout.rdbuf());
	int t;
	int tc = 1;
	cin >> t;
	while (t--) {
		int n, p;
		cin >> n >> p;
		for (int i = 0; i < n; i++)
			cin >> r[i];
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < p; k++) {
				cin >> ing[j][k];
				int f2 = (ing[j][k] * 100) / (r[j]*110) + (((ing[j][k] * 100) % (r[j] * 110))>0);
				int f1 = ((f2*r[j] * 90) / 100) + ((((f2*r[j] * 90) / 100))>0);
				int s1 = (ing[j][k] * 100) / (r[j]*90);
				int s2 = (s1*r[j] * 110) / 100;
				if (s2<ing[j][k] && f1>ing[j][k])
					ip[j][k] = { -1,-1 };
				else if (s2 < ing[j][k])
					ip[j][k] = { f2,f2 };
				else if (f1 > ing[j][k])
					ip[j][k] = { s1,s1 };
				else
					ip[j][k] = { f2,s1 };
			}
			sort(ip[j], ip[j] + p);
			//for (int i = 0; i < p; i++)
				//cout << "(" << ip[j][i].first << " " << ip[j][i].second << ") ";
			//cout << "\n";
		}

		ans = 0;
		dfs(n, p);

		cout << "Case #" << tc << ": " << ans << "\n";
		tc++;
	}
	system("pause");
	return 0;
}
