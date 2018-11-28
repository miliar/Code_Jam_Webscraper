#include<iostream>
#include<iomanip>
using namespace std;
long n, k, a[2][1000];
double mainer = 0, pi = 3.14159265358979323846;
void check(int rem, int pos, double val)
{
	double temper = 0;
	if(rem == 1)
	{
		for(int r = pos + 1; r<n; r++)
		{
			if(k == 1)
				temper = a[0][r]*pi*a[0][r] + 2*pi*a[0][r]*a[1][r];
			else
				temper = 2*pi*a[0][r]*a[1][r];
			if(val + temper>mainer)
				mainer = val + temper;
		}
	}
	for(int w = pos + 1; w<n; w++)
	{
		if(k == rem)
			temper = a[0][w]*pi*a[0][w] + 2*pi*a[0][w]*a[1][w];
		else
			temper = 2*pi*a[0][w]*a[1][w];
		check(rem - 1, w, val + temper);
	}
}
int main()
{
	int t, temp1, temp2;
	cin>>t;
	for(int i = 0; i<t; i++)
	{
		cin>>n>>k;
		for(int j = 0; j<n; j++)
			cin>>a[0][j]>>a[1][j];
		for(int j = 0; j<n; j++)
		{
			for(int e = 0; e<(n - 1); e++)
				if(a[0][e]<a[0][e + 1])
				{
					temp1 = a[0][e];
					temp2 = a[1][e];
					a[0][e] = a[0][e + 1];
					a[1][e] = a[1][e + 1];
					a[0][e + 1] = temp1;
					a[1][e + 1] = temp2; 
				}
		}
		check(k, -1, 0);
		cout<<"Case #"<<i + 1<<": "<<setprecision(20)<<mainer<<endl;
		mainer = 0;
	}
}
