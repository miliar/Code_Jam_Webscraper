#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

int main(){
	int T;
	cin >> T;
	int index = 0;

	while (index++ < T){
		int K;
		char s[1024];
		
		scanf("%s %d", s, &K);
		int len = strlen(s);
		int ans = 0;
		for(int i = 0; i+K <= len; i ++)
		{
			if(s[i] == '-')
			{
				for(int j = 0; j < K; j ++)
				{
					if(s[i+j] == '-')s[i+j] = '+';
					else s[i+j] = '-';
				}
				ans ++;
				//puts(s);
			}
		}
		for(int i = len-K; i < len; i ++)
		{
			if(s[i] == '-')ans = -1;
		}
		if(ans >= 0)
		{
			cout << "Case #" << index << ": " << ans << endl;
		}
		else
		{
			cout << "Case #" << index << ": IMPOSSIBLE" << endl;
		}
	}
}
