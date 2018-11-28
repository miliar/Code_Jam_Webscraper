#include <iostream>
#include <string>

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		string S;
		int K;
		cin >> S >> K;
		int count = 0;
		int curr = 0;
		for( ; curr + K <= S.size(); curr++) {
			if(S[curr] == '-') {
				count++;
				for(int i = curr; i < curr + K; i++)
					S[i] = (S[i] == '-') ? '+' : '-'; 
			}
		}
		bool valid = true;
		while(curr < S.size()) {
			if(S[curr] == '-') valid = false;
			curr++;
		}
		if(!valid)
			printf("Case #%d: IMPOSSIBLE\n", t);	
		else
			printf("Case #%d: %d\n", t, count);
	}
}
