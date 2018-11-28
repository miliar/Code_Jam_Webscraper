#include <vector>
#include <iostream>
#include <string>
#include <functional>
#include <algorithm>


using namespace std;

vector <int> ist(vector<int> num)
{
	int i;
	for (i = 0; i < num.size() - 1; i++)
		if (num[i + 1] < num[i])
			break;
	if (i == num.size() - 1)
		return num;
	for (; i >= 0; i--)
	{
		if (i == 0)
		{
			num[i]--;
			break;
		}
		if (num[i] > num[i - 1])
		{
			num[i]--;
			break;
		}

	}
	for (i = i + 1; i < num.size(); i++)
		num[i] = 9;
	return num;

}

int main(){
	int t;
	vector<string> ans;
	scanf("%d\n", &t);
	for (int i = 0; i < t; i++)
	{
		string t;
		vector <int> a;
		bool nn = 0;
		char c;
		while (1)
		{
			c = getc(stdin);
			if (c == '\n')
				break;
			a.push_back(c - '0');
		}
		a = ist(a);
		for (int i = 0; i < a.size(); i++)
		{
			if (!nn)
				if (a[i] == 0)
					continue;
				else
					nn = 1;
			t.push_back(char(a[i] + '0'));
		}
		ans.push_back(t);

	}
	for (int i = 0; i < ans.size(); i++)
		cout << "Case #" << i + 1 << ": " << ans[i] << endl;
	
	return 0;
}