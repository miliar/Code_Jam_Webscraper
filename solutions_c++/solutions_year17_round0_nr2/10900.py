#include <iostream>
using namespace std;

bool areSorted(unsigned long long n)
{
    
    unsigned long long next_digit = n%10;
    n = n/10;
    while (n)
    {
        unsigned long long digit = n%10;
        if (digit > next_digit)
            return false;
        next_digit = digit;
        n = n/10;
    }

    return true;
}

int main()
{
	int t,j;
	cin>>t;
	unsigned long long arr[t];
	for(j=0;j<t;j++)
	{
		cin>>arr[j];
	}
    unsigned long long n;
    unsigned long long i;
    unsigned long long number=0;

    for(j=0;j<t;j++)
	{
		n=arr[j];
		for(i=0;i<=n;i++)
    	{
    	areSorted(i)?number=i:number=number;
    	}
    cout<<"Case #"<<j+1<<": "<<number<<endl;
	}

    return 0;
}
