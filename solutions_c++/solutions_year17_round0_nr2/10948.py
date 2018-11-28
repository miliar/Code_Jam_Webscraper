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
	long long int t,x=1;
	cin>>t;
	while(t--){
		long long int n,i;
		bool res;
		cin>>n;
		for(i=n;i>=0;i--){
			res= areSorted(i);
			if(res) break;
		}
		cout<<"Case"<<" "<<"#"<<x<<":"<<" "<<i<<endl;
		x++;
	}
	return 0;
}