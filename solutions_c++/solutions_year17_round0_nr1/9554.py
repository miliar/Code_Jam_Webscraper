#include <cstdio>
#include<cstring>
#include<iostream>
using namespace std;
int main()
{
	int T;
	scanf("%d ", &T);
	for (int i = 1; i <= T; i++){
		int result = 0;
		int cnt = 0;
		int k;
		char s[1001];
		scanf("%s", s);
		scanf("%d", &k);
		for (int j = 0; j < strlen(s); j++){
			if (s[j] == '-'){
				result++;
				if (j + k > strlen(s)) break;
				for (int m = 0; m < k; m++){
					if (s[j + m] == '-')
						s[j + m] = '+';
					else
						s[j + m] = '-';
				}
			}
		}
		for (int n = 0; n < strlen(s); n++)
			if (s[n] == '+')cnt++;

		if (cnt == strlen(s))
			cout << "Case #" << i << ": " << result << endl;
		else
			cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
	}
	return 0;
}