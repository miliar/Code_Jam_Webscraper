#include<bits/stdc++.h>
using namespace std;
#define lli long long int
int main(){
	lli c,z,y,j,n,k,t,i,x;
	cin>>t;
	for(j=1;j<=t;j++){
		cin>>n>>k;
		vector<lli> v[2];
		v[0].resize(63,0);
		v[1].resize(63,0);
		v[0][0]=1;
		for(i=1;i<=62;i++){
			if(v[0][i-1]){
				x=(n>>(i-1));
				if(!x)	break;
				if(x&1){
					v[0][i]+=2*v[0][i-1];
				}
				else{
					v[0][i]+=v[0][i-1];
					v[1][i]+=v[0][i-1];
				}
			}
			if(v[1][i-1]){
				x=((n>>(i-1))-1);
				if(!x)	break;
				if(x&1){
					v[1][i]+=2*v[1][i-1];
				}
				else{
					v[0][i]+=v[1][i-1];
					v[1][i]+=v[1][i-1];
				}
			}
		}
		i=(k)>>1;
		y=1;
		c=0;
		while(i){
			c++;
			i=i>>1;
			y=y<<1;
		}
		z=y;
		z=1+k-z;
		if(v[0][c]>=z){
			c=(n>>c);
		}
		else{
			c=(n>>c)-1;	
		}
		//cout<<c<<endl;
		lli a,b;
		if(c&1){
			a=b=c/2;
		}
		else{
			a=c/2;
			b=(c/2)-1;
		}
		cout<<"Case #"<<j<<": "<<a<<" "<<b<<endl;
	}
	return 0;
}