#include <iostream>

using namespace std;

long long t;
long long n, k;
long long m, w;
long long a, b;
long long pot=1;
long long f;
bool dwa;
long long przek=1;

int main()
{
    cin>>t;
    for(long long i=1; i<=t; i++)
    {
        cin>>n>>k;
        w = 0;
        m = 1;
        a = n;
        b = -1;
        pot = 1;
        przek = 1;
        while(przek*2 <= n) przek*=2;
        while(pot*2 <= k)
        {
            pot*=2;
            if(a%2 == 0)
            {
                w = pot - m;
            }
            else
            {
				if(b != -1)
					m = pot - w;
				else
					m = pot;
            }
            if(a%2 == 0)
            {
				b = a/2;
				a = (a-1)/2;
			}
			else
			{
				if(b%2 == 0)
				{
					a = (b-1)/2;
					b = b/2;
				}
				else
					a = a/2;
			}
        }
        if(k > n-(przek/2))
			cout<<"Case #"<<i<<": "<<0<<" "<<0<<endl;
        else if((k-pot+1 <= w))	
        {
			if(b%2 == 0)
			{
				a = (b-1)/2;
				b = b/2;
			}
			else
			{
				a = b/2;
				b = b/2;
			}
			cout<<"Case #"<<i<<": "<<b<<" "<<a<<endl;
		}
        else
        {
			if(a%2 == 0)
			{
				b = a/2;
				a = (a-1)/2;
			}
			else
			{
				b = a/2;
				a = a/2;
			}
			cout<<"Case #"<<i<<": "<<b<<" "<<a<<endl;
		}
    }
    return 0;
}
