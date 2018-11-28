#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
#include<utility>
#include<queue>
#include<set>
#include<iomanip>
#include<functional>
#include<fstream>
#include<string.h>
#define fnt(t) for(int in=0;in<t;in++)
#define fn(n) for(int i=0;i<n;i++)
#define fnj(n) for(int j=0;j<n;j++)
#define foo(a,b,c) for(int i=a;i<b;i+=c)
#define fo(a,b) for(int i=a;i<b;i++)
#define get(x) scanf("%d",&x)
#define getll(x) scanf("%lld",&x)
#define lli long long int
#define cin fin
//#define cout fout
using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("C:\\Users\\Sh\\Desktop\\C-small-1-attempt0.in", ios::in);
	FILE *fp1,*fp2;
	fp2=fopen("C:\\Users\\Sh\\Desktop\\output.txt","w");
	//fout.open("C:\\Users\\Sh\\Desktop\\output.txt", ios::out);
	int t=1;
	cin>>t;
	
	fnt(t)
	{
		//cout<<"Case #"<<in+1<<": ";
		
	    fprintf(fp2,"Case #%d: ",in+1);
		int n,k;
		cin>>n>>k;
		double p[55],u;
		cin>>u;
		fn(n)
		cin>>p[i];
		sort(p,p+n);
		//fn(n)
		//cout<<p[i]<<" ";
		//cout<<in+1<<"   fsd\n";
		for(int i=n-1;i>=0;i--)
		{
			double sum=0;
			for(int j=0;j<=i;j++)
			{
				sum+=p[j];
				//cout<<sum<<"\n";
			}
			
			sum+=u;
			
			sum/=((double)(i+1));
			//cout<<sum<<" "<<p[i]<<"\n";
			if(sum>=p[i])
			{
				if(sum>=1.0000)
				{
					for(int j=0;j<=i;j++)
			       {
				    p[j]=1.00;
			       } 
				}
				else
				{
					for(int j=0;j<=i;j++)
			         {
				    p[j]=sum;
				    //cout<<p[j]<<" ";
			         }
			         //cout<<"\n";
				}
				
			   break;
			}
		}
		double pt=1;
		//fn(n)
		//cout<<p[i]<<" ";
		//cout<<"\n";
		fn(n)
		pt*=p[i];
		//cout<<pt<<"\n";
		fprintf(fp2,"%.12lf\n",pt);
	}
}
