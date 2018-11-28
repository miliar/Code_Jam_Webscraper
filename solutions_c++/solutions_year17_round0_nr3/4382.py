#include<bits/stdc++.h>
using namespace std;
struct kjoshi{
	long long int x,y;
};
int main()
{
	freopen("C-small-2-attempt1 .in","r",stdin);
	freopen("ggl.txt","w",stdout);
	long long int t,kk=0;
	cin>>t;
	while(t--)
	{
		long long int n,k;
		cin>>n>>k;
		long long int gp=(log2(k));
	//	cout<<gp<<endl;
			kjoshi a,b;
		a.x=0;
		a.y=0;
		b.x=0;
		b.y=0;
		if(n%2==0)
		{
			a.x=(n/2)-1;
	b.x=(n/2);
			a.y=1;
			b.y=1;
		}
		else
		{
			a.x=(n/2);
			a.y=1;
			b.x=(n/2);
			b.y=1;
		}
	//	cout<<a.x<<" "<<b.x<<" "<<a.y<<" "<<b.y<<endl;
		long long int t1,t2,tc1,tc2;
		for(int i=1;i<gp;i++)
		{
	//		cout<<"kj"<<endl;
			bool isd1=0,isd2=0;
			
		
				if(a.x%2==0)
				{
		t1=(a.x/2)-1;
		a.x=t1;
		tc1=a.y;
			isd1=1;
				}
		else
				{
			t1=(a.x/2);
			a.x=t1;
			a.y*=2;
				}
					
				if(b.x%2==0)
				{
					t2=(b.x/2)-1;
					b.x=t2+1;
					tc2=b.y;
					isd2=1;
				}
				else
				{
					t2=(b.x/2);
					b.x=t2;
					b.y*=2;
				}
//				if(isd2)	
				
//				else
				
				
				if(isd1)
				{
					b.y+=tc1;			
				}
				if(isd2)
				{
					a.y+=tc2;
				}
			//		cout<<a.x<<" "<<b.x<<" "<<a.y<<" "<<b.y<<endl;
			}
			
			
	//
	
		long long int posi=k-pow(2,gp)+1,ans;
	//	cout<<posi<<endl;
			ans=(b.y>=posi)?b.x:a.x;
		if(k==1)
			ans=n;
		kk++;
		if(ans%2==0)
		cout<<"Case #"<<kk<<": "<<(ans/2)<<" "<<(ans/2)-1<<endl;
		else
		cout<<"Case #"<<kk<<": "<<(ans/2)<<" "<<(ans/2)<<endl;
	}
}
