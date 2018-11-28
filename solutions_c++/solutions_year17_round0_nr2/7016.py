#include <bits/stdc++.h>
//#include <math.h>        round-mas cercano, floor-inferior, ceil-superior, trunc-truncar 
#define endl '\n'
#define fast_io() ios_base::sync_with_stdio(0);cin.tie(0)
using namespace std;
typedef long long ll ;
typedef vector<int> vi ;
typedef vector<ll> vll ;
bool bx=0;
vi num(long long x){
	vi y,p;
	while(x>=10){
		y.push_back(x%10);
		x=x/10;
	}
	y.push_back(x);
	for(int i=y.size()-1;i>=0;i--){
		p.push_back(y[i]);
	}
	return p;
}
int main() {
//	fast_io();	
	int t1,t2;
	cin>>t1;
	t2=t1;
	while(t1--){
		long long n;
		cin>>n;
		if(n<10){
			//cout<<n<<endl;
			cout<<"Case #"<<t2-t1<<": "<<n<<endl;
			continue;
		}
		if(n<100){
			int xx=n/10,yy=n%10;
			if(xx>yy){
				cout<<"Case #"<<t2-t1<<": "<<(xx-1)*10+9<<endl;
				continue;
			}
		}
		bx=0;
		vi z=num(n);
		for(int i=1;i<z.size();i++){
			if(z[i-1]>z[i]){
				bx=1;
				break;
			}
		}
		if(!bx){
			cout<<"Case #"<<t2-t1<<": "<<n<<endl;
		}else{
			ll t=0,pi,pp,maxi=0;
			bool b=1;
			for(int i=1;i<z.size();i++){
				t=t*10+9;
			//	cout<<z[0]<<" ";
			}
			//cout<<endl;
			maxi=t;
			//	cout<<t<<endl;
			t=0;
			for(int i=0;i<z.size();i++){
				t=t*10+z[0];
			}
		//	cout<<t<<endl;
			if(t<n){
				if(t>maxi && t<=n)maxi=t;
			}
			t=0;
			for(int i=0;b && i<z.size();i++){
				t=t*10+z[i];
				pp=t;
				for(int j=i+1;j<z.size();j++){
					pp=pp*10+z[i+1];
					if(z[j-1]>z[j]){
						b=0;
						break;
					}
					
				}
			//		cout<<pp<<endl;
				if(pp>maxi && pp<=n)maxi=pp;
			}
			
			int sd=0;
			while( sd<20){
				bool bv=1;
			
			for(int i=1;i<z.size();i++){
				if(z[i-1]>z[i]){
					z[i-1]=z[i-1]-1;
					for(int j=i;j<z.size();j++)
					{
						z[j]=9;
					}
				}
			}
			t=0;
			for(int i=0;i<z.size();i++)
			{
				t=t*10+z[i];
			}
			for(int i=1;i<z.size();i++){
				if(z[i-1]>z[i])bv=0;
			}
		//	cout<<t<<endl;
			if(t>maxi && t<=n && bv)maxi=t;
		sd++;
	}
			cout<<"Case #"<<t2-t1<<": "<<maxi<<endl;
		}
	}
	return 0;
}
