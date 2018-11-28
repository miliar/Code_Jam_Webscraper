#include <iostream>
#include <string>
using namespace std;


void process(int tc)
{
	string num;
	cin >> num;
	int point = num.size();
	for (int i = num.size() - 1; i >= 1; i--)
	{
		if (num[i - 1] > num[i])
		{
			num[i] = '9';
			num[i - 1] = num[i - 1] - 1;
			point = i;
		}
	}
	for (int i = point; i < num.size(); i++) num[i] = '9';
	int idx = 0;
	while (num[idx] == '0') num.erase(num.begin());

	cout << "Case #" << tc <<": " << num << endl;
}

int main()
{
	int C;
	cin >> C;
	for (int i = 0; i < C; i++) process(i+1);
	return 0;
}



