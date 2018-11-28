#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fr(a,n) for(int i=a;i<n;i++) 
#define vfr(v) for(vector<int>::iterator it=v.begin();it!=v.end();it++)
int main(){
int T;
cin>>T;
for(int t=1;t<=T;t++){
	double m=0,d,n;
	cin>>d>>n;
	fr(0,n){
		double l,s;
		cin>>l>>s;
		m=max(m,((d-l)/s));
		}
	cout<<"Case #"<<t<<": "<<fixed<<std::setprecision(6)<<d/m <<endl;	
	}	
	
}
