#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cstdint>

const int maxn = 18+5;

int main()
{
	int T;
	std::cin >> T;
	int64_t res;
	char num[maxn];
	for(int i = 1; i <= T; ++i)
	{
		std::cin >> num;
		int len = strlen(num);
		int inc = 0, j; //inc means the last position of an absolute increasing sub sequence
		bool flag = true; //flag means whether the orginal number is absolutely increasing
		for(j = 1; j < len && flag; ++j)
		{
			if(num[j] > num[j - 1]) //since '5' > '4' is also true, no need to transform to integers
				inc = j;
			else if(num[j] < num[j - 1])
				flag = false;
		}
		if(flag) {
			//if already absolutely increasing
			std::cout << "Case #" << i << ": " << num << std::endl;
			continue;
		}

		//the last increasing number is to sub num[inc] with 1, and replace all the following number with 9
                //for example, 12322, then sub 3 with 1, it becomes 12299
		res = 0;
		for(j = 0; j < inc; ++j)
			res = res * 10 + (num[j] - '0');

		res = res * 10 + (num[inc] - 1 - '0');
		++j;

		for(; j < len; ++j)
			res = res * 10 + 9;

		std::cout << "Case #" << i << ": " << res << std::endl;
	}
	return 0;
}
