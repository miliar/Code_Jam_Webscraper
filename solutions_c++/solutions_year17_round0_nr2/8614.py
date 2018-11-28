#include <iostream>
#include <cstring>
#include <cstdlib>

using namespace std;

char str[21];

int main()
{
	int n_case;
	cin >> n_case;
	for (int i = 1; i <= n_case; ++i)
	{
		cin >> str;
		int l = strlen(str); 

		int j = 0;
		while (j < l - 1 && str[j] <= str[j + 1]) ++j;

		for (int k = j + 1; k < l; ++k)
			str[k] = '9';

		if( j < l-1)
			--str[j];
		while (j > 0 && str[j] < str[j - 1])
		{
			str[j] = '9';
			--str[j - 1];
			--j;
		}

		long long ans = atoll(str);
		printf("Case #%d: %lld\n", i, ans);
	}
	return 0;
}