#include <iostream>

using namespace std;

int main()
{
	int T, test, len, i, t[20], p;
	bool is;
	long long N;

	cin>>T;

	for (test = 1; test <= T; test++)
	{
		cin>>N;

		p = 0;
		while (N)
		{
			t[p++] = N % 10LL;
			N /= 10LL;
		}

		len = p;

		do
		{
			is = false;

			while (--p)
			{
				if (t[p] > t[p-1])
				{
					is =- true;

					if (t[p] > 0)
					{
						t[p]--;
					}
					else
					{
						for (i = p; i < len; i++)
						{
							if (t[i] > 0)
							{
								t[i]--;
								break;
							}
							else
							{
								t[i] = 9;
							}
						}
					}

					while(p--)
					{
						t[p] = 9;
					}
					break;
				}
			}

			p = len;
		}
		while (is);


		cout<<"Case #"<<test<<": ";
		for (i = (t[len-1] ? (len-1) : (len-2)); i >= 0; i--)
		{
			cout<<t[i];
		}
		cout<<endl;
	}

	return 0;
}
