#include <iostream>
#include <string.h>
#include <math.h>
using namespace std;



int main(int argv, char* args[])
{
	int t;
	cin >> t;
	char ch;
	char ser[1000];
	int arr[1000], ptr=0;
	int plus=0, minus=0;
	for(int z=1; z<=t; z++)
	{
		char ser[1000];
		int k;
		cin >> ser;
		cin >> k;
		ch = ser[0];
		int flip = 0;
		for(int i=strlen(ser) - 1; i>=0; i--)
		{
			//cout << "For i = "<< i << endl;
			if(ser[i] == '+')
				continue;
			else
			{
				flip ++;
				if(i+1>=k)
				{
					for(int j=0; j<k; j++)
					{
						int z = i-j;
						if(ser[z] == '+')
						{
							ser[z] = '-';
						}
						else
						{
							ser[z] = '+';
						}
					}
				}
				else
				{
					flip = -1;
					break;
				}
			}

			
		}

		if(flip >= 0)
			cout << "Case #" <<  z<< ": "<< flip;
		else
			cout << "Case #" <<  z<< ": "<< "IMPOSSIBLE";
		cout << endl;
	}
}