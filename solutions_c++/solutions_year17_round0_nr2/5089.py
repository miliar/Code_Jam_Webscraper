#include <stdio.h>
#include <string.h>
#include <queue>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
	int T;
	scanf("%d",&T);
	//freopen("1.out","w",stdout);
	for(int t= 0; t< T;t++)
	{
		char s[100];
		scanf(" %s", s);
		printf("Case #%d: ",t+1);
		char ans[100];
		bool m[100] = {false};
		int fr = 0;
		for(int i = 1; i < strlen(s); i++)
		{
			int c;
			c = s[i]-'0';
			//if(m) c--;

			if(s[i-1]-'0'>c || c <= 0)
			{
				m[i] = true;
				s[i] ='9';
				for(int j = i-1; j >=fr ;j--)
				{
					//printf("%d %d %d\n",j,m[j],s[j]-'0');
					int num = s[j]-'0';
					num--;

					if( j== fr || m[j] || num >= s[j-1]-'0')
					{
						if(!m[j])s[j]--;
						m[j] = true;
						while(s[fr]=='0')
							fr++;
						break;
					}
					else
					{
						m[j] = true;
						s[j]='9';
					}
				}
			}
			else m[i] =false;
			//printf("%s\n",s);

		}
		//if(m) s[0]--;
		int p = 0;
		for(int i = 0; i < strlen(s); i++)
			if(s[i] !='0')
			{
				p= i;
				break;
			}

		printf("%s\n",s+p);
	}
	return 0;
}
