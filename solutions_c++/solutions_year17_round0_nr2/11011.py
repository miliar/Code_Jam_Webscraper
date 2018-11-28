 
#include <iostream>
#include<fstream>
using namespace std;
 
// Returns true if digits of n are sorted in decreasing
// order
bool areSorted(long long int n)
{
    // Note that digits are traversed from last to first
    long long next_digit = n%10;
    n = n/10;
    while (n)
    {
        long long digit = n%10;
        if (digit >next_digit )
            return false;
        next_digit = digit;
        n = n/10;
    }
 
    return true;
}
 
int main()
{
    ifstream f1;
    ofstream f2;
	f1.open("B-small-attempt1.txt");
	f2.open("ans.txt");
	int T;
    f1>>T;
	for(int i=0;i<T;i++)
    {
    	long long N;
    	f1>>N;
    	for(long long j=N;j>=1;j--)
    	{
    		if(areSorted(j)==true)
    		{	f2<<"Case #"<<i+1<<": "<<j<<endl;
    			break;
    		}
		}
	}
	f1.close();
	f2.close();
    return 0;
}
