#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int t;
	cin >> t;
	for (int i=0; i<t; i++)
	{
		string s;
		int k;
		cin >> s >> k;
		int index=0;
		int flips=0;
		bool impossible=false;
		while (index<s.length()-k+1)
		{
			if (s[index]=='-')
			{
				flips++;
				for (int j=index; j<index+k; j++)
				{
					if (s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
				}
			}
			index++;
		}
		while (index<s.length())
		{
			if (s[index]=='-')
				impossible=true;
			index++;
		}
		if (impossible)
			printf ("Case #%d: IMPOSSIBLE\n",i+1);
		else
			printf ("Case #%d: %d\n",i+1,flips);
	}
}
