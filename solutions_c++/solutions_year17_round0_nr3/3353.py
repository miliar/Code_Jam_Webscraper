#include <bits/stdc++.h>
using namespace std;
int t;
long long n,k;
long long a[2],b[2];
long long co[2],co2[2];
bool check(long long h) {
	a[0] = n;
	a[1] = -1;
	co[0]=1;
	co[1] = 0;
	long long nub = 0;
	while(1) {
		long long tmp = nub;
		b[0]=-1;
		co2[0]=0;
		b[1]=-1;
		co2[1]=0;
		for(int i=0;i<2;i++) {
			if(a[i]>h) {
				int left = (a[i]-1)/2;
				int right = a[i]-1-left;
				nub+=co[i];
				if(b[0]==-1 || b[0]==left) {
					b[0]=left;
					co2[0]+=co[i];
				}
				else {
					b[1]=left;
					co2[1]+=co[i];
				}
				if(b[0]==-1 || b[0]==right ) {
					b[0]=right ;
					co2[0]+=co[i];
				}
				else {
					b[1]=right;
					co2[1]+=co[i];
				}
			}
		}
		a[0]=b[0];
		a[1]=b[1];
		co[0]=co2[0];
		co[1]=co2[1];
		if(tmp==nub) break;
	}
	//printf("check %lld %lld\n",h,nub);
	return (k>=nub);
}
long long binary(long long h1, long long h2) {
	//printf("%lld %lld\n",h1,h2);
	if(h1==h2) return h1;
	long long mid = (h1+h2)/2;
	if(!check(mid)) return binary(mid+1,h2);
	return binary(h1,mid);
}
int main() {
	cin >> t;
	int no = 0;
	while(t--) {		
		no++;
		cin >> n >> k;
		k--;
		long long temp = binary(0,n);
		printf("Case #%d: ",no);
		cout << (temp)/2 << " " << ((temp-1)/2) << endl;
	}
}