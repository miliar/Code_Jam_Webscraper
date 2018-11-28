#include <iostream>
#include <cstdio>
#include <stack>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <set>
#include <map>
#include <cmath>

#define INF 20000000000000000
#define MOD 1000000007
#define PI acos(-1.0)

using namespace std;

int main() {
	int testCnt;
	cin >> testCnt;
	for (int testNum = 1; testNum <= testCnt; testNum++) {
		cout << "Case #" << testNum <<": ";
		int cam, jam;
		cin >> cam >> jam;
		vector< pair<int, int> > cc, jj;
		vector< pair<int, int> > all;
		int cSum = 0, jSum = 0;
		for (int i = 0; i < cam; i++) {
			int a, b;
			cin >> a >> b;
			cc.push_back(make_pair(a, b));
			cSum += b - a;
		}
		for (int i = 0; i < jam; i++) {
			int a, b;
			cin >> a >> b;
			jj.push_back(make_pair(a, b));
			jSum += b - a;
		}
		int day[720 * 2];
		for (int i = 0; i < 1440; i++)
			day[i] = 0;
		for (int i = 0; i < cc.size(); i++)
			for (int j = cc[i].first; j < cc[i].second; j++)
				day[j] = 1;
		for (int i = 0; i < jj.size(); i++)
			for (int j = jj[i].first; j < jj[i].second; j++)
				day[j] = -1;
		int mid = 0;
		int prev = 0, prevEnd = 0;
		int ans = 0;
		int cAdd = 0, jAdd = 0, cEnd = 0, cStart = 0, jEnd = 0, jStart = 0;
		vector<int> cdiffs, jdiffs;
		int ANS = 1000000;
		for (int i = 0; i < 1440; i++) {
			if (day[i] == 0)
				continue;
			else if (day[i] == -1) {
				if (prev == 1) { 
					mid += i - prevEnd - 1;
					ans++;
				}
				else if (prev == -1 && prevEnd < i - 1) {
					jdiffs.push_back(i - 1 - prevEnd);
					jAdd += i - 1 - prevEnd;
				}
				prev = -1;
				prevEnd = i;
			}
			else {
				if (prev == -1) {
					mid += i - prevEnd - 1;
					ans++;
				}
				else if (prev == 1 && prevEnd < i - 1) {
					cdiffs.push_back(i - 1 - prevEnd);
					cAdd += i - 1 - prevEnd;
				}
				prev = 1;
				prevEnd = i;	
			}
		}
		for (int i = 0; true; i++) {
			if (day[i] == 1) {
				cStart += i;
				break;
			}
			if (day[i] == -1) {
				jStart += i;
				break;
			}
		}
		for (int i = 1439; true; i--) {
			if (day[i] == 1) {
				cEnd += 1440 - i - 1;
				break;
			}
			if (day[i] == -1) {
				jEnd += 1440 - i - 1;
				break;
			}	
		}
		int e = day[1439], s = day[0];
		if (cEnd > 0)
			e = 1;
		if (jEnd > 0)
			e = -1;
		if (cStart > 0)
			s = 1;
		if (jStart > 0)
			s = -1;
		if (e != s)
			ans++;
		if (cSum + cAdd + cStart + cEnd <= 720 && jSum + jAdd + jStart + jEnd <= 720) {
			cout << ans << endl;
		}
		else if (cSum + cAdd + cStart + cEnd > 720) {
			sort(cdiffs.begin(), cdiffs.end());
			reverse(cdiffs.begin(), cdiffs.end());
			int remSum = 0;
			for (int i = 0; i <= cdiffs.size(); i++) {
				if (i > 0)
					remSum += cdiffs[i - 1];
				if (cSum + cAdd - remSum + cStart + cEnd <= 720) {
					cout << ans << endl;
					break;
				}
				if (cSum + cAdd - remSum + cStart <= 720) {
					if (e == 1 && s == 1)
						cout << ans + 2 << endl;
					else
						cout << ans << endl;
					break;
				}
				if (cSum + cAdd - remSum + cEnd <= 720) {
					if (e == 1 && s == 1)
						cout << ans + 2 << endl;
					else
						cout << ans << endl;
					break;
				}
				if (cSum + cAdd - remSum <= 720) {
					cout << ans + 2 << endl;
					break;
				}
				ans += 2;
			}
		}
		else {
			sort(jdiffs.begin(), jdiffs.end());
			reverse(jdiffs.begin(), jdiffs.end());
			int remSum = 0;
			for (int i = 0; i <= jdiffs.size(); i++) {
				if (i > 0)
					remSum += jdiffs[i - 1];
				if (jSum + jAdd - remSum + jStart + jEnd <= 720) {
					cout << ans << endl;
					break;
				}
				if (jSum + jAdd - remSum + jStart <= 720) {
					if (e == -1 && s == -1)
						cout << ans + 2 << endl;
					else
						cout << ans << endl;
					break;
				}
				if (jSum + jAdd - remSum + jEnd <= 720) {
					if (e == -1 && s == -1)
						cout << ans + 2 << endl;
					else
						cout << ans << endl;
					break;
				}
				if (jSum + jAdd - remSum <= 720) {
					cout << ans + 2 << endl;
					break;
				}
				ans += 2;
			}
		}
	}
	return 0;
}