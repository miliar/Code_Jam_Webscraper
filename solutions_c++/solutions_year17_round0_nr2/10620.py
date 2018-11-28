#include <iostream>
using namespace std;
bool areSorted(long int n)
{
    // Note that digits are traversed from last to first
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

int main() {
	// your code goes here
	freopen("B-small-attempt1.in","r",stdin);
	freopen("output.txt","w",stdout);
	std::ios::sync_with_stdio(false);
	long int t,n,i,j;
	cin>>t;
	for(i=1;i<=t;i++)
	{
	 cin>>n;
	 for(j=n;j>=1;j--)
	 {
     if(areSorted(j))
     {
     cout<<"Case #"<<i<<": "<<j<<"\n";
     break;
     }
    
	 }
	}
	return 0;
}


