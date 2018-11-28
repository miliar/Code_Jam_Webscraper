#include <bits/stdc++.h>
#define LL long long
#define pb push_back
#define mp make_pair
#define fi first
#define sc second
using namespace std;

int T;
long double d,n,k,s,speed;

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>T;
	for(int tc=1;tc<=T;tc++){
		cin>>d>>n;
		speed = 0.0;
		for(int i=0;i<n;i++){
			cin>>k>>s;
			speed = max(speed, (d-k)/s);
		}
		printf("Case #%d: %.8lf\n", tc, (double)(d/speed));
	}
	return 0;
}
