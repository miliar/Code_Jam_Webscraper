#include <iostream>
#include <math.h>
#include <stdlib.h>
using namespace std;

typedef struct
{
	bool value;
	int pos;
}broj;

int length;

broj tidy (long long number)
{
	bool is_tidy = true;
	length = floor(log10(number)); // Not optimal but it works :P
	int last = 9;
	int position=0;
	for (int i = 0; i <= length;i++)
	{
		int mod = number % 10;
		if (mod > last)
		{
			position = i;
			is_tidy = false;
			break;
		}
		last = mod;
		number /=10;
	}
	broj b;
	b.value = is_tidy;
	b.pos = position;
	return b;
}


void solve(int a)
{
	long long num;
	cin>>num;
	if (num / 10 == 0)
		cout<<"Case #"<<a<<": "<<num<<endl;
	else
	{
		tidy(num);
		bool solution = false;
		//cout<<length<<" "<<(long long)(pow(10,length-1))<<endl;
		if (num%(long long)floor((pow(10,length-0))) == num%(long long)floor((pow(10, length-1))))
		{
			cout<<"Case #"<<a<<": ";
			if (num / (long long) floor((pow(10, length))) > 1)
				cout<<num / (long long) floor((pow(10, length))) -1;
			for (int i = 0; i< length; i++)
				cout<<"9";
			cout<<endl;
			solution = true;
		}
		while (!solution)
		{
			broj b = tidy(num);
			solution = b.value;
			//cout<<num<<endl;
			if (num%(long long)(pow(10,length-0)) == num%(long long)(pow(10, length-1)))
			{
				cout<<"Case #"<<a<<": ";
							if (num / (long long) floor((pow(10, length))) > 1)
				cout<<num / (long long) floor((pow(10, length))) -1;
				for (int i = 0; i< length; i++)
					cout<<"9";
				cout<<endl;
				solution = true;
				break;
			}
			if (solution)
				cout<<"Case #"<<a<<": "<<num<<endl;
			else
			{
				num-= pow(10, b.pos-1);
				//cout<<b.pos<<endl;
			}
		}
	}
}
	

int main()
{
	int tests;
	cin>>tests;
	for (int i = 0;i<tests;i++) solve(i+1);
	return 0;
}
