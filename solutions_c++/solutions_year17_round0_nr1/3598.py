#include <cstdio>
#include <cstring>

using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	char s[1001];
	int k, n, result = 0;
	for(int q=1;q<=t;q++) {
		result = 0;
		scanf("%s %d", s, &k);
		printf("Case #%d: ", q);
		n = strlen(s);
		for(int i=0; i<=n-k;i++) {
			if(s[i] == '-') {
				result++;
				s[i] = '+';
				for(int j=i+1;j<i+k;j++) {
					if(s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
			}
		}
		for(int i=n-k+1; i<n;i++)
			if(s[i] == '-') {
				result = -1;
				break;
			}
		
		if(result == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", result);
	}
	return 0;
}
