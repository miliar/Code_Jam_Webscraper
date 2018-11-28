#include<bits/stdc++.h>

using namespace std;

int flipSet(char str[],int k,int pos)
{
	for(int i = 0;i < k;i++)
	{
		if(str[pos] == '-')
			str[pos] = '+';
		else
			str[pos] = '-';
		pos++;
	}
	return 0;
}

int chkSet(char str[],int len)
{
	for(int i = 0;i < len;i++)
	{
		if(str[i] == '-')
			return 0;
	}
	return 1;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	char str[1001];
	int t;
	int k;
	int x1 = 1;
	int flips = 0;
	cin >> t;
	while(t--)
	{
		flips = 0;
		cin >> str;
		cin >> k;
		
		int len = strlen(str);
		for(int i = 0;i < len;i++)
		{
			if(str[i] == '-' && (i+k) <= len)
			{
				flipSet(str,k,i);
				flips++;
			}
		}
		//cout << str << endl;
		if(chkSet(str,len) == 1)
		{
			cout << "Case #" << x1 << ": " << flips << endl;
		}
		else
		{
			cout << "Case #" << x1 << ": " << "IMPOSSIBLE" << endl;
		}
		x1++;
	}
}
