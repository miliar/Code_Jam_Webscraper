#include <cstdio>
#include <cstring>

bool valid(long long N)
{
	int last = 9;
	while(N)
	{
		int digit = N % 10;
		if(digit > last)
			return false;
		last = digit;
		N /= 10;
	}
	return true;
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		char buf[24];
		scanf(" %s", buf);
		int len = strlen(buf);
		
		int pos = -1;
		for(int i = len - 2; i >= 0; i--)
			if(buf[i] > buf[i + 1])
				pos = i;
		if(pos != -1)
		{
			buf[pos]--;
			while(pos > 0 && buf[pos - 1] > buf[pos])
			{
				pos--;
				buf[pos]--;
			}
			for(int i = pos + 1; i < len; i++)
				buf[i] = '9';
		}
		printf("Case #%d: %s\n", t, (*buf == '0') ? buf + 1 : buf);
	}
}
