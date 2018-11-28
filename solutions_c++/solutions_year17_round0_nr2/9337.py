// B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <conio.h>

using namespace std;

int main()
{
	int i;
	unsigned long long N;
	string tmp,q;
	int T,gg=1;
	cin >> T;

	for (int j = 0; j < T; j++)
	{
		cin >> N;
		gg = 0;
		cout << "Case #" << j+1;
		while (N>0)
		{
			
			tmp = to_string(N);
			
			for (i = 0; i < tmp.length() - 1; i++)
			{
				if (tmp[i] > tmp[i + 1])
				{
					if (gg == 0)
					{
						q = tmp;//11111111111111110 
						q = q.erase(0, i + 1);//76543
						N -= stoull(q); //9800000
						tmp = to_string(N);
						gg++;
					}
					else
					{
						N--;
						tmp = to_string(N);
						gg = 0;
						break;
					}
					i = -1; //like brake 
				}
			}
			if (i == (tmp.length() - 1))
			{
				cout << ": " <<N<<endl; break;
			}
				
		}
			
		}
	return 0;
}

