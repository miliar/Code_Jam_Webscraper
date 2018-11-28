#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int m[4];

int main(){
	int t, n, p, v;
	scanf("%d", &t);
	
	for(int z=1; z<=t; z++){
		scanf("%d %d", &n, &p);
		
		memset(m, 0, sizeof(m));
		for(int i=0; i<n; i++){
			scanf("%d", &v);
			m[v%p]++;
		}
		
		int ans = m[0];
		if(p == 2){
			ans += (m[1]+1)/2;
		}else if(p == 3){
			int mn = min(m[1], m[2]);
			ans += mn;
			m[1] -= mn;
			m[2] -= mn;
			ans += (m[1]+2)/3 + (m[2]+2)/3;
		}else if(p == 4){
			ans += (m[2]+1)/2;
			int mn = min(m[1], m[3]);
			ans += mn;
			m[1] -= mn;
			m[3] -= mn;
			if(m[2]%2 == 1){
				ans += (m[1]+1)/4 + (m[3]+1)/4;
			}else{
				ans += (m[1]+3)/4 + (m[3]+3)/4;
			}
		}
		
		printf("Case #%d: %d\n", z, ans);
	}
	
	return 0;
}