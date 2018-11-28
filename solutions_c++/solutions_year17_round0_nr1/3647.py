#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

int main() {
	int T;
	cin >>T;

	for(int t = 1; t <= T; ++t) {
		string pancakes;
		int K;
		cin >> pancakes >> K;

		int filps = 0;
		int pancakes_count = pancakes.size();
		bool chk = false;
		for(int i = 0; i < pancakes_count; ++i) {
			if(pancakes[i] == '-') {
				if(pancakes_count - i >= K) {
					for(int k = 0, j = i; k < K; ++k, ++j)
						pancakes[j] = pancakes[j] == '+' ? '-' : '+';
					++filps;
				}
				else {
					cout <<"Case #" <<t <<": IMPOSSIBLE"<<endl;
					chk = true;
					break;
				}
			}
		}
		if(!chk)
			cout <<"Case #" <<t <<": " <<filps <<endl;
	}
	return 0;
}