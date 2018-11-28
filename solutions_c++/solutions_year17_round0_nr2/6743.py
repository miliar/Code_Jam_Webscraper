#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

ll fcheck(ull n){
	ll flag=0,prev=10,d;
	while(n>0&&flag==0){
		d=n%10;
		if(d>prev){
			flag=1;
		}
		prev=d;
		n=n/10;
	}
	return flag;
}

int main()
{
	ll tc,flag,m;
	ull n,ans,temp;
	cin>>tc;
	for(int t=1;t<=tc;t++){
		cin>>n;
		ans=n;
		m=10;
		while(n>0){
			flag=fcheck(n);
			if(flag==1){
				temp=9*(m/10)-((n%m)%10)*(m/10);
				ans=ans+temp;
				/*cout<<n<<" "<<temp<<endl;
				cout<<ans<<endl;*/
				ans=ans-m;
				/*cout<<n<<" "<<m<<endl;
				cout<<ans<<endl;*/
				n=ans;
			}
			n=n/10;
			m=m*10;
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}				
}