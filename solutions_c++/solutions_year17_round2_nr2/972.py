#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

void izp(vector< pair<int, char> > *a) {
	cout << "======================izpisujem:\n";
	for(int i=0; i<(*a).size(); ++i) {
		cout << (*a)[i].first << ' ' << (*a)[i].second << endl;
	}
	cout << endl;
}

bool so(pair<int, char> a, pair<int, char> b) {
	return a.first > b.first;
}

bool preveri(vector< pair<int, char> > *a, int n) {
	for(int i=0; i<(*a).size(); ++i) {
		if((*a)[i].first >= (int)((n+1)/2)) return false;
	}
	return true;
}

void manj(vector< pair<int, char> > *a, int za) {
	for(int i=0; i<(*a).size(); ++i) {
		(*a)[i].first -= za;
	}
}

void izpis(vector< pair<int, char> > *barve, vector< pair<int, char> > *same, int k) {
	int barv = 1;
	if((*same)[k].second == 'R') barv = 3;
	else if((*same)[k].second == 'Y') barv = 5;
	cout << (*same)[k].second;
	for(int i=0; i<(*barve)[barv].first; ++i) {
		cout << (*barve)[barv].second;
		cout << (*same)[k].second;
	}
	(*barve)[barv].first = 0;
}

int main() {
	string b = "ROYGBV";
	int t;
	cin >> t;
	for(int i=0; i<t; ++i) {
		cout << "Case #" << i+1 << ": ";
		int n;
		string out = "";
		vector< pair<int, char> > barve, same;
		cin >> n;
		bool flag = false;
		for(int j=0; j<6; ++j) {
			int a;
			cin >> a;
			if(a > (int)(n/2)) {
				flag = true;
			}
			barve.push_back(make_pair(a, b[j]));
		}

		//cout << flag << endl;

		//izp(&barve);
		//cout << n << endl;
		bool con = false;
		for(int j=1; j<6; j+=2) {
			if(barve[j].first == barve[(j+3)%6].first && n == barve[j].first * 2) {
				for(int i=0; i<n/2; ++i) {
					cout << barve[(j+3)%6].second;
					cout << barve[j].second;
				}
				cout << endl;
				con = true;
				break;
			}
			if(barve[j].first >= barve[(j+3)%6].first && barve[j].first > 0) {
				flag = true;
				//cout << j << " 11111111111111111111111111111111111111\n";
			}
			barve[(j+3)%6].first -= barve[j].first;
			n -= 2*barve[j].first;
		}
		if(con) continue;

		//izp(&barve);
		//cout << flag << endl;

		for(int j=0; j<6; j+=2) {
			if(barve[j].first > (int)(n/2)) {
				flag = true;
			}
			same.push_back(barve[j]);
		}
		//cout << flag << endl;

		if(flag) {
			cout << "IMPOSSIBLE\n";
			continue;
		}
		sort(same.begin(), same.end(), so);
		for(int j=0; j<same.size(); ++j) out += same[j].second;
		while(preveri(&same, n) && same[same.size()-1].first > 0) {
			for(int k=0; k<3; ++k) {
				izpis(&barve, &same, k);
			}
			manj(&same, 1);
			n-=3;
		}
		/*if(!preveri(&same, n+1)) {
			cout << "IMPOSSIBLE\n";
			continue;
		}*/
		//cout << izp;
		for(int j=0; j<same[2].first; ++j) {
			izpis(&barve, &same, 0);
			izpis(&barve, &same, 2);
		}
		for(int j=0; j<same[1].first; ++j) {
			izpis(&barve, &same, 0);
			izpis(&barve, &same, 1);
		}
		cout << endl;
	}
	return 0;
}