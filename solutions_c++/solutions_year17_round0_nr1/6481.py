/*************************************************************************
    > File Name: OversizedPancakeFlipper.cpp
    > Author: ma6174
    > Mail: ma6174@163.com 
    > Created Time: 六  4/ 8 20:37:23 2017
 ************************************************************************/

#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
	freopen("in.in","r",stdin) ;
	freopen("out.out","w",stdout) ;
	int t ;
	cin >> t ;
	for(int i = 0; i < t; i++)
	{
		string s ;
		cin >> s ;
		int k ;
		int ans = 0 ;
		cin >> k ;
		for(int j = 0; j < s.length() - k + 1; j ++)
		{
			if(s[j] == '-')
			{
				for(int a = j; a < j + k; a++)
				{
					if(s[a] == '+')
						s[a] = '-' ;
					else
						s[a] = '+' ;
				}
				ans ++ ;
			}
		}
		printf("Case #%d: ",i + 1) ;
		int flag = 1 ;
		for(int a = 0; a < s.length(); a++)
			if(s[a] == '-')
				flag = 0 ;
		if(flag == 0)
			cout << "IMPOSSIBLE" << endl ;
		else
			cout << ans << endl ;
	}
	return 0 ;
}
