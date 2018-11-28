#include <iostream>
#include <string.h>

using namespace std;

int main () {
	unsigned int t;
	cin >> t;
	for (int i1 =1;i1<=t;i1++) {
		string a;
		int k;
		cin >> a;
		cin >> k;
		int count = 0;
		int i = 0;
		while (i <a.length()) {
			if (a[i] == '-')
			{
				if (i+k<=a.length()) 
				{
					count++;
					for (int j = i;j<i+k;j++) {
						if (a[j] == '-') 
						{
							a[j] = '+';
							/* code */
						}
						else {
							a[j] = '-';
						}
					}
				}
				else {
					i = -1;
					break;
				}

			}

			i++;
		}
		if (i == -1) 
		{
			cout <<"Case #"<<i1<<": "<<"IMPOSSIBLE"<<endl;
			/* code */
		}
		else {
			cout <<"Case #"<<i1<<": "<<count<<endl;
		}

	}
	return 0;
}