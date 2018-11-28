#include<bits/stdc++.h>

char str[2020];

int main()
{
	int K, T;
	freopen("A-large.in", "r", stdin);
	freopen("data.out", "w", stdout);
	std::cin >> T;
	for(int cas = 1; cas <= T; cas ++) {
		std::cin >> str >> K;
		int len = strlen(str);
		std::cout << "Case #" << cas << ": ";
		if(len < K) {
			std::cout << "IMPOSSIBLE" << std::endl;
			continue;
		}
		int cnt = 0;
		for(int i = 0; i + K - 1 < len; i ++) {
			if(str[i] == '-') {
				cnt ++;
				for(int j = i; j < i + K; j ++) {
					if(str[j] == '-') {
						str[j] = '+';
					} else {
						str[j] = '-';
					}
				}
			}
		}
		bool flag = true;
		for(int i = 0; i < len; i ++) {
			if(str[i] == '-') {
				flag = false;
				break;
			}
		}
		if(!flag) {
			std::cout << "IMPOSSIBLE" << std::endl;
		} else {
			std::cout << cnt << std::endl;
		}
	}
	return 0;
}
