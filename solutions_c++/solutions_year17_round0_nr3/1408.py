#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int t=1, u, i, now;
ll n, k, l, a[2], b[2], tmp[2], tp[2];
int main(){
	ios::sync_with_stdio(false);
	for(cin>>u; t<=u; t++){
		cin>>n>>k;
		a[0]=a[1]=0;
		a[n%2]++;
		b[n%2]=n;	b[(n+1)%2]=n-1;
		while(k>a[0]+a[1]){
			k-=a[0]+a[1];
			tp[(b[0]/2)%2]=b[0]/2;
			tp[((b[0]-1)/2)%2]=(b[0]-1)/2;
			tmp[tp[0]%2]=a[0];
			tmp[tp[1]%2]=a[0];
			tmp[(b[1]/2)%2]+=2*a[1];
			b[0]=tp[0];		b[1]=tp[1];
			a[0]=tmp[0];	a[1]=tmp[1];
		//	if(b[0]==0)	a[0]=0;
		}
		if(b[0]<b[1]){
			tmp[0]=b[0]; b[0]=b[1]; b[1]=tmp[0];
			tmp[0]=a[0]; a[0]=a[1]; a[1]=tmp[0];
		}
		if(k>a[0])	l=b[1];
		else		l=b[0];
		cout<<"Case #"<<t<<": "<<l/2<<" "<<(l-1)/2<<endl;
	}
	return 0;
}
