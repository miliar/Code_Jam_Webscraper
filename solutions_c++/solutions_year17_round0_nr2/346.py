#include <bits/stdc++.h>
using namespace std;

int main() {
	int tc;
	scanf("%d", &tc);

	for (int tt = 1; tt <= tc; ++tt) {
		int N;
		char temp[20];
		scanf("%s", temp);
		N = strlen(temp);

		bool small = false;
		for (int i=0; i<N; ++i) {
			if (small) {
				temp[i] = '9';
				continue;
			}
			
			char cur;
			for (int j='0'; j<='9'; ++j) {
				bool flag = true;
				for (int k=i; k<N; ++k) {
					if (temp[k] < j) {
						flag = false;
						break;
					}
					else if (temp[k] > j)
						break;
				}

				if (flag) cur = j;
			}

			if (cur < temp[i]) small = true;
			temp[i] = cur;
		}

			


		printf("Case #%d: ", tt);
		int i = 0;
		while (temp[i] == '0')
			i++;
		while (i<N)
			printf("%c", temp[i++]);
		puts("");
	}
	return 0;
}

			

