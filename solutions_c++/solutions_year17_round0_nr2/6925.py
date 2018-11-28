#include<cstdio>
#include<cstring>
#include<iostream>

using namespace std;

char num[20];
char output[20];

int main()
{
	int t, past = 0, now;
	bool isTidy = true;
	cin >> t;
	for(int time = 1; time <= t; time++)
	{
		cin >> num;
		past = 0;
		isTidy = true;
		for(int i = 0; i < strlen(num); i++)
		{
			if(!isTidy)
			{
				output[i] = '9';
				continue;
			}
			if(num[i] < past)
			{
				isTidy = false;
				output[i - 1] -= 1;
				output[i] = '9';
				for(int j = i; j > 0; j--)
				{
					if(output[j] < output[j - 1])
					{
						output[j - 1] -= 1;
						output[j] = '9';
					}
				}
			}
			else
			{
				output[i] = num[i];
			}
			past = output[i];
		}
		output[strlen(num)] = '\0';
		cout << "Case #" << time << ": ";
		for(int i = 0; i < strlen(output); i++)
		{
			if(output[i] == '0')
				continue;
			else cout << output[i];
		}
		cout << "\n";
	}
}

