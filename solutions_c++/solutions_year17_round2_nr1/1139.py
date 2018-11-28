#include <bits/stdc++.h>
#define MAX 100001
#define ll long long
using namespace std;

int n;
double t[MAX],d;

int main(){
	freopen("large.in","r",stdin);
	freopen("large.out","w",stdout);
	int ts,cs = 1;
	cin >> ts;
	while(ts--){
		cin >> d >> n;
		double mx = 0;
		for (int i=0;i<n;i++){
			double k,s;
			cin >> k >> s;
			t[i] = (d-k)/s;
			mx = max(mx,t[i]);
		}
		printf("Case #%d: %f\n",cs++,d/mx);
	}
	return 0;
}