#include <bits/stdc++.h>
using namespace std;


typedef long long lint;

lint rec(lint mi, lint n)
{
	if(n < mi) return -1;
	//cout << "enter: " << mi << " " << n << endl;
	if(n < 10) return n;
	char str[30];
	sprintf(str, "%lld", n);
	lint lead;
	if((lead = (str[0] - '0')) < mi) return -1;
	for(int i = 0; str[i]; i++)
		str[i] = str[i + 1];
	//cout << str << endl;
	lint next; sscanf(str, "%lld", &next);
	lint x = rec(lead, next);
	lint a = -1;
	if(x != -1)
	{
		sprintf(str + 1, "%lld", x);
		str[0] = lead + '0';
		lint r = 0;
		sscanf(str, "%lld", &r);
		a = r;
	}
	sprintf(str, "%lld", n);
	str[0]--;
	lint r = -1;
	if(str[0] >= mi + '0')
	{
		for(int i = 1; str[i]; i++)
			str[i] = '9';
		sscanf(str, "%lld", &r);
	}
	//cout << "here" << endl;
	return max(a, r);
}

bool isTidy(lint i)
{
	char str[100];
	sprintf(str, "%lld", i);
	for(int i = 0; str[i + 1]; i++)
		if(str[i] > str[i + 1]) return false;
	return true;
}

int main()
{
	int T;
	cin >> T;
	
	for(int t = 1; t <= T; t++)
	{
		lint N; cin >> N;
		lint x = rec(0, N);
		
		/*lint basic = 0;
		for(int i = N; i >= 0; i--)
		{
			if(isTidy(i))
			{
				basic = i;
				break;
			}
		}
		if(basic != x) cout << N << " " << x << " " << basic << endl;*/
		cout << "Case #" << t << ": " << x << endl;
		//return 0;
		
	}
	
	return 0;
}
