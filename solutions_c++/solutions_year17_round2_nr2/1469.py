#include <bits/stdc++.h>

using namespace std;

#define INF 2000000000
#define MOD 1000000007
typedef long long ll;
typedef pair<int, char> P;


int main()
{
	int t;
	cin >> t;

	for (int ii = 1; ii <= t; ii++) {
		int n, r, o, y, g, b, v;
		cin >> n >> r >> o >> y >> g >> b >> v;
//		ll sum = 0;
		P pr(r, 'R');
		P py(y, 'Y');
		P pb(b, 'B');
		vector<P> plist;
		plist.push_back(pr);
		plist.push_back(py);
		plist.push_back(pb);
		vector<int> ryb = {r,y,b};
		sort(ryb.begin(),ryb.end(),greater<int>());
		if (ryb[0]>n/2) {
			cout << "Case #" << ii << ": " << "IMPOSSIBLE" << "\n";
			continue;
		}

		// ll avg = n/2;
		// cout << avg << "\n";
		// if (r>avg||y>avg||b>avg) {
		// 	cout << "Case #" << ii << ": " << "IMPOSSIBLE" << "\n";
		// 	continue;
		// }
		string ret = "";

		while (true) {
			if (plist[0].first<=0&&plist[1].first<=0&&plist[2].first<=0) {
				break;
			}
			sort(plist.begin(),plist.end());
			ret += plist[2].second;
			if (plist[1].first==0) {
				break;
			}
			ret += plist[1].second;
			plist[2].first--;
			plist[1].first--;
		}

		// while (true) {
		// 	if (r==0&&y==0&&b==0) {
		// 		break;
		// 	}
		// 	if (r>0) {
		// 		ret += "R";
		// 		r--;
		// 	}
		// 	if (y>0) {
		// 		ret += "Y";
		// 		y--;
		// 	}
		// 	if (b>0) {
		// 		ret += "B";
		// 		b--;
		// 	}
		// }
		if (ret[0]==ret[ret.size()-1]) {
			char tmp = ret[ret.size()-2];
			ret[n-2] = ret[n-1];
			ret[n-1] = tmp;
		}
		cout << "Case #" << ii << ": " << ret << "\n";
	}
}
