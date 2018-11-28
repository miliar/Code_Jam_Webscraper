#include <bits/stdc++.h>

using namespace std;
bool sorted_digit(long n ){
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
int main(void){
	int t;
	long n;
	scanf("%d",&t);
	for(int p = 1;p<=t;p++){

		scanf("%ld",&n);
		while(!sorted_digit(n)){
			n--;
		}
		printf("Case #%d: %ld\n",p, n);
	}

	return 0;
}