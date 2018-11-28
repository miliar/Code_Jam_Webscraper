#include <bits/stdc++.h>
using namespace std;

bool cmp(pair<char,int> a, pair<char,int> b) {
	return a.second > b.second;
} 

int main(int argc, char const *argv[])
{
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int num;
		int red, blue, yellow, orange, violet, green;
		cin >>  num >> red >> orange >> yellow >> green >> blue >> violet;
		string result = "";
		vector<pair<char, int> > colors;
		colors.push_back(make_pair('R', red));
		colors.push_back(make_pair('B', blue));
		colors.push_back(make_pair('Y', yellow));
		int c = 0;
		bool flag = true;
		sort(colors.begin(), colors.end(), cmp);
		if (colors[0].second > colors[1].second + colors[2].second) {
			cout << "Case #" << i + 1 << ": IMPOSSIBLE\n";
			continue;
		}
		int lim = colors[0].second - colors[1].second;
		for (int j = 0; j < lim; j++) {
			result += colors[0].first;
			result += colors[2].first;
			colors[0].second--;
			colors[2].second--;
		}
		while(colors[2].second > 0) {
			result += colors[0].first;
			result += colors[1].first;
			result += colors[2].first;
			colors[0].second--;
			colors[1].second--;
			colors[2].second--;
		}
		while(colors[0].second > 0) {
			result += colors[0].first;
			result += colors[1].first;
			colors[0].second--;
			colors[1].second--;
		}
		cout << "Case #" << i + 1 << ": " << result << endl;
	}
	return 0;
}