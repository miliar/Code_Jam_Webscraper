#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long llint;

bool isTidy(llint num)
{
	int lastDigit = 10;
	while(num>0)
	{
		if(num%10 > lastDigit)
			return false;

		lastDigit = num%10;
		num/=10;
	}

	return true;
}

int main()
{
	int T;
	llint num;
	
	freopen("input_B.txt", "r", stdin);
	freopen("output_B.txt", "w", stdout);

	scanf("%d", &T);

	for(int test_case=1;test_case<=T;test_case++)
	{
		scanf("%lld", &num);
		
		llint d = 10;
		llint tnum = num;
		while(isTidy(tnum)==false)
		{
			tnum = (num/d)*d - 1;
			d *= 10;
		}

		printf("Case #%d: %lld\n", test_case, tnum);
	}

	return 0;
}
