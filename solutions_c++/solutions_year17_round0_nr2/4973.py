#include<bits/stdc++.h>

using namespace std;
int nu[30],d;
bool bad;
void numdig(long long int n)
{
	int ctr=0;
	long long int cp =  n;
	while(n)
	{
		//nu[ctr] = n%10;

		n/=10;

		ctr++;
	}
	for(int i=ctr-1;i>=0;i--)
	{
		nu[i] = cp%10;
		cp/=10;
	}
	for(int i=0;i<ctr-1;i++)
	{
		if(nu[i]>nu[i+1])
			bad = true;
	}
	d = ctr;
}
// long long int nextno(long long int n)
// {
// 	int num[20];
// 	long long int cp = n;
// 	int i=0;
// 	while(cp)
// 	{
// 		num[i] = cp%10;
// 		cp/=10;
// 		i++;
// 	}
// 	int dig = i;
// 	int carry = 0;
// 	for(int i=dig-1;i>0;i--)
// 	{
// 		while(num[i] == num[i-1]&&i>0)
// 		{
// 			i--;
// 		}
// 		if(i==0)
// 		{
// 			if(num[i+1]==num[i])
// 			{
// 				num[i]=9;
// 				num[i+1]--;
// 			}
// 			break;
// 		}
// 		if(num[i-1]<num[i])
// 		{
// 			num[i]--;
// 			while(i>=1)
// 			{
// 				num[i-1] = 9;
// 				i--;
// 			}
// 			break;
// 		}
// 	}
// 	long long int ans = 0,p10=1;
// 	for(int i=0;i<dig;i++)
// 	{
// 		ans+= (num[i]*p10);
// 		p10 = p10*10;
// 	}
// 	return ans;
// }
bool onetime;
void nextno2(int r)
{
	if(r==0)
		return;
	if(nu[r-1]>nu[r])
	{
		for(int i = r;i<d;i++)
		nu[i] = 9;
		nu[r-1]--;
		onetime = true;
		r=d;
	}
	// if(nu[r-1]==nu[r]&&!onetime)
	// {
	// 	nu[r] = 9;
	// 	nu[r-1]--;
	// 	onetime = true;
	// }
	// cout<<r<<"->";
	// for(int i=0;i<d;i++)
	// 	cout<<nu[i];
	// cout<<endl;
	nextno2(r-1);
}
long long int makeno()
{
	long long int ans=0,p10=1;
	for(int i = d-1;i>=0;i--)
	{
		ans+=nu[i]*p10;
		p10*=10;
	}
	return ans;
}
int main()
{
	int t,cs=0;
	long long int n;
	scanf("%d",&t);
	while(t--)
	{	
		cs++;
		onetime =bad= false;
		printf("Case #%d: ",cs);
		scanf("%lld",&n);
		numdig(n);
		nextno2(d-1);
		printf("%lld\n",makeno());
	}

	return 0;
}