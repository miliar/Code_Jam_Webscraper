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
		char s[1024];
		
		scanf("%s", s);
		int len = strlen(s);
		int ans = 0;
		bool flag = true;
		
		for(int i = 0; i < len; i ++)
		{
			if(i+1 < len && s[i] > s[i+1])flag = false;
		}

		if(flag == false)
		{
			for(int i = 0; i < len; i ++)
			{
				if(flag == false)
				{
					if(i+1 < len && s[i] >= s[i+1])
					{
						s[i] --;
						s[i+1] = '9';
						flag = true;
					}
				}
				else 
				{
					s[i] = '9';
				}
			}
			
			int start = 0;
			while(s[start] == '0' && start+1 < len)start ++;
			cout << "Case #" << index << ": " << s + start << endl;
		}
		else
		{
			cout << "Case #" << index << ": " << s << endl;
		}
	}
}
