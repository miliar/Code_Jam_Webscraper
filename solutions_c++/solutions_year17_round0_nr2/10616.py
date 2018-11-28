#include <iostream>

using namespace std;

int a;
unsigned long long int b;
//int tab[101] = {0};
int main()
{
	cin >> a;
	int tab[1000];
	for (int i = 1; i <= a; i++)
	{
		cin >> b;
		unsigned long long int temp = b;
		int j = 0;
		int x = 0;
		int y = 0;
		//int wtf;
		//int n = 10;
		while (temp > 0)
		{
			x = temp % 10;
			y = (temp % 100) / 10;
			if (x < y)
			{
				j++;
				temp = b - j;
			}
			else
			{
				temp = temp / 10;
			}
			//n = n * 10;
		}
		tab[i] = b - j;
		//cout << "Case #" << i << ": " << b - j << endl;
	}
	for (int i = 1; i <= a; i++)
	{
		cout << "Case #" << i << ": " << tab[i] << endl;
	}
	//system("pause");
    return 0;
}
