#include <stdio.h>

#include <iostream>
using namespace std;
 
// Returns true if digits of n are sorted in increasing order
bool areSorted(int n)
{
	// Digits are traversed from last to first
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

int main(void)
{
    int T, N;
    scanf("%d", &T);
    
    for(int i = 0; i < T; i++)
    {
        scanf("%d", &N);

        printf("Case #%d: ", i+1);
        
        for(int j = N; j >= 1; j--)
        {
            if(areSorted(j))
            {
                printf("%d", j);
                break;
            }
        } 
        printf("\n");
    }
    
    return 0;
}