#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <vector>

using namespace std;

struct Task{
	int s, e, p;
};

bool cmp(Task a, Task b){
	return a.s < b.s;
}

int main(){
	int T;
	cin >> T;
	for (int K = 1; K <= T; K++){
		int a, b, ta, tb;
		ta = tb = 720;
		cin >> a >> b;
		Task t[205];
		for (int i = 0; i < a; i++){
			cin >> t[i].s >> t[i].e;
			t[i].p = 0;
			ta -= t[i].e - t[i].s;
		}
		for (int i = a; i < a + b; i++){
			cin >> t[i].s >> t[i].e;
			t[i].p = 1;
			tb -= t[i].e - t[i].s;
		}
		sort(t, t + a + b, cmp);
		vector<int> ag, bg;
		int cnt = 0;
		for (int i = 1; i < a + b; i++){
			if (t[i].p == t[i - 1].p){
				if (t[i].p == 0) ag.push_back(t[i].s - t[i - 1].e);
				else bg.push_back(t[i].s - t[i - 1].e);
			} else cnt++;
		}
		if (t[0].p == t[a + b - 1].p){
			if (t[0].p == 0) ag.push_back(t[0].s + 1440 - t[a + b - 1].e);
			else bg.push_back(t[0].s + 1440 - t[a + b - 1].e);
		} else cnt++;
		sort(ag.begin(), ag.end());
		sort(bg.begin(), bg.end());
		for (int i = 0; i < ag.size(); i++){
			if (ag[i] <= ta){
				ta -= ag[i];
			} else {
				cnt += (ag.size() - i) * 2;
				break;
			}
		}
		for (int i = 0; i < bg.size(); i++){
			if (bg[i] <= tb){
				tb -= bg[i];
			} else {
				cnt += (bg.size() - i) * 2;
				break;
			}
		}
		cout << "Case #" << K << ": ";
		cout << cnt << endl;
	}
	
	return 0;
}
