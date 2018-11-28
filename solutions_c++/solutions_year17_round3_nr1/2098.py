#include<bits/stdc++.h>
using namespace std;

const double pi = 3.141592653588888;
int n,k;
long long int r[11],h[11];
double long ans=0;


void sort_r()
{
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(r[i]<r[j])
			{
				swap(r[i],r[j]);
				swap(h[i],h[j]);
			}
		}
	}
}

void area(int done,int i,int p,long long int sur)
{
//	cout<<done<<"  "<<i<<"  "<<p<<"  "<<sur<<endl;
	if(done==k)
	{
		if(sur>ans)
		ans=sur;
		
		return;
	}
	
	
	if(i>=n)
	return;
	
	for(int j=i;j<n;j++)
	{
		long long int o=(2*r[j]*h[j])+(r[j]*r[j]-r[p]*r[p]);
		area(done+1,j+1,j,sur+o);
	}
}

int main()
{
	freopen("in1.in","r",stdin);
	freopen("out11.txt","w",stdout);
	int t;
	cin>>t;
	for(int l=1;l<=t;l++)
	{
		cin>>n>>k;
		for(int i=0;i<n;i++)
		{			
			cin>>r[i]>>h[i];
		}
		sort_r();
		for(int i=0;i<n;i++)
		{
			long long int aa=(2*r[i]*h[i]+r[i]*r[i]);
	
			area(1,i+1,i,aa);
		}
		ans=ans*pi;
		cout<<"Case #"<<l<<": ";
		cout<<fixed<<setprecision(10)<<ans<<endl;
		ans=0;
		
		
	}
}
