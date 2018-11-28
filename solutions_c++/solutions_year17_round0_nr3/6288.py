//pragun
#include <iostream>
#include <cmath>
#define ll long long int 
using namespace std;
ll bathroom(long long int n, long long int k){
int l=floor(log(k)/log(2));
ll pl=pow(2,l);
ll sl=(n-pl)+1;
ll ga=ceil(1.0*sl/pl);
ll ba=floor(1.0*sl/pl);
ll ng =sl-(ba*pl);
if((k-pow(2,l)+1)<=ng){
{
return ga;
}
}
else
{
return ba;
}
}
int main()
{
	int t;	   ll n,k;
	cin>>t;
	for (int i=1;i<=t;i++) {
		cin>>n>>k;
		ll es=bathroom(n,k);
		cout<<"Case #"<<i<<":"<<" ";
		if(es<=1){
			cout<<0<<" "<<0<<endl;
		}else
		{
 ll up=ceil(1.0*(es-1)/2);
			   ll d=floor(1.0*(es-1)/2);
		printf("%lld %lld\n",up,d);
 
	}
	}
	return 0;
}