#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <cstdlib>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int caseT = 1; caseT <= T; caseT++)
	{
		char temp[20];
		int number[20];
		scanf(" %s", temp);
		int len = strlen(temp);
		for (int i = 0; i < len; i++)
		{
			number[i] = temp[i] - '0';
		}

		//if (number[len - 1] == 0)
		//{
		//	number[len - 1] = 9;
		//	number[len - 2] -= 1;
		//}
		//else number[len - 1] -= 1;

		//for (int i = len - 2; i >= 0; i--)
		//{
		//	if (number[i] < 0)
		//	{
		//		number[i] = 9;
		//		number[i - 1] -= 1;
		//	}
		//	else
		//	{
		//		break;
		//	}
		//}
		//if (number[0] == 0)
		//{
		//	//shift ke kiri dan len dikurang 1
		//	len -= 1;
		//	for (int i = 0; i < len - 2; i++)
		//	{
		//		number[i] = number[i + 1];
		//	}
		//}

		while (1)
		{
			int flag = 1;
			for (int i = 1; i < len; i++)
			{
				if (number[i] < number[i - 1])
				{
					flag = 0;
					// angka yang lebih kecil diubah jadi 9
					for (int x = i; x < len; x++)
					{
						number[x] = 9;
					}
					//angka yang lebih besar (sebelumnya) dikurang satu
					number[i - 1] -= 1;
					/*while (1)
					{
						if (i > 1 && number[i - 1] < number[i - 2])
						{
							number[i - 1] = 9;
							i--;
							number[i - 1] -= 1;
							continue;
						}
						break;
					}
					break;*/
				}
			}
			if (flag) break;
		}

		if (number[0] == 0)
		{
			//shift ke kiri dan len dikurang 1
			len -= 1;
			for (int i = 0; i < len - 1; i++)
			{
				number[i] = number[i + 1];
			}
		}

		printf("Case #%d: ", caseT);
		for (int i = 0; i < len; i++)
		{
			printf("%d", number[i]);
		}
		puts("");
	}
}