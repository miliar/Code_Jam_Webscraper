#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
	int T; cin >> T;
	for(int z = 0; z < T; z++) {
		int N, C, M; cin >> N >> C >> M;
		int purchased[C+1];
		int filled[N+1];
		int filled_part[N+1];
		int required[N+1];
		for(int i = 0; i < C+1; i++) {
			purchased[i] = 0;
		}
		for(int i = 0; i < N+1; i++) {
			filled[i] = 0;
			filled_part[i] = 0;
			required[i] = 0;
		}
		for(int i = 0; i < M; i++) {
			int pos, buy; cin >> pos >> buy;
			purchased[buy]++;
			filled[pos]++;
		}
		int max_req = -1;
		int to_change = 0;
		int largest_customer = -1;
		for(int i= 1; i < C+1; i++) {
			if(purchased[i] > largest_customer) {
				largest_customer = purchased[i];
			}
		}
		for(int i = 1; i < N+1; i++) {
			filled_part[i] = filled_part[i-1] + filled[i];
			required[i] = (filled_part[i] + i - 1) / i;
			if(required[i] > max_req) max_req = required[i];
		}
		max_req = max(max_req, largest_customer);
		for(int i = 1; i < N+1; i++) {
			 if(filled[i] > max_req) {
			 	to_change += filled[i] - max_req;
			 }
		}
		cout << "Case #" << z+1 << ": " << max_req << " " << to_change << endl;

	}
}