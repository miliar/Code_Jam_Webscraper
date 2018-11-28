#include <iostream>
using namespace std;

bool areSorted(long long int n)
{
    // Note that digits are traversed from last to first
    long long int next_digit = n%10;
    n = n/10;
    while (n)
    {
        long long int digit = n%10;
        if (digit > next_digit)
            return false;
        next_digit = digit;
        n = n/10;
    }
 
    return true;
}
 
int main() {
	// your code goes here
	int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        long long int n;
        cin>>n;
        while(1)
        {
            if(areSorted(n))
            {
                cout<<"Case #"<<i<<": "<<n<<endl;
                break;
            }
            n--;
        }
    }
	return 0;
}

