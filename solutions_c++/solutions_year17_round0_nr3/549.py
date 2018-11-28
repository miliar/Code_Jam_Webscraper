#include <iostream>
#include <queue>
#define ull unsigned long long int
using namespace std;

priority_queue<pair<ull, ull> > pq;	
ull N, K, rmax, rmin, current, followingK, totalK;
bool found;

void process() {
	pq.push(make_pair(N, 1));
	totalK = 0;
	found = false;
	//cout << "We're doing " << N << ", " << K << " now." << endl;
	
	while(!pq.empty()) {
		current = pq.top().first;
		followingK = pq.top().second;
		pq.pop();
		
		while(!pq.empty() && pq.top().first==current) {
			followingK += pq.top().second;
			pq.pop();
		}
		//cout << "Next up is " << current << " with " << followingK << " upcoming Ks" << endl;
		
		totalK += followingK;
		if (totalK >= K) found=true;
		
		if (current && current%2) { //Impar
			if (found) {
				rmax = rmin = current/2;
				break;
			} else {
				pq.push(make_pair(current/2, followingK*2));
			}
		} else {
			if (found) {
				rmax = current/2;
				rmin = rmax-1;
				break;
			} else {
				pq.push(make_pair(current/2, followingK));
				pq.push(make_pair((current/2)-1, followingK));
			}
		}
	}
}

int main() {
	int tc, t;
	cin >> t;
	for(tc=1; tc <= t; ++tc) {
		cin >> N >> K;
		
		process();
		
		cout << "Case #" << tc << ": " << rmax << " " << rmin << endl;
		
		while(!pq.empty())
			pq.pop();
	}
	return 0;
}