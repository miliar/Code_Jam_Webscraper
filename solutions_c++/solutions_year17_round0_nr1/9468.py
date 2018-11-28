#include <iostream>
#include <map>
using namespace std;

map<char , char> f;

int main()
{
	f['-'] = '+';
	f['+'] = '-';
	int T;string tmp;int k;
	cin >> T;
	for(int ttt = 1 ; ttt <= T ; ttt++)
	{
		cin >> tmp >> k;
		int cnt = 0;
		for(int i = 0 ; i < tmp.length() ; i++)
		{
			if(tmp[i] == '-')
			{
				if(i + k <= tmp.length())
				{
					cnt++;
					for(int j = i ; j < i + k ; j++)
						tmp[j] = f[tmp[j]];
				}
				else
				{
					cnt = -1;
					break;
				}
			}
		}
		printf("Case #%d: " , ttt);
		if(cnt == -1)printf("IMPOSSIBLE\n");
		else printf("%d\n" , cnt);
	}
	return 0;
}

