#include <iostream>
#include <cstring>
#include <vector>
using namespace std;
int T;
int N;
int ca=1;
bool ok(int n)
{
	string s=to_string(n);
	for(int i=1;i<s.length();i++)
	{
		if(s[i]<s[i-1])
			return false;
	}
	return true;
}
int main()
{
	scanf("%d",&T);
	vector<int> table(1007);
	table[0]=0;
	for(int i=1;i<=1000;i++)
	{
		if(ok(i))
		{
			table[i]=i;
		}
		else
			table[i]=table[i-1];
	}
	while(T--)
	{
		scanf("%d",&N);
		printf("Case #%d: %d\n",ca++,table[N]);
	}
	return 0;
}