#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <queue>
#include <vector>
#include <functional>
#include <math.h>
#include <iomanip>
#include <utility>

using namespace std;

struct Time {
	int id;
	int c, d;
	Time(int id, int c, int d) : id(id), c(c), d(d) {}
};

vector<Time> a;
vector<int> me, you;
int T, n, m;

bool check(const Time& t1, const Time& t2) {
	return t1.c < t2.c;
}

int main() {

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	cin>>T;
	for (int tt = 0; tt < T; tt++) {
		cin>>n>>m;
		a.clear();
		for (int i = 0; i < n; i++) {
			int r, h;
			cin>>r>>h;
			Time t(0, r, h);
			a.push_back(t);
		}
		for (int i = 0; i < m; i++) {
			int r, h;
			cin>>r>>h;
			Time t(1, r, h);
			a.push_back(t);
		}
		sort(a.begin(), a.end(), check);
		Time last(a[0].id, a[0].c+1440, a[0].d+1440);
		a.push_back(last);
		me.clear();
		you.clear();
		int mine = 0, yours = 0, ours = 0, cut = (n+m)*2;
		for (int i = 0; i < n+m; i++) {
			if (a[i].id==0)
				mine += a[i].d-a[i].c;
			else
				yours += a[i].d-a[i].c;
			if (a[i].id==a[i+1].id) {
				if (a[i].id==0)
					me.push_back(a[i+1].c-a[i].d);
				else
					you.push_back(a[i+1].c-a[i].d);
			}
			else {
				cut -= 1;
				ours += a[i+1].c-a[i].d;
			}
		} 
		sort(me.begin(), me.end());
		sort(you.begin(), you.end());
		for (auto t : me)
			if (mine+t<=720) {
				mine += t;
				cut -= 2;
			}
		for (auto t : you)
			if (yours+t<=720) {
				yours += t;
				cut -= 2;
			}
		cout<<"Case #"<<tt+1<<": "<<cut<<endl;
	}
	return 0;
}