#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;

int T;
ll n;

int main(){
	scanf("%d\n", &T);
	for(int c=1; c<=T; c++){
		scanf("%lld", &n);
		ll nn = n;
		vector<int> vn;		
		while(n>0){
			vn.push_back(n%10);
			n/=10;
		}
		reverse(vn.begin(), vn.end());
		int tam = vn.size(), fd=-1;
		for(int i=1; i<tam; i++){
			if(vn[i]<vn[i-1]){
				fd = i;
				break;
			}
		}
		printf("Case #%d: ", c);
		if(fd==-1){
			printf("%lld\n", nn);
		}
		else{
			int bb=-1;
			for(int i=fd; i>=0; i--){
				if(i==0 || (vn[i]>vn[i-1])){
					bb = i;
					break;
				}
			}
			//printf("%d %d*\n", bb, fd);
			vector<int> ans;
			for(int i=0; i<bb; i++){
				ans.push_back(vn[i]);
			}
			ans.push_back(vn[bb]-1);
			for(int i=bb+1; i<tam; i++){
				ans.push_back(9);
			}
			int i=0;
			while(ans[i]==0) i++;
			for(; i<tam; i++){
				printf("%d", ans[i]);
			}		
			printf("\n");
		}
	}
	return 0;
}
