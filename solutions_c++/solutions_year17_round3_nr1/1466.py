#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;


struct cmpop {
	bool operator()(pair<long long, long long> &a, pair<long long, long long> &b) {
		return a.first < b.first || a.first == b.first && a.second > b.second;
	}
} oop;

struct cmpleft {
	bool operator()(pair<long long, long long> &a, pair<long long, long long> &b) {
		return a.first * a.second > b.first * b.second;
	}
} cmpleftop;

void proc(const long long caseno) {
	int n, k;
	vector<pair<long long, long long> > pan;
	scanf("%d %d", &n, &k);
	for (long long i = 0; i < n; i++ ) {
		int r, h;
		scanf("%d %d", &r, &h);
		pan.push_back(make_pair(r, h));
	}

	sort(pan.begin(), pan.end(), oop);


	priority_queue<pair<long long, long long>, vector<pair<long long,long long> >, cmpleft> pq;

	long long total_left = 0;
	long long total_top = 0;
	for (long long i = 0; i < k; i++) {
	//	printf("Adding %lld %lld\n", pan[i].first, pan[i].second);
		total_left += (long long) 2 * pan[i].first * pan[i].second;
		total_top = max(total_top, pan[i].first * pan[i].first);
		pq.push(pan[i]);
	}

	for (long long i = k; i < n; i++) {
		pair<long long, long long> rem = pq.top();

	//	printf("Smallest %lld %lld\n", rem.first, rem.second);
		long long new_left = total_left - (long long)2 * rem.first * rem.second + (long long) 2 * pan[i].first * pan[i].second;
	        long long new_top = max(total_top, pan[i].first * pan[i].first);

		if (new_left + new_top > total_left + total_top) {
			pq.pop();
			pq.push(pan[i]);
			total_left = new_left;
			total_top = new_top;
		}
	}
	
	printf("Case #%lld: %Lf\n", caseno, (long double)(total_left + total_top) * M_PI);


}

int main() {
	int n;
	scanf("%d", &n);
	for (long long i = 0; i < n; i++)
		proc(i  + 1);
	return 0;
}
