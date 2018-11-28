//
//  main.cpp
//  17_round_2_A
//
//
//
//

#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	freopen("A-large.in.txt", "r", stdin);
	freopen("A-large.out.txt", "w", stdout);
	int t, n, p, freq[4], k, ans;
	scanf("%d", &t);
	for(int i=1; i<=t; i++){
		for(int j=0; j<4; j++) freq[j]=0;
		scanf("%d %d", &n, &p);
		for(int j=0; j<n; j++){
			scanf("%d", &k);
			freq[k%p]++;
		}
		ans=freq[0];
		if(p==2) ans+=(freq[1]+1)/2;
		else if(p==3){
			if(freq[1]<freq[2]) ans+=freq[1]+(freq[2]-freq[1]+2)/3;
			else ans+=freq[2]+(freq[1]-freq[2]+2)/3;
		}
		else if(p==4){
			k=freq[2]/2;
			freq[2]%=2;
			ans+=k;
			k=min(freq[1], freq[3]);
			ans+=k;
			freq[1]-=k;
			freq[3]-=k;
			if(freq[2]!=0){
				if(freq[3]==0){
					ans++;
					freq[1]-=2;
				}else if(freq[1]==0){
					ans++;
					freq[3]-=2;
				}else printf("ERROR\n");
			}
			ans+=(freq[1]+freq[3]+3)/4;
		}
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}
