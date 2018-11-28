#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <iostream>
#include <vector>
#include <cstring>
#include <stack>

using namespace std;
int stall[1005];

int main(){
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;test++){
		long long n,k;
		scanf("%lld %lld", &n, &k);
		memset(stall,0,sizeof(stall));
		stall[0] = stall[n+1] = 1;
		for(int i=0;i<k;i++){
			int maxA=-1, maxB=-1;
			int ind = -1;
			for(int j=1;j<=n;j++) if(!stall[j]){
				int ls,rs;
				for(ls=j-1;ls>=0;ls--) if(stall[ls]) break;
				for(rs=j+1;rs<=n+1;rs++) if(stall[rs]) break;
				ls = j - ls - 1;
				rs = rs - j - 1;
				int a = min(ls,rs);
				int b = max(ls,rs);
				//printf("%d %d %d\n",j, a,b);
				if(a>maxA){
					ind=j;
					maxA = a;
					maxB = b;
				}else if(a==maxA){
					if(b>maxB){
						ind = j;
						maxB = b;
					}
				}
			}
			if(i+1==k) { printf("Case #%d: %d %d\n",test, maxB,maxA); break; }
			stall[ind]=1;
		}
	}
	return 0;
}