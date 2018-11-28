#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
bool done;

void calculate(std::vector<int>& v)
{
	int target = INT_MIN;
	for (int i = 0; i < v.size() - 1; ++i)
	{
		if (v[i+1]<v[i])
		{
			target = i;
		}
	}
	if (target == INT_MIN)
	{
		done = true;
		return;
	}
	v[target]--;
	for (int i = target + 1; i < v.size(); ++i)
	{
		v[i] = 9;
	}

	return;
}
int main()
{
	int t;
	cin>>t;
	int testCaseNum = 0;
	while(t--)
	{
		ull n;
		cin>>n;
		testCaseNum++;
		printf("Case #%d: ", testCaseNum);
		done=false;
		if ((n/10)==0)
		{
			printf("%llu\n", n );
			continue;
		}
		stack<int> stc;
		std::vector<int> v;
		while(n!=0)
		{
			stc.push(n%10);
			n/=10;
		}
		while(!stc.empty())
		{
			v.push_back(stc.top());
			stc.pop();
		}
		while(!done)
		{
			calculate(v);
		}
		bool zero = true;
		for (int i = 0; i < v.size(); ++i)
		{
			if (v[i] !=0)
			{
				zero = false;
			}
			if (!zero)
			{
				printf("%d", v[i]);
			}
		}
		printf("\n");
	}


	return 0;
}