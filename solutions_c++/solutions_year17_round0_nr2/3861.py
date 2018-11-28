#include <cstdio>
#include <cstring>
#include <cstdlib>


int is_tidy(char *s)
{
	int l = strlen(s);
	for(int i = 0; i < l-1; i++)
	{
		if(s[i] > s[i+1])
			return 0;
	}
	return 1;
}





int main()
{
	int T;
	scanf("%d", &T);
	int cnt = 1;
	while(T--)
	{
		char num[64];
		scanf("%s", num);
		int l = strlen(num);
		if(is_tidy(num))
		{
			printf("Case #%d: %s\n", cnt, num);
		}
		else
		{
			int modified = 0;
			char tmp_num[64];
			strcpy(tmp_num, num);

			for(int i = 0; i < l-1; i++)
			{
				if(tmp_num[i] > tmp_num[i+1])
				{
					tmp_num[i] = tmp_num[i] - 1;
					for(int j = i+1; j < l; j++)
					{
						tmp_num[j] = '9';
					}
					modified = 1;
					break;
				}
			}
			while(modified)
			{
				modified = 0;
				for(int i = 0; i < l-1; i++)
				{
					if(tmp_num[i] > tmp_num[i+1])
					{
						tmp_num[i] = tmp_num[i] - 1;
						for(int j = i+1; j < l; j++)
						{
							tmp_num[j] = '9';
						}
						modified = 1;
						break;
					}
				}
		//		printf("tmp%s\n", tmp_num);
				
			}
	//		printf("tmp = %s\n", tmp_num);
			long long int res = atoll(tmp_num);
			if(res == 0)
			{
				for(int i = 0; i < l-1; i++)
				{
					res *= 10;
					res += 9;
				}
				printf("Case #%d: %lld\n", cnt, res);
			}
			else
			{
				int start_increase = 0;
				for(int i = 0; i < l; i++)
				{
					if(tmp_num[i] < num[i])
					{
						start_increase = 1;
						continue;
					}
					if(start_increase == 1)
					{
						tmp_num[i] = '9';
					}
				}
				res = atoll(tmp_num);
				printf("Case #%d: %lld\n", cnt, res);
			}
		}
		cnt++;
	}





	return 0;
}