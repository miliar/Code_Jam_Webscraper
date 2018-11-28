#include <iostream>
#include <string>
#include <vector>
#include <cstring>
#include <utility>

typedef std::pair<int, int> ii;

int freq[256];
int y[256][2], x[256][2];

std::string str[30];

int main()
{
	int t;
	std::cin >> t;
	for(int te = 1; te <= t; te++)
	{
		std::cout << "Case #" << te << ":\n";
		int n, m;
		std::cin >> n >> m;
		memset(freq, 0, sizeof freq);
		for(int i = 0; i < n; i++)
			std::cin >> str[i];
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < m; j++)
			{
				char cur = str[i][j];
				if(!freq[cur])
				{
					x[cur][0] = x[cur][1] = i;
					y[cur][0] = y[cur][1] = j;
				}
				x[cur][0] = std::min(x[cur][0], i);
				x[cur][1] = std::max(x[cur][1], i);
				y[cur][0] = std::min(y[cur][0], j);
				y[cur][1] = std::max(y[cur][1], j);
				freq[cur]++;
			}
		}
		for(char i = 'A'; i <= 'Z'; i++)
		{
			if(!freq[i])
				continue;
			for(int j = x[i][0]; j <= x[i][1]; j++)
			{
				for(int k = y[i][0]; k <= y[i][1]; k++)
				{
					str[j][k] = i;
				}
			}
		}
		for(char i = 'A'; i <= 'Z'; i++)
		{
			if(!freq[i])
				continue;
			//std::cout << "working on " << i << '\n';
			while(x[i][0] > 0)
			{
				bool got = false;
				for(int j = y[i][0]; j <= y[i][1]; j++)
					got = got || str[x[i][0] - 1][j] != '?';
				if(got)
					break;
				for(int j = y[i][0]; j <= y[i][1]; j++)
					str[x[i][0] - 1][j] = i;
				x[i][0]--;
				//std::cout << "expanded to " << x[i][0] << '\n';
			}
		}
		for(char i = 'A'; i <= 'Z'; i++)
		{
			if(!freq[i])
				continue;
			//std::cout << "second step\n";
			while(x[i][1] < n - 1)
			{
				bool got = false;
				for(int j = y[i][0]; j <= y[i][1]; j++)
					got = got || str[x[i][1] + 1][j] != '?';
				if(got)
					break;
				for(int j = y[i][0]; j <= y[i][1]; j++)
					str[x[i][1] + 1][j] = i;
				x[i][1]++;
				//std::cout << "expanded to " << x[i][1] << '\n';
			}
		}
		for(char i = 'A'; i <= 'Z'; i++)
		{
			if(!freq[i])
				continue;
			//std::cout << "third step\n";
			while(y[i][0] > 0)
			{
				bool got = false;
				for(int j = x[i][0]; j <= x[i][1]; j++)
					got = got || str[j][y[i][0] - 1] != '?';
				if(got)
					break;
				for(int j = x[i][0]; j <= x[i][1]; j++)
					str[j][y[i][0] - 1] = i;
				y[i][0]--;
				//std::cout << "expanded to " << y[i][0] << '\n';
			}
		}
		for(char i = 'A'; i <= 'Z'; i++)
		{
			if(!freq[i])
				continue;
			//std::cout << "fourth step\n";
			while(y[i][0] < m - 1)
			{
				bool got = false;
				for(int j = x[i][0]; j <= x[i][1]; j++)
					got = got || str[j][y[i][1] + 1] != '?';
				if(got)
					break;
				for(int j = x[i][0]; j <= x[i][1]; j++)
					str[j][y[i][1] + 1] = i;
				y[i][1]++;
				//std::cout << "expanded to " << y[i][1] << '\n';
			}
		}
		for(int i = 0; i < n; i++)
			std::cout << str[i] << '\n';
	}
}