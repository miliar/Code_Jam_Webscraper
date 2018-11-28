#include <bits/stdc++.h>
using namespace std;

long long t,d,n,caso;
double k,s,tempo,maxi;

int main(){
	cin >> t;
	caso=1;
	while(t--){
		maxi=-1;
		cin >> d >> n;
		for(int i=0;i<n;i++){
			cin >> k >> s;
			tempo=(d-k)/s;
			maxi=max(maxi,tempo);
		}
		printf("Case #%lld: %.6lf\n",caso,d/maxi);
		caso++;
	}
}