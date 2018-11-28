#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

string S;

bool isTidy(unsigned long long int N)
{
	unsigned long long int CurrentDigit, LastDigit;

	LastDigit = N % 10;
	N = N / 10;

	while (N != 0)
	{
		CurrentDigit = N % 10;
		// cout<<CurrentDigit<<endl;
		
		if (CurrentDigit > LastDigit)
		{
			return 0;
		}
		
		N = N / 10;
		LastDigit = CurrentDigit;

	}
	return 1;
}

unsigned long long int getLastTidyNumber1(unsigned long long int N)
{
	while (1)
	{
		if (isTidy(N))
		{
			break;
		}
		N--;
	}
	//unsigned long long int  N;
	return N;
}

string getLastTidyNumber(string S)
{	
	string TidyNumber;

	if (is_sorted(S.begin(),S.end()))
	{
		TidyNumber = S;
	}
	else
	{
		while (1)
		{
			
		}
	}

	return TidyNumber;
}

int main()
{
	unsigned long long int T,N;

	cin>>T;
	
	for(unsigned long long int i = 1; i <= T; i++)
	{	

		cin>>N;
		cout<<"Case #"<<i<<": "<<getLastTidyNumber1(N)<<endl;

	}

	return 0;
}