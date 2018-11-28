/*
 * yat0
 * problem B - Large
 */

#include <iostream>
#include <cmath>
#define LL long long int
using namespace std;

bool isTidy(LL num, LL *decrement)
{
    int prevDigit = num%10;

    *decrement = 1;
    num /= 10;
    
    while(num)
    {
	int curDigit = num%10;
	
	if(curDigit > prevDigit || (curDigit == 0 && prevDigit == 0))
	{
	    if(*decrement > 1)
		*decrement /= 10;
	    return false;
	}
	
	prevDigit = curDigit;
	*decrement *= 10;
	num /= 10;
    }
    
    return true;
}

LL search(LL num)
{
    LL decrement;
    
    while(!isTidy(num,&decrement))
	num -= decrement;

    return num;
}

int main()
{
    int T;
    LL N;
    
    cin >> T;
    for(int i=1; i<=T; ++i)
    {
	cin >> N;
	cout << "Case #" << i << ": " << search(N) << endl;
    }
    
    return 0;
}
