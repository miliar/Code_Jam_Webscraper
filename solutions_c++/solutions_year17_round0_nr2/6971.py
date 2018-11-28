/*
  The problem is not hard, but this should be enough to qualify for
  round 1, and I'm in a bit of a hurry.
 */
#include <iostream>

bool tidy(int x)
{
    int prev = 11;
    while(x)
    {
	int curr = x % 10;
	x /= 10;

	if(curr > prev) return false;
	prev = curr;
    }

    return true;
}

int main()
{
    int test;
    std::cin >> test;

    for(int t = 1; t <= test; t++)
    {
	std::cout << "Case #" << t << ": ";

	int n;
	std::cin >> n;

	int res = n;
	while(!tidy(res)) res--;
	
	std::cout << res << std::endl;
    }
    
    return 0;
}
