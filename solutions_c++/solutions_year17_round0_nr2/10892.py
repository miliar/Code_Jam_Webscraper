#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include<set>
#include<vector>

using namespace std;
int check_num(unsigned long long N)
{
	int t=N;
	int s = t%10;
	int s1;
	t=t/10;
	while(t>0)
	{
		s1 = t%10;
		if(s1>s)
			return 0;
		else
		{
			s = s1;
			t = t/10;
		}

	}
	return 1;
}
int main() 
{
	int test_case, i, j, k,r,c;
	unsigned long long N;
	freopen("input.txt","r",stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d\n",&test_case);

	for(i=0; i< test_case; i++)
	{
		scanf("%d\n",&N);
		if(N<10)
			printf("Case #%d: %d\n",i+1,N);
		else
		{

			while(N>0)
			{
			if(check_num(N)==0)
				N=N-1;
			else
			{
			printf("Case #%d: %d\n",i+1,N);
			break;
			}
			}
		}
	}

	return 0;
}