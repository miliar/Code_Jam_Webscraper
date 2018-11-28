#include <cstdio>
#include <utility>
#include <vector>
#include <cmath>
#include <algorithm>
#include <queue>

using namespace std;

typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

int caseNum = 0;
unsigned long long stalls;
unsigned long long people;

priority_queue<unsigned long long> intervals;

int main() {
	int t;

	scanf("%d", &t);

	while(t--){
	//	printf("Case %d\n", caseNum	);
		while(intervals.empty() == false) {
				intervals.pop();
		}
		caseNum++;

		scanf("%llu %llu", &stalls, &people);

		intervals.push(stalls);

		if(stalls == people) {
			printf("Case #%d: 0 0\n", caseNum);
			continue;
		}

		//printf("%llu %llu\n", stalls, people);

		for(unsigned long long i = 0; i < people - 1; i++) {
			unsigned long long interval = intervals.top();
		//	printf("%llu\n", interval);
			intervals.pop();
			intervals.push((interval - 1) /2);
			intervals.push((interval) /2);
		}

		unsigned long long ansBase = intervals.top();

		unsigned long long ans1 = ansBase/2;
		unsigned long long ans2 = (ansBase - 1) /2;
		
		printf("Case #%d: ", caseNum);
		printf("%llu %llu", ans1, ans2);

		printf("\n");
	}
}