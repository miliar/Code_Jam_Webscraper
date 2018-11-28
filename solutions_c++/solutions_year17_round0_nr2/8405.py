#include<stdio.h>
#include<string.h>
bool isSorted(long long int n)
{
	int lastNum = 10;
	while (n)
	{
		int curNum = n % 10;
		if (curNum > lastNum) return false;
		lastNum = curNum;
		n /= 10;
	}
	return true;
}

long long int makeTidyNumbers(long long int n)
{
	char temp[25] = { 0 };
	sprintf(temp, "%lld", n);
	int len = strlen(temp);
	for (int i = len - 1; i > 0; i--)
	{
		if (temp[i - 1] == '0' && temp[i] == '0')
		{
			temp[i - 1]--;
			for (int j = i; j < len; j++)
				temp[j] = '9';
		}
		else if (temp[i - 1] > temp[i])
		{
			temp[i - 1]--;
			for (int j = i; j < len; j++)
				temp[j] = '9';
		}
	}
	sscanf(temp, "%lld", &n);
	return n;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int Case = 1; Case <= T; Case++)
	{
		long long int n;
		scanf("%lld", &n);
		printf("Case #%d: %lld\n", Case, makeTidyNumbers(n));
	}

	return 0;
}