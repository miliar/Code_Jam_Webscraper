#include<bits/stdc++.h>

using namespace std;

int main()
{
	int tcc;
	scanf("%d", &tcc);
	for(int tc = 1; tc <= tcc; tc++)
	{
		printf("Case #%d: ", tc);

		string str;
		int k, ret = 0;

		cin >> str >> k;
		for(int i = 0; i <= (int)str.size()-k; i++)
			if(str[i] == '-')
			{
				ret++;
				for(int j = i; j < i+k; j++)
				{
					if(str[j] == '+')	str[j] = '-';
					else	str[j] = '+';
				}
			}

		bool impossible = false;
		for(int i = (int)str.size()-k+1; i < str.size(); i++)
			if(str[i] == '-')
				impossible = true;

		if(impossible)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ret);
	}
	return 0;
}
