#include<bits/stdc++.h>
#define	    ll		    long long int
using namespace std;
pair<ll,ll> rohit[10005];
#define mod 10000000000005
int main()
{
	FILE *wfile;
	ll t,l,r,i,j,ji,p,q,n,k;
cin>>t;

	wfile=fopen("output1.txt","w");
	ji=0;
	double pi = 3.1415926535897;
	
while(t--)
{
	ji++;
	fprintf(wfile,"Case #%lld: ",ji);
	cin>>n>>k;

	for(i=0;i<n;i++)
	{
		cin>>l>>r;
		rohit[i].first=l;
		rohit[i].second=r;

	}
	double temp=0.0;
	
	sort(rohit,rohit+n);

	for(i=n-1;i>=k-1;i--)
	{

		double li ,ri,xi,hi;
		li=double(rohit[i].first);
		ri=double(rohit[i].second);
		double ans=pi*li*li;
		//cout<<ans<<endl;
		ans+=(2.0)*pi*li*ri;
	//	cout<<li<<" "<<ri<<"  "<<ans<<endl;
		vector<double> vv;
		for(j=n-1;j>=0;j--)
		{
			if(j==i)
				continue;
			li=double(rohit[j].first);
			ri=double(rohit[j].second);
			xi=(2.0)*pi*li*ri;
			vv.push_back(xi);
		}
		sort(vv.begin(),vv.end());
		j=k-1;
		r=vv.size();
		if(r>=j)
		{
			while(j--)
			{
				ans+=vv[r-1];
				r--;
			}
			temp=max(temp,ans);
			cout<<ans<<endl;
		}



	}
	
		
	
		fprintf(wfile,"%lf",temp);
	
	fprintf(wfile,"\n");
}
	
	return 0;
}
