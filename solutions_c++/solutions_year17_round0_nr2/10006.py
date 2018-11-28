#include <iostream>
#include <string>
#include <cmath>
#include <stack>
#include <deque>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <iomanip>

using namespace std;

int main()
{
	int T = 0;
	cin >> T;

	for (long long i = 1; i <= T; i++ )
	{
		// long long NN = 0;
		string N = "";
		cin >> N;
		string NN = N;
		bool f = false;

		if(N.size() == 1)
		{
			cout << "Case #" << i << ": "<< N << endl;
			continue;
		}

		if(N[0] == '1')
		{
			f = true;
			for(int j = 1; j < N.size(); j++)
			{
				if(N[j] != '0')
				{
					f = false;
					break;
				}
			}
		}

		if(f)
		{
			string temp = "";
			for(int j = 1; j < N.size(); j++)
			{
				temp += '9';
			}
			cout << "Case #" << i << ": "<< temp << endl;
		}
		else
		{
			for(int j = 0; j < N.size() - 1; j++)
			{
				if(N[j] > N[j + 1])
				{
					N[j] = (char) N[j] - 1;
					int k = j;
					j++;
					while(j < N.size())
					{
						N[j] = '9';
						j++;
					}

					for(; k > 0; k--)
					{
						if(N[k - 1] > N[k])
						{
							if(N[k] == '0' && N[k - 1] == '1')
							{
								string temp = "";
								for(int j = 1; j < N.size(); j++)
								{
									temp += '9';
								}
								N = temp;
								break;
							}
							else
							{
								N[k - 1] = N[k - 1] - 1;
								N[k] = '9';
								// N[k - 1] = N[k - 1] - 1;
							}
						}
						else
						{
							break;
						}
					}

					while(0 < N.size() && N[0] == '0')
					{
						N = N.substr(1);
					}
				}
			}

			cout << "Case #" << i << ": "<< N << endl;

		}

	}

	return 0;
}


