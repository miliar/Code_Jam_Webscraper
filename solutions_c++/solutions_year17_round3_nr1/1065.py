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
	FILE *fp1,*fp2;
	fp2=fopen("C:\\Users\\Sh\\Desktop\\output.txt","w");
	
	fin.open("C:\\Users\\Sh\\Desktop\\A-large.in", ios::in);
	//fout.open("C:\\Users\\Sh\\Desktop\\output.txt", ios::out);
	int t=100;
	cin>>t;
	double pi=3.141592653589793238462643383279502884197169399375105820974944592307816406286;
	fnt(t)
	{
		//cout<<"Case #"<<in+1<<": ";
		fprintf(fp2,"Case #%d: ",in+1);
		int n=1000,k=1000;
		cin>>n>>k;
		cout<<n<<"\n";
		double h[1005],r[1005];
		pair <double, double > ar[1005];
		fn(n)
		cin>>r[i]>>h[i];
		fn(n)
		{
			ar[i].first=2*pi*h[i]*r[i];
			ar[i].second=r[i];
		}
		sort(ar,ar+n);
		double mmax=0;
		fn(n)
		{
			double are=0,arm=0;
			if(arm<pi*ar[i].second*ar[i].second)
				arm=pi*ar[i].second*ar[i].second;
			int j=n-1;
			int count=0;
			are+=ar[i].first;
			while(count<k-1)
			{
				if(j!=i)
				{
					are+=ar[j].first;
					if(arm<pi*ar[j].second*ar[j].second)
				arm=pi*ar[j].second*ar[j].second;
				}
				j--;
				count++;
				
			}
			are+=arm;
			if(are>mmax)
			mmax=are;
		}
		fprintf(fp2,"%.12lf\n",mmax);
	}
}
