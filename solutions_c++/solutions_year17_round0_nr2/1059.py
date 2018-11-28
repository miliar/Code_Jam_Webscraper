#include <bits/stdc++.h>

using namespace std;

int main()
{
	int ntc;
	scanf("%d", &ntc);
	for (int itc = 1; itc <= ntc; ++itc) {
		printf("Case #%d: ", itc);
		string N;
		cin >> N;
		int l = N.size();
		bool changed = true;
		while (changed) {
			changed = false;
			for (int i = 0; i+1 < l; ++i) {
				if (N[i] > N[i+1]) {
					N[i] = N[i]-1;
					for (int j = i+1; j < l; ++j) {
						N[j] = '9';
					}
					changed = true;
					break;
				}
			}
			/* cout << N << endl; */
		}
		for (int i = 0; i < l; ++i)
			if (N[i] != '0') printf("%c", N[i]);
		puts("");
		continue;
		
	}
	return 0;
}
