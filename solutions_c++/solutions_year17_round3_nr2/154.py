#include <bits/stdc++.h> 

using namespace std;

typedef long long ll; 
typedef pair<int, int> pii;

#define REP(i,n) for(int(i)=0;(i)<(int)(n);(i)++)

int cam, jam;
int day[3000];
int forceL[3000];
int forceR[3000];
int day_start;
int cam_time, jam_time;

void read() {
	memset(day,0,sizeof(day));
	cam_time = jam_time = 0;

	scanf("%d %d", &cam, &jam);
	for (int i = 0; i < cam; i++) {
		int st, ed;
		scanf("%d %d", &st, &ed);
		day_start = ed;

		for (int j = st; j < ed; j++) {
			day[j] = day[j+1440] = 1;
		}

		cam_time += ed-st;
	}

	for (int i = 0; i < jam; i++) {
		int st, ed;
		scanf("%d %d", &st, &ed);
		day_start = ed;

		for (int j = st; j < ed; j++) {
			day[j] = day[j+1440] = 2;
		}

		jam_time += ed-st;
	}
}

void solve() {
	int switches = 0;
	int la = -1;

	vector<int> caam;
	vector<int> jaam;
	int miiix = 0;

	for (int i = day_start; i < day_start + 1440; i++) {
		if (day[i] == 1 && day[i-1] != 1) switches++;
		if (day[i] != 1 && day[i-1] == 1) switches++;

		if (day[i] == 0) {
			if (day[i-1] != 0) la = i;
			if (day[i+1] != 0) {
				if (day[la-1] != day[i+1]) miiix += i-la+1;
				else if (day[la-1] == 1) caam.push_back(i-la+1);
				else jaam.push_back(i-la+1);
			}
		}
	}

	sort(caam.begin(), caam.end());
	sort(jaam.begin(), jaam.end());

	int need = 720 - cam_time;
	while (need > 0) {
		if (!caam.empty()) {
			int t = caam.front();
			if (need >= t) {
				need -= t;
				switches -= 2;
			}
			else need = 0;
			caam.erase(caam.begin());
		}

		else if (miiix) {
			need -= miiix;
			miiix = 0;
		}

		else {
			int t = jaam.back();
			need -= t;
			switches += 2;
			jaam.erase(--jaam.end());
		}
	}

	printf("%d\n", switches);
}


























int myMod = 0;
int howMany = 1;

int main(int argc, char** argv) {
	if (argc > 1) {
		stringstream ss; ss << argv[1]; ss >> myMod;
		ss.str(""); ss.clear();
		ss << argv[2]; ss >> howMany;
	}

	int cases;
	scanf("%d", &cases);
	for (int i = 0; i < cases; i++) {
		read();
		if (i % howMany == myMod) {
			printf("Case #%d: ", i+1);
			solve();
		}
	}
}