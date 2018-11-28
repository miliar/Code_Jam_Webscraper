#include <iostream>
using namespace std;

bool areSorted(long int n)
{
    int next_digit = n%10;
    n = n/10;
    while (n)
    {
        int digit = n%10;
        if (digit > next_digit)
            return false;
        next_digit = digit;
        n = n/10;
    }
 
    return true;
}

int main()
{
	int T;
	cin>>T;
	for(long i=1;i<=T;i++)
	{
	long n;
	cin>>n;
	for(long m=n;m>=0;m--)
	{
		bool ff = areSorted(m);
		if(ff)
		{
			cout<<"Case #"<<i<<": "<<m<<"\n";
			break;
		}
	}
   }
   return 0;
}