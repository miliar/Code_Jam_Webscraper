#include <bits/stdc++.h>
using namespace std;

void doCase(int t) {
	int N, C, M;
	cin >> N >> C >> M;
	
	vector<pair<int, int>> tickets(M);
	for (int i=0; i<M; i++) {
		cin >> tickets[i].first >> tickets[i].second;
		tickets[i].first--;
		tickets[i].second--;
	}
	
	vector<int> persCount(C);
	vector<int> posCount(N);
	for (int i=0; i<M; i++) {
		persCount[tickets[i].second]++;
		posCount[tickets[i].first]++;
	}
	
	int rides = 0;
	for (int i=0; i<C; i++)
		rides = max(persCount[i], rides);
	int stickets = 0;
	for (int i=0; i<N; i++) {
		stickets += posCount[i];
		rides = max(rides, (stickets+i)/(i+1));
	}
	
	int promos = 0;
	for (int i=0; i<N; i++) {
		promos += max(0, posCount[i]-rides);
	}
	
	cout << "Case #" << t << ": " << rides << " " << promos << endl;
}

int main() {
	int T;
	cin >> T;
	for (int i=0; i<T; i++)
		doCase(i+1);
	return 0;
}
