#include <iostream>
#include <string>
#include <stdio.h>
#include <math.h>
using namespace std;
// typedef long long ll;
int NoOfPlaces(int temp)
{
	int count = 0;
	while(temp)
		{
			count++;
			temp /= 10;
		}
	return count;
}
int getQ(int k)
{
	// n = tidy(1, count);
	// return n*(k/pow(10,count-1));
	int count;
	count = NoOfPlaces(k);
	return k/pow(10,count-1);
}
int tidy(int k,int count)
{
	// q = getQ(k);
	// count = NoOfPlaces(k);
	int n = 0;
	for(int a = 0; a<count; a++)
		n = n*10 + 1;
	return n*k;
}

int rem(int temp)
{
	return temp - getQ(temp)*pow(10,NoOfPlaces(temp)-1);	
}
int main() 
{
	int t; cin>>t;
	int s =0;
	int no;
	int k;
	int temp;int re;
	int count;
	int n;
	int a,b,c,d;
	int x;
	// int flag;
	while(s<t)
	{
		n = 0;
		
		cin>>k;
		count = NoOfPlaces(k);
		// n = 2<<(count+1);
		// n--;
		b = tidy(getQ(k), count);
		// b = getTidy(k,count);
		// n*(k/pow(10,count-1));
		no = b;
		if( b == k)
			;
		else if( b< k)
		{
			// move till the end
			// for(b++; b<k; b++)
			for(; b<=k; b++)
			{
				// flag = 0;
				temp = b;
				while(temp/10)
				{
					x = -1;
					// getQ(temp)*pow(10,NoOfPlaces(temp)-1);
					re = rem(temp);
					if(getQ(temp) == getQ(re))
						;
					else
						x = temp - getQ(re)*pow(10,NoOfPlaces(temp)-1) ;//
					if( x > 0)
					{
						break;
						// flag = 1;
					}
					else
						;
					temp = rem(temp);
				}
				
				if( x < 0)
					no = b;
				else
					;
			}
		}
		else if(b > k)
		{
			c = tidy(getQ(k) -1 ,count);
			for(; c<k; c++)
			{
					// flag = 0;
				temp = c;
				while(temp/10)
				{
					x = -1;
					// getQ(temp)*pow(10,NoOfPlaces(temp)-1);
					re = rem(temp);
					if((getQ(temp) == getQ(re)) && (NoOfPlaces(temp) - NoOfPlaces(re) == 1))
						;
					else
						x = temp - getQ(re)*pow(10,NoOfPlaces(re)) ;//
					// x = temp - getQ(re)*pow(10,NoOfPlaces(temp)-1) ;//
					if( x > 0)
					{
						break;
						// flag = 1;
					}
					else
						;
					temp = rem(temp);
				}
				
				if( x < 0)
					no = c;
				else
					;
			}
		}
		
		s++;
		cout<<"Case #"<<s<<": "<<no;
		cout<<endl;
	}
	return 0;
}