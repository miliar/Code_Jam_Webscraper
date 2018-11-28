#include <bits/stdc++.h>

using namespace std;

int		main()
{
	int			t;
	long long	n;
	long long	n_cpy;
	int			digits[100];
	int			num_digits;
	int			i;

	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		scanf("%lld", &n);
		n_cpy = n;
		num_digits = 0;
		while (n)
		{
			digits[num_digits] = n % 10;
			num_digits++;
			n /= 10;
		}
		for (i = num_digits - 2; i >= 0; i--)
		{
			if (digits[i] < digits[i + 1])
				break;
		}
		if (i < 0)
		{
			printf("Case #%d: %lld\n", tt, n_cpy);
			continue;
		}
		i++;
		while (i < num_digits - 1 && digits[i] == digits[i + 1])
		{
			i++;
		}
		digits[i]--;
		i--;
		while (i >= 0)
		{
			digits[i] = 9;
			i--;
		}
		n_cpy = 0;
		for (i = num_digits - 1; i >= 0; i--)
		{
			n_cpy = n_cpy * 10 + digits[i];
		}
		printf("Case #%d: %lld\n", tt, n_cpy);
	}
	return 0;
}
