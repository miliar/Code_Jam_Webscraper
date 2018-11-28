#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

//auto &out = cout;
//auto &in = cin;

ofstream out("out.txt");
ifstream in("in.txt");


class A
{
public:
	void operator()(int a)
	{
		cout << a << " ";
	}
};
int main()
{
	int T;
	in >> T;
	for (int case_numb = 1; case_numb <= T; case_numb++)
	{
		string S;
		int k;
		in >> S;
		in >> k;
		int len;
		int res=0;
		vector<int> v(len=S.length());
		for (int i = 0; i < len; i++)
		{
			if (S[i] == '-')
				v[i]++;
		}

		for (int i = 0; i <= len - k; i++)
		{
			if (v[i] % 2==1)
			{
				res++;
				for (int j = i; j < i + k; j++)
					v[j]++;
			}
		}
		bool pos = true;
		for (int i = len - k + 1; i < len; i++)
		{
			if (v[i] % 2) pos = false;
		}
		if (pos)
			out << "Case #" << case_numb << ": " << res << endl;
		else
			out << "Case #" << case_numb << ": IMPOSSIBLE" << endl;

	}
	in.close();
	out.close();
}