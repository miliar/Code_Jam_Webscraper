#include<iostream>
#include<cstdio>
using namespace std;

enum coins {penny=1, nickel=5, dime=10, qtr=25, half=50};
enum bills {dollar=1, five=5, ten=10, twenty=20, fifty=50};

const int max1 = 5;

struct money {
	coins coin[max1];
	bills bill[max1];
};

void count (const money &);

int main(int argc, char const *argv[])
{
	static money bag = {
		{qtr,qtr,qtr,dime},
		{fifty,fifty,fifty,fifty}

	};
	count(bag);
	return 0;
}

void count(const money & this_bag) {
	int paper=0,silver=0;

	for (int i =0; i<max1; i++)
	{
		paper+=this_bag.bill[i];
		silver+=this_bag.coin[i];


	}
	cout<<"you have "<<paper<<"dollars ";
	cout<<"and "<<silver<<" cents "<<endl;
};
