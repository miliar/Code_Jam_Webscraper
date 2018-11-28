#include<bits/stdc++.h>
using namespace std;

typedef long long int ll; 

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	cin>>test;
	for(int tt=1;tt<test+1;tt++)
	{
		priority_queue<ll> s;
		ll n,k,t;
		cin>>n>>k;
		s.push(n);
		for(ll i=1;i<k;i++)
		{
			t = s.top();
	//		cout<<t<<endl;
			s.pop();
			t--;
			s.push(t/2);
			if(t%2)
				s.push(1+t/2);
			else
				s.push(t/2);
		}
		ll ans_min=0;
		ll ans_max=0;
		t = s.top();
		t--;
		ans_min = t/2;
		t++;
		ans_max = t/2;
		cout<<"Case #"<<tt<<": "<<ans_max<<" "<<ans_min<<"\n";
	}
}
