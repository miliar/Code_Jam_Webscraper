#include <stdio.h>
#include <memory.h>
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>

//0~n번째까지 동전 이용해서 k원 만들기
void solve()
{
	std::vector<std::string> cakes;
	std::vector<std::string> newCakes;
	int R, C;
	
	scanf("%d %d", &R, &C);

	for (int i = 0; i < R; i++)
	{
		std::string cake;

		std::cin >> cake;

		cakes.push_back(cake);
		newCakes.push_back(cake);
	}

	printf("\n");

	for (int x = 0; x < R; x++)
	{
		for (int y = 0; y < C; y++)
		{
			if (cakes[x][y] == '?')
				continue;

			//왼쪽 채워넣기
			int sy = y;
			int ey = y;

			while (sy > 0 && newCakes[x][sy-1] == '?')
			{
				sy--;
				newCakes[x][sy] = cakes[x][y];
			}

			while (ey < C - 1 && newCakes[x][ey + 1] == '?')
			{
				ey++;
				newCakes[x][ey] = cakes[x][y];
			}

			for(int nx = x+1; nx < R;nx++)
			{
				bool isAll = true;

				for (int i = sy; i <= ey; i++)
				{
					if (newCakes[nx][i] != '?')
					{
						isAll = false;
						break;
					}
				}

				if (!isAll)
					break;

				for (int i = sy; i <= ey; i++)
				{
					newCakes[nx][i] = cakes[x][y];
				}
			}
		}
	}

	for (int i = 0; i < newCakes.size(); i++)
	{
		auto& cake = newCakes[i];

		if (std::all_of(cake.begin(), cake.end(), [](char c) { return c == '?'; }))
		{
			for (int j = i + 1; j < newCakes.size(); j++)
			{
				if (!std::all_of(newCakes[j].begin(), newCakes[j].end(), [](char c) { return c == '?'; }))
				{
					cake = newCakes[j];
					break;
				}
			}
		}

		std::cout << cake << std::endl;
	}
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
}