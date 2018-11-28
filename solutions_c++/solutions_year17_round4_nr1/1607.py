#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main(){
	int T,P,N;
	int ans,tmp;
	int a[5];
	scanf("%d",&T);
	for(int ca = 1; ca<=T; ++ca){
		scanf("%d %d",&N,&P);
		memset(a,0,sizeof(a));
		for(int i=0;i<N;++i){
			scanf("%d",&a[4]);
			++a[a[4] % P];
		}
		ans = a[0];
		switch(P){
			case 2:
				ans += a[1] / 2 + a[1] % 2;
				break;
			case 3:
				if(a[1] > a[2]){
					ans += a[2];
					a[1] -= a[2];
					ans += a[1] / 3;
					if(a[1] % 3) ++ans;
				}
				else{
					ans += a[1];
					a[2] -= a[1];
					ans += a[2] / 3;
					if(a[2] % 3) ++ans;
				}
				break;
			case 4:
				ans += a[2] / 2;
				if(a[1] > a[3]){
					ans += a[3];
					a[1] -= a[3];
					if(a[2]){
						++ans;
						if(a[1] > 1){
							a[1] -= 2;
							ans += a[1] / 4;
							if(a[1] % 4) ++ans;
						}
					}
					else{
						ans += a[1] / 4;
						if(a[1] % 4) ++ans;
					}
				}
				else{
					ans += a[1];
					a[3] -= a[1];
					if(a[2]){
						if(a[3] > 1){
							a[3] -= 2;
							ans += a[3] / 4;
							if(a[3] % 4) ++ans;
						}
					}
					else{
						ans += a[3] / 4;
						if(a[3] % 4) ++ans;
					}
				}
				break;
			defalut:
				printf("NOFUCKINGPOSSIBLE\n");
				return 0;
		}
		printf("Case #%d: %d\n",ca,ans);
	}
	return 0;
}
