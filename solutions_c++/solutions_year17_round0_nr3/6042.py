#include<bits/stdc++.h>

using namespace std;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","wb",stdout);

	int t;
	int test = 1;
	scanf("%d",&t);

	while(t--)	
	{
		long long int n;
		long long int k;
		long long min_val = LLONG_MAX;
		long long int max_val = 0;
		int count = 0;
		scanf("%lld",&n);
		scanf("%lld",&k);

		priority_queue<long long int> p;

		p.push(n);

		while(!p.empty() && (count < k))
		{
			min_val = LLONG_MAX;
			max_val = 0;
			long long int x = p.top();
			long long int val;
			long long int o_val;
			if(x%2 == 0)
			{
				val = x/2;
				o_val = x-val;
				val -= 1;
				p.push(val);
				p.push(o_val);
				min_val = min(val,o_val);
				max_val = max(val,o_val);
				//cerr << "first: "<< val << " "<<o_val << endl;
			}
			else
			{
				val = x/2;
				p.push(val);
				p.push(val);
				min_val = val;
				max_val = val;
				//cerr << "second: " << val << " "<< val << endl;
			}


			p.pop();
			count++;
		}
		printf("Case #");
		printf("%d",test);
		printf(": ");
		printf("%lld %lld\n",max_val,min_val);
		test++;
	}
	return 0;
}

