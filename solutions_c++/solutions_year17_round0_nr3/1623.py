#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C_large.txt","w",stdout);
	long long a,b,c,d,N,K,T;
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cin>>T;
	for(a=0;a<T;a++)
	{
		cin>>N>>K;
		b=1;
		while(b*2-1<K)
		{
			b*=2;
		}
		c=(N-b+1)%b;
		d=(N-b+1)/b;
		if(K-b+1<=c)d++;
		cout<<"Case #"<<a+1<<": ";
		if((d-1)%2==0)cout<<(d-1)/2<<" "<<(d-1)/2<<"\n";
		else cout<<(d-1)/2+1<<" "<<(d-1)/2<<"\n";
	}
}
