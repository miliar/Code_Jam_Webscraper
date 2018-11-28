//phi

#include <bits/stdc++.h>

#define iOS ios::sync_with_stdio(false)

#define M 1000000007

#define tp4 10000
#define tp5 100000
#define tp6 1000000
#define tp7 10000000
#define tp8 100000000
#define tp9 1000000000

#define ll long long
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define sd(x) scanf("%d",&x)
#define sc(x) scanf("%c",&x)

using namespace std;

int a[20],dig;

int tidy(ll n)
{
	int pd=10;
	int cd;

	while(n)
	{
		cd=n%10;
		if(!(pd>=cd)) return 0;

		n/=10;
		pd=cd;
	}

	return 1;
}

ll check(ll n)
{
	while(n)
	{
		if(tidy(n)) return n;
		n--;
	}
}

ll checkl()
{
	for(int k=0;k<dig;k++)
	{
		for(int i=0;i<dig-1;i++)
			{
				if(a[i]>a[i+1])
				{
					a[i]--;
					for(int j=i+1;j<dig;j++) a[j]=9;
				}
			}
	}

	int ind=0;
	while(a[ind]==0) ind++;

	for(int i=ind;i<dig;i++) cout<<a[i];

}

void store(ll n)
{
	int ind=0;
	int b[20];
	while(n)
	{
		b[ind++] = n%10;
		n/=10;
	}

	int j=0;
	for(int i=ind-1;i>=0;i--)
	{
		a[j++] = b[i];
	}

	dig= ind;
}

int main()
{
	int t,test;

	ll n;
	cin>>test;
	for(t=1;t<=test;t++)
	{
		cin>>n;

		store(n);

		cout<<"Case #"<<t<<": ";
		checkl();
		cout<<endl;

	}

	return 0;
}

