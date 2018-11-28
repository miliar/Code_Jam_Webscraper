#include <bits/stdc++.h>
#define F first
#define S second
#define X real()
#define Y imag()
using namespace std;
typedef long long ll;
typedef long double ld;

void solve(){
	int n,p;
	cin>>n>>p;
	if (p==2){
		int c0=0;
		int c1=0;
		for (int i=0;i<n;i++){
			int a;
			cin>>a;
			if (a%2) c1++;
			else c0++;
		}
		cout<<c0+(c1+1)/2<<endl;
	}
	else if(p==3){
		int c0=0;
		int c1=0;
		int c2=0;
		for (int i=0;i<n;i++){
			int a;
			cin>>a;
			if (a%3==0) c0++;
			else if(a%3==1) c1++;
			else c2++;
		}
		int t=min(c1, c2);
		c1-=t;
		c2-=t;
		cout<<c0+t+(c1+2)/3+(c2+2)/3<<endl;
	}
	else if(p==4){
		int c0=0;
		int c1=0;
		int c2=0;
		int c3=0;
		for (int i=0;i<n;i++){
			int a;
			cin>>a;
			if (a%4==0) c0++;
			else if(a%4==1) c1++;
			else if(a%4==2) c2++;
			else c3++;
		}
		int t=c2/2;
		c2%=2;
		int u=min(c1, c3);
		c1-=u;
		c3-=u;
		int v=0;
		if (c2>0&&c1>0){
			v=min(c2, c1/2);
			c2-=v;
			c1-=2*v;
		}
		int w=0;
		if (c2>0&&c3>0){
			w=min(c2, c3/2);
			c2-=w;
			c3-=2*w;
		}
		assert(c0>=0&&c1>=0&&c2>=0&&c3>=0);
		if (c2>0){
			c1=0;
			c3=0;
		}
		int nz=0;
		if (c1>0) nz++;
		if (c2>0) nz++;
		if (c3>0) nz++;
		assert(nz<=1);
		cout<<c0+t+u+v+w+(c1+3)/4+(c2+1)/2+(c3+3)/4<<endl;
	}
	else{
		assert(0);
	}
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int tcs;
	cin>>tcs;
	for (int tc=1;tc<=tcs;tc++){
		cout<<"Case #"<<tc<<": ";
		solve();
	}
}