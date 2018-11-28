#include<iostream>
#include<cstdio>
using namespace std;
typedef long long ll;

int main(){
	int t;
	ll n;
	scanf("%d", &t);
	for(int tcase=1;tcase<=t;tcase++){
		printf("Case #%d: ", tcase);
		scanf("%I64d", &n);
		ll trial, inc;
		trial=0;
		inc=0;
		while(inc*10+1<=n){
			inc=inc*10+1;
		}
		int cnt;
		while(inc!=0){
			while(trial+inc<=n&&trial%(inc*9+1)%10!=9){
				trial+=inc;
				cnt++;
			}
			inc/=10;
			cnt=0;
		}
		printf("%I64d\n", trial);
	}
	return 0;
}
