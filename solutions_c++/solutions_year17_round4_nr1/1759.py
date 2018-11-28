#include <bits/stdc++.h>
#define MAX 300001
#define M 1000000007
#define ll long long
#define ld long double
#define ESP 0.0001
using namespace std;

int main(){
	freopen("small.in","r",stdin);
	freopen("small.out","w",stdout);
	int t,cs = 1;
	cin >> t;
	while(t--){
		int n,p;
		cin >> n >> p;
		int a[n];
		int m[10];
		memset(m,0,sizeof(m));
		for (int i=0;i<n;i++){
			cin >> a[i];
			a[i]%=p;
			m[a[i]]++;
		}
		int cn = 0;
		if (p==2){
			cn+=m[0];
			if (m[1]%2==0) cn+=m[1]/2;
			else cn+=m[1]/2+1;
		}
		else if (p==3){
			cn+=m[0];
			int mn = min(m[1],m[2]);
			cn+=mn;
			m[1]-=mn;
			m[2]-=mn;
			cn+=m[1]/3;
			m[1]%=3;
			cn+=m[2]/3;
			m[2]%=3;
			if (m[1] || m[2]) cn++;
		}
		printf("Case #%d: %d\n",cs++,cn);
	}
	return 0;
}