#include <iostream>
#include <string>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		long long int n;
		cin >> n;
		string temp;
		long long int hold = -1;
		for (long long int i = n; i > 0; i--)
		{
			temp = to_string(i);
			if (temp.size() == 1) {
				hold = i;
				break;
			}
			bool flag = true;
			for (int j = temp.size()-1; j > 0; j--)
			{
				if (temp[j] >= temp[j - 1])
					continue;
				else {
					while (j > 0 && temp[j] < temp[j - 1] ) {
						temp[j - 1] = temp[j-1]-1;
						j--;
					}
					if (temp[0] == '0')
					{
						temp[0] = '1';
						i = stoll(temp);
					}
					flag = false;
					break;
				}
			}
			if (flag) {
			hold = i;
			break;
			}
		}
		cout << "Case #" << i+1 << ": " << hold << endl;
	}

}