#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef double ld;
ld D;
int n;
ld K[1010],S[1010];
int main(){
	
	int test;
	cin>>test;
	for(int te=1;te<=test;te++){
		cin>>D>>n;
		ld mn;
		for(int i=0;i<n;i++){
			cin>>K[i]>>S[i];
			if(i==0){
				mn=(D-K[i])/S[i];
			}else{
				mn=max(mn,(D-K[i])/S[i]);
			}
		}
		printf("Case #%d: %.7lf\n",te,D/mn );
	}
	
	return 0;
}