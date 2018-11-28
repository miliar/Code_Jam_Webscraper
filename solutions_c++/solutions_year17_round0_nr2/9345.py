#include <iostream>
#include <math.h>
using namespace std;

bool isAcending(long long int n)
{
    long long int x = n%10;
    n = n/10;
    while (n)
    {
        long long int digit = n%10;
        if (digit > x)
            return false;
        x = digit;
        n = n/10;
    }
    return true;
}

int digits(long long int n)
{
	int count=0;
	while(n != 0)
    {
        n /= 10;
        ++count;
    }
    return count;
}

long long int lastAscending(long long int n)
{
	int i=1;
	while(isAcending(n)==false)
	{
		int d = digits(n);
		//cout<<"digits="<<d<<endl;
		long long int k = pow(10, i++);
		n = n - n%k;
		n--;
		// cout<<n<<endl;
	}
	return n;
}

int main()
{
	int t;
	long long int n;
	cin>>t;
	int i=1;
	while(t--)
	{
		cin>>n;
		cout << "Case #" << i++ << ": " << lastAscending(n) << endl;
	}

	return 0;
}