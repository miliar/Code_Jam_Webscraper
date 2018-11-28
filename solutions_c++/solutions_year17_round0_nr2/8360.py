#include <iostream>
#include <cstring>

using namespace std;

void preencheN (char* N, int index, int len)
{
	for (int i = index; i < len; i++)
		N[i] = '9';
}

int main()
{
	int T;
	cin >> T;
	for (int k = 0; k < T; k++)
	{
		int i, j;
		char N[20];
		cin >> N;
		int len = strlen(N);
		bool flag = false;
		cout << "Case #" << k+1 << ": ";
		for (int i = 0; i < len-1; i++)
		{
			if (N[i] > N[i+1])
			{
				if (N[i] == '1')
				{
					for (j = 0; j < len-1; j++)
						cout << '9';
					flag = true;
					break;
				}
				else
				{
					if (i == 0)
					{
						N[i]--;
						preencheN(N, i+1, len);
						break;
					}
					else
					{
						if (N[i-1] > N[i]-1)
						{
							for (j = i-1; j > 0; j--)
							{
								if (N[j-1] != N[j])
									break;
							}
							if (j == 1)
								if (N[j-1] == N[j])
									j = 0;
							N[j]--;
							preencheN(N,j+1,len);
							break;							
						}
						else
						{
							N[i]--;
							preencheN(N, i+1, len);
							break;
						}
					}
				}
			}
		}
		if (!flag)
		{
			cout << N;
		}
		cout << endl;
	}
	return 0;
}
