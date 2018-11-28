#include <cstring>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <map>
#include <set>

using namespace std;


int v[1111];
char str[1111];


int main(){

	int t, k;
	scanf("%d", &t);
	int caso = 1;
	while(t--){
		scanf("%s %d", str, &k);
		int len = strlen(str);

		
		for(int i = 0; i < len; i++) v[i] = (str[i] == '+')?1:0;
		
		int fim = len-k+1;
		int ans = 0;
		for(int i = 0; i < fim; i++){
			if(v[i] == 0){
				for(int j = i; j < i+k; j++){
					v[j] = 1 - v[j];
				}
				ans++;
			}
		}
		bool b = 1;
		for(int i = 0; i < len; i++) b &= v[i];
		if(b) printf("Case #%d: %d\n",caso,  ans);
		else printf("Case #%d: IMPOSSIBLE\n", caso);
		caso++;
	}
	return 0;
}