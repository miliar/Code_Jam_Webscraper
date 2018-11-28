#include <bits/stdc++.h>
using namespace std;
typedef  long long ll;
bool tidy(ll n)
{
	ll cop=n;
	ll d=10;
	while(cop>0)
	{
		//cout<<cop%10<<' '<<d<<'\n';
		if(cop%10<=d)
			d=cop%10;
		else return false;
		cop/=10;
	}
	return true;

}
int main()
{
	freopen("B-small-attempt2.in","r",stdin);
	freopen("myfile.txt","w",stdout);
int nbt;
cin>>nbt;
for(int t=1;t<=nbt;t++)
	{
		ll nb;
		cin>>nb;
		while(!tidy(nb))
			nb--;
		printf("Case #%d: ",t);
		cout<<nb;
		if(t<nbt)
			cout<<'\n';
	}
}
