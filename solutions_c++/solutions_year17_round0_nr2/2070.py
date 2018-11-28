#include <cstdio>
#include <cstring>

char s[505], ss[505];
int cases;

int main() {
	scanf("%d", &cases);
	for(int xx = 1; xx <= cases; ++xx) {
		memset(s, 0, sizeof(s));
		memset(ss, 0, sizeof(ss));
		scanf("%s", s);
		int len = strlen(s);
		bool ok = true;
		for(int i = 1; i < len; ++i){
			if(s[i] < s[i - 1]) {
				// gao problem
				ok = false;
				bool ok2 = false;
				for(int j = i - 1; j >= 1; --j) {
					if(s[j] != s[j - 1]) {
						for(int k = 0; k <= j - 1; ++k)
							ss[k] = s[k];
						ss[j] = s[j] - 1;
						for(int k = j + 1; k < len; ++k)
							ss[k] = '9';
						ok2 = true;
						break;
					}
				}
				if(!ok2) {
					if(s[0] != '1') {
						ss[0] = s[0] - 1;
						for(int j = 1; j < len; ++j)
							ss[j] = '9';
					} else {
						for(int j = 0; j < len - 1; ++j)
							ss[j] = '9';
					}
				}
				break;
			}
		}
		if(ok){
			printf("Case #%d: %s\n", xx, s);
		} else {
			printf("Case #%d: %s\n", xx, ss);
		}
	}
}
