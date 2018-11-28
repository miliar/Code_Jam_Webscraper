#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

int main()
{
	int T;
	string s;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		printf("Case #%d: ", i);
		cin >> s;

		bool nine = false;
		int start = -1;

		if (s.length() == 1)
			printf("%c\n", s[0]);
		else
		{
			for (int j = 0; j < s.length() - 1; j++)
			{
				if (nine)
					cout << "9";
				else
				{
					if (s[j] == s[j + 1])
					{
						if (start == -1)
							start = j;
					}
					else if (s[j] < s[j + 1])
					{
						if (start != -1)
						{
							for (int temp = start; temp < j; temp++)
								printf("%c", s[temp]);
							start = -1;
						}
						printf("%c", s[j]);
					}
					else
					{
						nine = true;
						if (start != -1)
						{
							//
							if (s[start] == '1')
							{
								for (int temp = 1; temp < j; temp++)
									printf("9");
							}
							else
							{
								for (int temp = start; temp < j; temp++)
									printf("%c", s[temp] - 1);
							}
							printf("9");
							start = -1;
						}
						else if (s[j] != '1')
							printf("%c", s[j] - 1);
					}
				}
			}
			if (start != -1)
			{
				for (int temp = start; temp < s.length() - 1; temp++)
					printf("%c", s[temp]);
				start = -1;
			}
			if (nine)
				printf("9\n");
			else
				printf("%c\n", s[s.length() - 1]);
		}
	}
	return 0;
}