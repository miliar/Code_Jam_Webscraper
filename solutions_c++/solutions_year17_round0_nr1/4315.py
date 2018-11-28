#include <iostream>
#include <string>

using namespace std;

int solve(string &s, int K)
{
	int ret = 0;
	int len = s.size();
	int i = 0;
	while(i < len) {
		if(s[i] == '+') {
			i++;
		} else {
			if( K <= (len - i)) {
				ret++;
				for(int flip = 0; flip < K; flip++) {
					if(s[flip + i] == '-') {
						s[flip + i] = '+';
					} else {
						s[flip + i] = '-';
					}
				}
			} else {
				return -1;
			}
		}
	}
	return ret;
}

int main(void)
{
	int N, i;
	string s;
	cin >> N;

	for(i=0; i<N; i++) {
		int K, ret;
		cin >> s >> K;
		cout << "Case #" << i + 1 << ": ";
		ret = solve(s, K);
		if(ret >= 0) {
			cout << ret;
		} else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;		
	}
}