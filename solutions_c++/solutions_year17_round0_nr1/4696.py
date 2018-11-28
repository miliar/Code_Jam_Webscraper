#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

int main()
{
    int T,K;
	char S[1005];
	int count = 0;
	bool can;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
		can = true;
		count = 0;
		cin >> S >> K;
		for(int a=0;a<1005 && S[a] !='\0' && can;a++)
		{
			if(S[a] == '-')
			{
				count += 1;
				for(int b=a;b<a+K;b++)
				{
					if(S[b] == '\0')
					{
						can = false;
						break;
					} else {
						if(S[b] == '-')
						{
							S[b] = '+';
						} else {
							S[b] = '-';
						}
					}
				}
			}
		}
		printf("CASE #%d: ",i);
		if(can)
		{
			cout << count << endl;
		} else {
			cout << "IMPOSSIBLE" << endl;
		}
	}
    return 0;
}

