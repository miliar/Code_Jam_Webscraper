#include<iostream>
#include<algorithm>
using namespace std;
int compare(long double *a,long double *b)
{
	if(b[0]>a[0])
		return 0;
	else 
		return 1;
}
int compare1(long double *a,long double *b)
{
	if(b[1]>a[1])
		return 0;
	return 1;
}
long double max(long double a,long double b)
{
if(a>b)
	return a;
return b;
}
int main()
{
int t;
long double pi=3.141592653589793;
cin>>t;
for(int l=0;l<t;l++)
{
	int n,k,p;
	long double s=0;//,max=-999;
	cin>>n>>k;
	std::cout.setf(std::ios_base::fixed, std::ios_base::floatfield);
	long double **a=new long double *[n];
	for(int i=0;i<n;i++)
		a[i]=new long double[3];
	

	for(int i=0;i<n;i++)
	{
		cin>>a[i][0]>>a[i][1];
		a[i][1]=2*pi*a[i][0]*a[i][1];
		a[i][0]=pi*a[i][0]*a[i][0];
		a[i][2]=a[i][0]+a[i][2];
	}

	for(int i=0;i<=n-k;i++)
	{
		long double sum=0;
		sort(a,a+n,compare);
		sort(a+i+1,a+n,compare1);
		sum+=a[i][0];
		for(int j=0;j<k;j++)
			sum+=a[j+i][1];
		s=max(s,sum);
	}
	std::cout.precision(9);
	cout<<"Case #"<<l+1<<": "<<s<<endl;
	
}


return 0;
}
