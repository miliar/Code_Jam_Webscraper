#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

struct line
{
public:
	vector<char> pancake;
	int flipper;
};

int main()
{
	short int T;
	scanf_s("%hd", &T);
	vector<line> pan;
	vector<int> answer(T);
	int K;
	string s;
	for (short int i = 0; i < T; i++)
	{
		line boof;
		char a;
		vector<char> s;
		do
		{
			a=getchar();
			s.push_back(a);
		} while (a != ' ');
		s.pop_back();
		s.erase(s.begin());
		boof.pancake = s;
		scanf_s("%d", &K);
		boof.flipper = K;
		pan.push_back(boof);
	}

	for (short int i = 0; i < T; i++)
	{
		for (int j = 0; j<pan[i].pancake.size() ;j++)
		{
			if (pan[i].pancake[j] == '-')
			{
				if (j + pan[i].flipper > pan[i].pancake.size())
				{
					answer[i]=-1;
					break;
				}
				else
				{
					for (int oo = 0; oo < pan[i].flipper; oo++)
					{
						if (pan[i].pancake[j + oo] == '-')
						{
							pan[i].pancake[j + oo] = '+';
						}
						else
						{
							pan[i].pancake[j + oo] = '-';
						}
					}
					answer[i]++;
				}
			}
		}
	}
	for (short int i = 0; i < T; i++)
	{
		printf("Case #");
		printf("%d", (i+1));
		printf(": ");
		if (answer[i] == -1)
		{
			printf("IMPOSSIBLE");
		}
		else
		{
			printf("%d", answer[i]);
		}
		printf("\n");
	}
	return 0;
}