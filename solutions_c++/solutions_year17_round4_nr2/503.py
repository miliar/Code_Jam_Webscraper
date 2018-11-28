#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pii;
typedef vector<ll> vi;
typedef vector<vi> vvi;
typedef vector<pii> vp;

int N,C,M;
vp tix;
set<int> seen[1005];

int use[1005][1005];

bool test_ride(int m) {
	for (int i=0; i<m; i++)
		seen[i].clear();

	//cout << "Starting " << m << endl;
	for (int i=0; i<tix.size(); i++) {
		pii p = tix[i];
		int rd;
		for (rd=0; rd<m; rd++) {
			if (seen[rd].count(p.second) == 0) {
				//cout << "Assigned " << p.first << " " << p.second << " to " << rd << endl;
				seen[rd].insert(p.second);
				break;
			}
		}
		if (rd==m || i/m >= p.first) {
			//cout << "Fail " << rd << " " << i << " " << p.first << endl;
			return false;
		}
	}

	return true;
}

int min_prom(int m) {
	for (int i=0; i<m; i++) {
		for (int j=0; j<=N; j++) {
			use[i][j] = 0;
		}
	}

	int prom=0;
	//cout << "Starting " << m << endl;
	for (int i=0; i<tix.size(); i++) {
		pii p = tix[i];
		int rd;
		for (rd=0; rd<m; rd++) {
			if (use[rd][p.first] == 0) {
				//cout << "Assigned " << p.first << " " << p.second << " to " << rd << endl;
				use[rd][p.first] = p.second;
				break;
			}
		}
		if (rd==m) {
			prom++;
		}
	}

	return prom;
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0);
	int T;
	cin >> T;
	for (int Tct=1; Tct<=T; Tct++) {
		cout << "Case #" << Tct << ": ";
		tix.clear();
		cin >> N >> C >> M;
		for (int i=0; i<M; i++) {
			int P,B;
			cin >> P >> B;
			tix.push_back(make_pair(P,B));
		}

		sort(tix.begin(),tix.end());

		int rides;		
		for (rides=1; rides<=1000; rides++)
			if (test_ride(rides)) break;
			
		cout << rides << " " << min_prom(rides) << endl;
	}
}

