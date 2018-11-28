#include<algorithm>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>


using namespace std;
string getTidy(string N)
{
	for (int j = N.length() - 1;j >= 1;j--)
	{
		if (N[j] == '0' - 1)
		{
			N[j] = '9';
			N[j - 1]--;
		}
		if (N[j] < N[j - 1])
		{
			for (int h = j;h < N.length();h++)
			{
				N[h] = '9';
			}

			N[j - 1]--;
		}
	}

	if (N[0] == '0')
		N = N.substr(1, N.length() - 1);
	return N;
}

bool isTidy(string s)
{
	for (int i = 1;i < s.length();i++)
	{
		if (s[i] < s[i - 1])
			return false;
	}
	return true;
}

int getTidy(int N)
{
	stringstream ss;
	string s;
	for (int i = N;i >= 0;i--)
	{
		ss << i;
		ss >> s;
		ss.str("");
		ss.clear();
		if (isTidy(s))
			return i;
	}
	return 0;
}


void Test()
{
	stringstream ss;
	for (int i = 2; i < 10000;i++)
	{
		string s;
		ss.str("");
		ss.clear();
		ss << i;
		ss >> s;

		string ans;
		ss.str("");
		ss.clear();
		ss << getTidy(i);
		ss >> ans;

		cout << i << " "<<ans<<endl;
		if (ans != getTidy(s))
			cout <<i<< " " << ans << endl;

	}
	cout << "Done" << endl;

}

void B()
{
	int T;
	cin >> T;
	for (int i = 0;i < T;i++)
	{
		string N;
		cin >> N;

		cout << "Case #" << i + 1 << ": ";
		cout << getTidy(N)<<endl;
	}
}

int main()
{
	//Test();
	B();
	return 0;
}

