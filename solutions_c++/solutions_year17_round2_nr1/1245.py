#include <bits/stdc++.h>
using namespace std;
int u, t=1, d, n, k[1010], s[1010], i;
double fin[1010], mx;
int main(){
	for(cin>>u; t<=u; t++){
		i=mx=0;
		for(cin>>d>>n, i=0; i<n; i++)
			cin>>k[i]>>s[i], fin[i]=(double)(d-k[i])/s[i], mx=max(mx, fin[i]);
		printf("Case #%d: %.6lf\n", t, d/mx);
	}
	return 0;
}
