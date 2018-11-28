#include<bits/stdc++.h>
using namespace std;
int main(){
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int tc;
	long long x;
	scanf("%d", &tc);
	for(int i=1; i<=tc; i++){
		scanf("%lld", &x);
		string y = to_string(x);
		int n = y.size();
		if(n==1){
			printf("Case #%d: %lld\n",i, x);
			continue;
		}
		bool flag = false;
		int start = 0;
		for(int j=0; j<n-1; j++){
			if(y[j]<y[j+1]){
				start++;
			}
			else if(y[j]>y[j+1]){
				flag=true;
				break;
			}
		}
		if(flag){
			y[start]-=1;
			for(int j=start+1; j<n; j++){
				y[j]='9';
			}
		}
		 x = stoll(y);
		 printf("Case #%d: %lld\n",i, x);
	}
}
