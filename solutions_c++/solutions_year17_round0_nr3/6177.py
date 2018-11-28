//tidy numbers

#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

int main()
{

freopen("B-large.in.txt","r",stdin);
freopen("Blargeout.txt","w",stdout);

	int t, len, t1;
	int a[20];
	string str, s;
	cin >> t;
	t1 = t;
	while(t--)
	{
		s.empty();
		cin >> str;
		len =  str.length();
		for(int i = 0; i < len; i++)
		{
			if((str[i] < str[i - 1]) && (i != 0))
			{
				i--;
				while((i > 0) && (str[i] - 1 < str[i - 1])){i--;}
				s[i] = str[i] - 1;
//				cout << i << endl;
				for(int j = i + 1; j < len; j++) {s[j] = '9';}
				break;
			}
			else s[i] = str[i];
		}
		cout << "Case #" << t1 - t << ": ";
		for(int i = 0; i < len; i++)
		{
			if(i == 0 && s[i] == '0');
			else cout << s[i];
		}
		cout << endl;
	}

	return 0;
}

/*

		{
			if(str[i] < str[i - 1])
			{
				if(str[i] != '1') a[len - i] = str[i] - '1';
				for(int j = 0; j < len - i; j++) cout << 9;
				break;
			}
			else cout << str[i];
		}
*/