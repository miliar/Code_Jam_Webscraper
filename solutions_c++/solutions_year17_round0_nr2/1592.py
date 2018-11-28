#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	while (T--) {
		static int id = 0;
		long long n;
		scanf("%lld", &n);
		vector<int> dig;
		long long tmp = n;
		while (tmp) {
			dig.push_back(tmp % 10);
			tmp /= 10;
		}
		reverse(dig.begin(), dig.end());
		long long ans = 0;
		bool smaller = false;
		for (int i = 0; i < (int)dig.size(); ++i) {
			int d;
			if (smaller) {
				d = 9;
			} else {
				bool succ = true;
				d = dig[i];
				for (int j = i + 1; j < (int)dig.size(); ++j) {
					if (dig[j] < d) {
						succ = false;
						break;
					} else if (dig[j] > d) {
						break;
					}
				}
				if (!succ) {
					--d;
					smaller = true;
				}
			}
			ans = ans * 10 + d;
		}
		printf("Case #%d: %lld\n", ++id, ans);	
	}
	return 0;
}
