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
#define cout fout
using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;
	FILE *fp1,*fp2;
	fin.open("C:\\Users\\Sh\\Desktop\\A-large.in", ios::in);
	fp1=fopen("C:\\Users\\Sh\\Desktop\\output.txt","w");
	int t=1;
	cin>>t;
	pair <double, double> arr[1005];
	fnt(t)
	{
		fprintf(fp1,"Case #%d: ",in+1);
		int n;
		double d;
		cin>>d>>n;
		fn(n)
		cin>>arr[i].first>>arr[i].second;
		sort(arr,arr+n);
		double mmax;
		mmax=(d-arr[n-1].first)/arr[n-1].second;
		fn(n)
		{
			mmax=max((d-arr[i].first)/arr[i].second,mmax);
			
		}
		fprintf(fp1,"%.9lf\n",d/mmax);
	}
}
