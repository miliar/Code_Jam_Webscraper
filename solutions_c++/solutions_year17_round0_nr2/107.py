#include <stdio.h>
#include <iostream>
#include <string>

void solve()
{
	std::string number;
	std::cin >> number;

	std::string answer;

	std::string prev = "9012345678";
	
	int point = number.size();

	while (point > 0)
	{
		int nextPoint = point;

		for (int i = 1; i < point; i++)
		{
			if (number[i] < number[i - 1])
			{
				nextPoint = i;
				break;
			}
		}

		if (nextPoint == point) // ���� ��������
		{
			answer.insert(answer.begin(), number.begin(), number.begin() + nextPoint);
			break;
		}

		//���� �������� ���̴� �κ� �˴� 9�� ä���
		for (int i = nextPoint; i < point; i++)
			answer.push_back('9');

		number[nextPoint - 1] = prev[number[nextPoint - 1] - '0'];

		point = nextPoint;
	}

	while (answer[0] == '0')
		answer.erase(answer.begin());

	std::cout << answer << std::endl;
}

int main()
{
	int T;
	scanf("%d", &T);

	for (int i = 1; i <= T; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}