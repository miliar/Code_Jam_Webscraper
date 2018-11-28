#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
//#define small
bool check(int num)
{
	int arr[1000];
	int tmp = 0;
	while (num != 0)
	{
		arr[tmp++] = num % 10;
		num /= 10;
	}
	int prev = -1;
	for (int i = tmp-1; i >= 0; i--)
	{
		if (arr[i] < prev)
		{
			return false;
		}
		prev = arr[i];
	}
	return true;
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	scanf("%d\n", &T);
	const int ch_arr_max = 1000;
	char ch[ch_arr_max];
	int arr[ch_arr_max];
	int cnt = 1;
	while (T--)
	{
#ifdef small
		int num;
		scanf("%d", &num);
		for (int i=num;i>=0;i--)
		{
			if (check(i))
			{
				printf("Case #%d: ", cnt++);
				printf("%d\n", i);
				break;
			}
		}
#else
		
		scanf("%s", ch);
		int len = strlen(ch);
		for (int i = 0;i < len; i++)
		{
			arr[i] = ch[i] - '0';
		}
		int pre = 0;
		int found_id = -1;
		for (int i = 0; i < len; i++)
		{
			if (arr[i] < pre)
			{
				found_id = i;
				break;
			}
			pre = arr[i];
		}
		if (found_id == -1)
		{
			printf("Case #%d: ", cnt++);
			printf("%s\n", ch);
			continue;
		}
		else
		{
			int edit_id = found_id - 1;
			int value = arr[edit_id];
			int start;
			if (value == 1)
			{
				for (int i = edit_id; i >= 0; i--)
				{
					if (arr[i] == value)
					{
						arr[i] --;
					}
					else
					{
						break;
					}
				}
				if (arr[0] == 0)
				{
					for (int i = 1; i <= edit_id; i++)
					{
						arr[i] = 9;
					}
				}
				start = found_id;
			}
			else
			{
				int tag = edit_id;
				for (int i = edit_id; i >= 0; i--)
				{
					if (arr[i] == value)
					{
						tag = i;
					}
					else
					{
						break;
					}
				}
				arr[tag]--;
				start = tag + 1;
			}
			
			for (int i = start; i < len; i++)
			{
				arr[i] = 9;
			}
			start = 0;
			if (arr[0] == 0) start = 1;
			printf("Case #%d: ", cnt++);
			for (int i = start; i < len; i++)
			{
				printf("%d", arr[i]);
			}
			printf("\n");
		}
#endif
	}
}
