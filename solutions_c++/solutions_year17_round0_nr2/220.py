#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<string>
#include<set>
#include<sstream>
using namespace std;
typedef long long lld;
#define mp make_pair
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define eps 1e-8
#define pi acos(-1.0)
char str[100010];
bool check(lld s)
{
	lld small=s%10;
	while(s)
	{
		if(s%10 > small)
			return false;
		small=min(small,s%10);
		s/=10;
	}
	return true;
}
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		lld s;
		scanf("%I64d",&s);
		lld end=0;
		while(s)
		{
			if(check(s))
				break;
			end=end*10+9;
			s/=10;
			s--;
		}
		printf("Case #%d: ",cc);
		if(s != 0)
			printf("%I64d",s);
		if(end != 0)
			printf("%I64d",end);
		printf("\n");
	}
	return 0;
}
/*
4
132
1000
7
111111111111111110

 */
