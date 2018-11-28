#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;

int t[60*24+1][60*12+1][2];
// 0 - C, 1 - J

const int INF = 1e7;

int main() {
	
	int test;
	cin>>test;
	for (int testc = 1; testc<=test; testc++) {
		int ac, aj;
		cin>>ac>>aj;
		
		vector<pair<int,int>> cjob;
		vector<pair<int,int>> jjob;
		
		for (int i = 0; i < ac; i++) {
			int tmp1, tmp2;
			cin >> tmp1 >> tmp2;
			cjob.push_back(make_pair(tmp1, tmp2));
		}
		
		
		for (int i = 0; i < aj; i++) {
			int tmp1, tmp2;
			cin >> tmp1 >> tmp2;
			jjob.push_back(make_pair(tmp1, tmp2));
		}
		
		sort(cjob.begin(), cjob.end());
		sort(jjob.begin(), jjob.end());
		
		if (ac < 2 && aj < 2) {
			printf("Case #%d: %d\n", testc, 2);
			continue;
		}
		
		if (ac == 2) {
			if (cjob[1].second - cjob[0].first <= 720) {
				printf("Case #%d: %d\n", testc, 2);
				continue;
			}
			if (1440 + cjob[0].second - cjob[1].first <= 720) {
				printf("Case #%d: %d\n", testc, 2);
				continue;
			}
			printf("Case #%d: %d\n", testc, 4);
			continue;
		}
		
		
		if (aj == 2) {
			if (jjob[1].second - jjob[0].first <= 720) {
				printf("Case #%d: %d\n", testc, 2);
				continue;
			}
			if (1440 + jjob[0].second - jjob[1].first <= 720) {
				printf("Case #%d: %d\n", testc, 2);
				continue;
			}
			printf("Case #%d: %d\n", testc, 4);
			continue;
		}
		
		
	}
	return 0;
}



