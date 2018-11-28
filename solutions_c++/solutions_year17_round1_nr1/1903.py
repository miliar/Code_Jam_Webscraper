#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <queue>

using namespace std;

const string IMP = "IMPOSSIBLE";
typedef unsigned long long int ll;

void solve(vector<string>& vs, vector<string>& vr, int st = 0) {

	int r = vs.size();
	int c = vs[0].size();
	int X = st;
	///
	/*cout<<"BEFORE" <<endl;
	for(int i=0; i<r; ++i)
		cout << vr[i] << endl;
	cout<<endl;*/
	vector<pair<char, int>> pos;
	while (true) {
		for (int i = 0; i<r; ++i) {
			if (vs[i][X] != '?') {
				pos.push_back(make_pair(vs[i][X], i));
			}
		}
		if(!pos.empty())
			break;
		X++;
	}

	int Y = X+1;
	while (Y<c) {
		bool f = false;
		for (int i = 0; i<r; ++i) {
			if (vs[i][Y] != '?') {
				f = true;
				break;
			}
		}
		if (f)
			break;
		Y++;
	}

	int xx = 0;
	char last = 'X';
	for (int i = 0; i< pos.size(); ++i) {
		///
		//cout<<"YO: " <<pos[i].first << " " << pos[i].second << endl;;
		int yy = pos[i].second;
		last = pos[i].first;
		for (int j = xx; j <= yy; ++j) {
			for (int k = st ; k<Y; ++k) {
				vr[j][k]=pos[i].first;
			}
		}
		xx = yy+1;
	}
	for (int j = xx; j < r; ++j) {
		for (int k = st ; k<Y; ++k) {
			vr[j][k]=last;
		}
	}
	/*///
	cout<<"STEP" <<endl;
	for(int i=0; i<r; ++i)
		cout << vr[i] << endl;
	cout<<endl;*/

	if (Y != c)
		solve(vs, vr, Y);
}

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {
    printf("Case #%d:", qq);
		cout<<endl;
		int r, c;
		cin >> r >> c;
		vector<string> vs(r);
		vector<string> vr(r);
		for(int i=0; i<r; ++i) {
			cin >> vs[i];
			vr[i] = vs[i];
		}
		solve(vs, vr);
		for(int i=0; i<r; ++i)
			cout << vr[i] << endl;
  }
  return 0;
}
