#include <iostream>
#include <queue>
#include <cmath>
#include <utility>
#define priority first
#define start second.first
#define end second.second
#define mp make_pair
using namespace std;
int T, N, K;
priority_queue< pair< double, pair< int, int > > > pqueue;
pair< double, pair< int, int > > auxval;

void bfs() {
	int mid, ind=1;
	pqueue.push(mp(N-1, mp(0, N-1)));
	while(ind++ <= K) {
		auxval = pqueue.top();
		pqueue.pop();
		//cout << " priority: " << auxval.priority << " start: " << auxval.start << " end: " << auxval.end << "\n";
		mid = (auxval.start+auxval.end)/2;
		pqueue.push(mp((mid-1)-auxval.start, mp(auxval.start, mid-1)));
		pqueue.push(mp(auxval.end-(mid+1), mp(mid+1, auxval.end)));
	}
	while(!pqueue.empty())
		pqueue.pop();
}

int main() {
	cin >> T;
	for(int i=0; i<T; i++) {
		cin >> N >> K;
		bfs();
		cout << "Case #" << i+1 << ": " << ceil(auxval.priority/2) << " " << floor(auxval.priority/2) << "\n";
	}
	return 0;
}