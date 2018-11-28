#include<bits/stdc++.h>
// code_is_life
// vishu_is_cool
// code_is_cool
// life_is_cool
# define rf freopen("input.txt","r",stdin)
# define wf freopen("output.txt","w",stdout)

using namespace std;

typedef long long ll;

int main()
{
	rf;
	wf;
	int test;
	cin>>test;
	int t=test;
	ll k,n;
	ll kitna_abhi_tak=1;

	ll vishu_total=0;
	ll abhi;
	ll r,g;
	ll a,b;
	for(int it=1;it<=t;it++)
	{
		kitna_abhi_tak=1;
		vishu_total=0;
		cin>>n>>k;
		abhi=k;
		while(abhi>kitna_abhi_tak){
			vishu_total=vishu_total+kitna_abhi_tak;
			abhi=abhi-kitna_abhi_tak;
			kitna_abhi_tak=2*kitna_abhi_tak;
			

		}
		ll check=0;
			n=n-vishu_total;
		r=n/kitna_abhi_tak;
		if(r==0){
			a=0;b=0;
			check=1;
		}
		else if(r==1){
			g=n-kitna_abhi_tak;
		}
		else{
		g=(n-r*kitna_abhi_tak);}
	
		
		if(check==0){
		if(abhi<=g){
			a=r+1;
			if(a%2==0){
				a=a/2-1;
				b=a+1;
			}
			else{
				a=a/2;
				b=a;
			}
		}
		else{
			a=r;
			if(a%2==0){
				a=a/2-1;
				b=a+1;
			}
			else{
				a=a/2;
				b=a;
			}
		}
		}
		cout<<"Case #"<<it<<": "<<b<<" "<<a<<endl;

	}
	
}
