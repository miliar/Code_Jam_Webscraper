#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

long long power(long long m)
{	
	if(m==1)
	return 10;
	
	if(m==0)
	return 1;
	
	if(m%2==1)
	return power(m/2)*power(m/2+1);

        else
	return power(m/2)*power(m/2);

}

bool check(long long n)
{
	long long ptr, highest;
	highest = n%10;
	n/=10;

	while(n!=0)
	{
		ptr=n%10;

		if(ptr>highest)
		  return false;
		else 
		  highest = ptr;

		n/=10;
	}

	return true;
}

long long smallestTidy(long long n)
{
	long long k = log10(n) ;
	long long prev_m = 0;
	for(long long int i=0;i<=k;i++)
	{
		long long m = n / power(k-i);
		
		if(!check(m))
		{
			m = n / pow(10, k-prev_m);
			long long tidy = (m - 1) * power(k-prev_m) + power(k-prev_m) - 1;
			return tidy;
		}
		
		if(m%10 != (m/10)%10)
		{
			prev_m=i;
		}	
	}
	return n;	
}

int main()
{
	ifstream fin;
	fin.open("B-large.in");
	ofstream fout;
	fout.open("B-output.txt");
	long long T;
	long long N;
	
	fin>>T;
	
	for(long long i=0; i<T; i++)
	{
		fin>>N;
		fout<<"Case #"<<(i+1)<<": "<<smallestTidy(N)<<endl;
	}

	return 0;
}
