#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
	int ca;
	cin >> ca;
	for (int i = 1; i <= ca; i++) {
		priority_queue <pair <int, pair <int, int> > > pq;
		
		int N, K;
		cin >> N >> K;
		pq.push(pair <int, pair <int, int> > (N, pair <int, int> (0, N + 2 - 1)));
		
		for (int j = 0; j < K-1; j++) {
		
			pair <int, pair <int, int> > fr = pq.top();
			pq.pop();

			pair <int, int> aux = fr.second;
			int auxi = fr.first;
			aux.second = aux.first + (fr.first/2) + 1;
			fr.second.first = aux.second;
			auxi = aux.second - aux.first - 1;
			fr.first = fr.second.second - fr.second.first - 1;
			
						
			if (fr.first != 0) {
				pq.push(fr);

			}
			
			if (auxi != 0) {
				pq.push(pair <int, pair <int, int> > (auxi, aux));

			}
		}
		
		cout << "Case #"<<i<<": "<<pq.top().first/2 << " "<<(pq.top().first/2 - (pq.top().first%2==0))<<endl;
		
	}
}