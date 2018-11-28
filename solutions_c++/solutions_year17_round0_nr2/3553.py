#include <cstdio>
#include <cstring>

using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	char s[20];
	int n;
	for(int q=1;q<=t;q++) {
		scanf("%s", s);
		n = strlen(s);	
		printf("Case #%d: ", q);
		int index = -10;
		for(int i=1;i<n;i++) {
			if(s[i] < s[i-1]) {
				index = i;
				break;
			}
		}
		if(index != -10) {
			int temp = 0;
			for(int i=index-2;i>=0;i--) {
				if(s[i] != s[index-1]) {
					temp = 1;
					index = i+2;
					break;
				}
			}
			if(temp == 0)
				index = 1;
			s[index-1]--;
			for(int i=index; i<n;i++)
				s[i] = '9';
		}
		if(s[0] == '0')
			printf("%s\n", (s+1));
		else
			printf("%s\n", s);
	}
	return 0;
}
