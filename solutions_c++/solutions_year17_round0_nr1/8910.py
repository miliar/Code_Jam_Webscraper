                      #include <bits/stdc++.h>
using namespace std;
void solve()
{
	int num;
	string s;
	cin >> s;
	cin >> num;
	int count = 0;
	for(int i=0;i<s.length()-num+1;i++)
	{
		if(s[i]=='-')
		{
			count++;
			for(int it = i; it < i + num ; it++)
			{
				
				if ( s[it] ==  '+') 
					s[it] = '-';
				else 
					s[it] = '+';
			}
		}	
	}
	int flag;
	for(int j = 0; j < s.length() ; j++)
	{
		if (s[j] == '-')
		{
			flag = 1;
			break;
		}
	}
	if(flag == 0)
		cout << count << "\n";
	else
		cout <<"IMPOSSIBLE"<< "\n";
}

int main()
{
	int tc;
	cin >> tc;
	for(int i=0;i<tc;i++)
	{
		cout << "Case #" << i+1 << ": ";
		solve();
	}
}