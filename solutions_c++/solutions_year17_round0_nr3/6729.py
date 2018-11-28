#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	long long int n,k;
	int t;
	int *s;
	cin>>t;
	//for each test case
	for(int i=1;i<=t;i++)
	{
		cin>>n;		//total stalls
		cin>>k;		//people count
		s=new int[n+2];
		//fill the values for s
		s[n+1]=s[0]=1;
		fill(s+1,s+n,0);
		//for each person
		long long int minlr=0,maxlr=0,lr=0;
		for(long long int j=1;j<=k;j++)
		{
			minlr=0,maxlr=0,lr=0;
			//check each stall
			for(long long int l=1;l<=n;l++)
			{
				long long int rs=0;
				long long int ls=0;	
				if(s[l]==0)
				{
					//count ls
					for(long long int cl=l-1;s[cl]==0&&cl>=0;cl--)
						ls++;
					//count rs
					for(long long int cl=l+1;s[cl]==0&&cl<=n+1;cl++)
						rs++;
				}
				long long int mintmp=min(ls,rs);
				long long int maxtmp=max(ls,rs);
				if(mintmp>minlr)
				{
					minlr=mintmp;
					maxlr=maxtmp;
					lr=l;
				}
				else if(mintmp==minlr)
				{
					if(maxtmp>maxlr)
					{
						maxlr=maxtmp;
						lr=l;
					}
					else if(maxtmp==maxlr)
					{
						if(lr>l)
							lr=l;
					}
				}
			}
			s[lr]=1;
		}
		cout<<"Case #"<<i<<": "<<maxlr<<' '<<minlr<<endl;
	}
	exit(0);
}

