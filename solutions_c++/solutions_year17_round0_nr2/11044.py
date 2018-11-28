#include <iostream>
using namespace std;
 
// Returns true if digits of n are sorted in increasing
// order
bool areSorted(unsigned long long n)
{
    // Note that digits are traversed from last to first
    int next_digit = n%10;
    n = n/10;
    while (n)
    {
        int digit = n%10;
        if (next_digit < digit)
            return false;
        next_digit = digit;
        n = n/10;
    }
 
    return true;
}

int main(){
	unsigned long long n,j;
	int t,i=1;
	scanf("%d",&t);
	while(t--){
		scanf("%llu",&n);
		for(j=n;j>=1;j--){
			if(areSorted(j)){
				break;
			}
		}
		printf("Case #%d: %llu\n",i++,j);
	}
	return 0;
}
