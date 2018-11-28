
#include<vector>
#include<algorithm>
#include<iostream>
#include<cstdio>
#include<stdio.h>
#include<cstdlib>
#include<stdlib.h>
#include<cstring>
#include<map>
#include<set>
#include<queue>
#include<string>
#include <iomanip>

using namespace std;
#define lli long long int 
#define fr(a,b,c) for(a=b;a<c;a++)	
#define vi vector<int> 
#define vlli vector<long long int >
#define vpii vector<pair<int,int>>
#define pb push_back
#define pii pair<int,int>
#define mp make_pair
#define f first
#define s second
#define ld long double
ld max(ld a,ld b)
{
	if(a>b)return a;
	else return b;

}
#define pi 3.14159265358979323846
int main()
{
	
	//long double pi = 3.141592653589793238463;
	int t,q;
	cin>>t;
	q=1;
	

	while(t--)
	{
		vector<long double> a(10001);
		vector<long double> b(10001);
		//vector<ld>c(10001);

		vector<vector<long double>>c(10001,vector<long double>(3));
		
		int n,k;
		cin>>n>>k;
		int i,j;
		
		long double ans=0.000000000000;

		fr(i,0,n)
		{
			cin>>a[i]>>b[i];
			c[i][0]=a[i]*b[i];
			c[i][1]=a[i];
			c[i][2]=i;

		}

		sort(c.begin(),c.begin()+n);
		//cout<<c[0][0]<<endl;

		reverse(c.begin(),c.begin()+n);
		//cout<<c[0][0]<<endl;
		
		ld maxr=-1;

		for(i=0;i<k-1;i++)
		{
			//cout<<c[i][0]<<endl;

			ans+=(long double)pi*(long double)c[i][0]*(long double)2;
			
			maxr=max(maxr,c[i][1]);
		}
		

		long double maxi=0;
		
		ld mark=-1;

		ld temp1=maxr;
		
		temp1=max(maxr,c[k-1][1]);

		//cout<<temp<<endl;

		for(i=k-1;i<n;i++)
		{
			if(c[i][1]>maxr)
			{
				mark=i;
				maxr=c[i][1];

			}
		}
		//cout<<mark<<endl;
		//cout<<ans<<endl;


		if(mark==-1)
		{
			//cout<<"mark-1"<<endl;
			ans+=(long double)pi*(long double)c[k-1][0]*(long double)2;
			ans+=(long double)pi*(ld)maxr*(ld)maxr;
		}
		else
		{
			//cout<<c[mark][2]<<endl;
			
			//cout<<c[mark][1]<<endl;
			//cout<<c[k-1][1]<<endl;
			//cout<<c[k-1][0]<<endl;

			ld temp=(long double)pi*(long double)c[mark][0]*(long double)2+(long double)pi*(ld)c[mark][1]*(ld)c[mark][1];

			ld temp2=(long double)pi*(long double)c[k-1][0]*(long double)2+(long double)pi*(ld)temp1*(ld)temp1;
			
			//cout<<temp<<" "<<temp2<<endl;

			ans+=(max(temp,temp2));
		}
		
	
		cout<<"Case #"<<q<<": "<<fixed<<setprecision(15)<<ans<<endl;
		q++;
	}		
} 
