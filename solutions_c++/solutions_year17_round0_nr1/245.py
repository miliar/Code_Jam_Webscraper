#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;

int main(){
	int T; scanf("%d", &T);
	for(int ti=1;ti<=T;ti++){
		char s[1111]; scanf("%s", s);
		int n = strlen(s);
		int k; scanf("%d", &k);
		int cnt = 0;
		for(int i=0;i<n-k+1;i++){
			if(s[i] == '-'){
				cnt++;
				for(int j=i;j<i+k;j++){
					s[j] = (s[j] == '-' ? '+' : '-');
				}
			}
		}
		bool det = true;
		for(int i=0;i<n;i++) if(s[i] == '-') det = false;
		printf("Case #%d: ", ti);
		if(det) printf("%d\n", cnt);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
