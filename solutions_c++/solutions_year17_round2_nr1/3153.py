#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
	int t=1;
	cin>>t;
	for(int cases =1;cases<=t;cases++){
		double d;ll n;
		cin>>d>>n;
		double a[n][2];
		for(int i=0;i<n;i++){
			double k,s;
			cin>>k>>s;
			a[i][0]=k;
			a[i][1]=s;
		}
		double time[n];
		for(int i=0;i<n;i++){
			time[i]=double(d-a[i][0])/double(a[i][1]);
		}
		double temp=0;
		for(int i=0;i<n;i++){
			if(time[i]>temp) temp=time[i];
		}
		setprecision(6);
		double x=d/temp;
		cout<<"Case #"<<cases<<": ";cout<<fixed<<showpoint<<setprecision (6)<<x;cout<<endl;

	}
}