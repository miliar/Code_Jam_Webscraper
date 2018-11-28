#include <bits/stdc++.h>

using namespace std;

int arr[20], size;
long long ans;

int numToArray(long long n) 
{
	int size = 0;
	while (n)
	{
		arr[size] = n % 10;
		n /= 10;
		++size;
	}

	return size;
}

void bt(int i, bool menor, long long num, long long p)
{
	if (i == -1)
	{
		ans = max(ans, num);
		return;
	}

	if (menor)
		bt(i-1, true, num+(9*p), p/10);
	else
	{
		if (i == size-1 or (i < size-1 and arr[i] >= arr[i+1]))
			bt(i-1, false, num+(arr[i]*p), p/10);
		
		if (arr[i] > 0 and (i == size-1 or (i < size-1 and arr[i]-1 >= arr[i+1]))) 
			bt(i-1, true, num+(arr[i]-1)*p, p/10);
	}
}

long long tenPowerSize(int size)
{
	long long p = 1;
	size--;
	while (size--) p *= 10;
	return p;
}

int main()
{
	int tt, caso = 1;
	scanf("%d", &tt);

	while (tt--)
	{
		ans = 0;
		long long n;
		scanf("%lld", &n);

		size = numToArray(n);
		
		/*for (int i = 0; i < size; ++i)
			printf("%d", arr[i]);
		printf("\n");*/

		bt(size-1, false, 0, tenPowerSize(size));

		printf("Case #%d: %lld\n", caso++, ans);
	}
}