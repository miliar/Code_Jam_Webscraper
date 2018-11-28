#include <iostream>
#include <queue>

using namespace std;

typedef long long int tint;

#define forsn(i,s,n) for(int i = (s);i < (int)(n);i++)
#define forn(i,n) forsn(i,0,n)



int main() {
	int T; cin >> T;
	
	forn(caso, T) {
		cout << "Case #" << caso + 1 << ": ";
		tint n, k;
		cin >> n >> k;
			
		priority_queue<int> pq;
		pq.push(n + 1);
		forn(i, k - 1) {
			//~ cout << i << endl;
			int current = pq.top(); pq.pop();
			
			int n1 = current / 2;
			int n2 = current - n1;
			
			pq.push(n1);
			pq.push(n2);
		}
		
		int last = pq.top();
		
		cout << (last - (last / 2)) - 1 << ' ' << (last / 2) - 1 << endl;
	}
}
