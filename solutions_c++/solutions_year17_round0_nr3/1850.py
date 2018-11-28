#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

ll N,K;
ll a,b;
ll t1,t2;

int main()
{
	int testN;

	cin >> testN;

	for(int test=1; test<=testN; test++)
	{
		printf("Case #%d: ",test);

		cin >> N >> K;

		ll cur = N;
		ll res;
		a=1;
		b=0;

		while(1)
		{
			K-=b;
			if(K<=0)
			{
				res = cur+1;
				break;
			}

			K-=a;
			if(K<=0)
			{
				res = cur;
				break;
			}

			t1=t2=0;

			if(cur&1)
			{
				t1 = a*2 + b;
				t2 = b;
			}

			else
			{
				t1 = a;
				t2 = a + 2*b;
			}

			a = t1;
			b = t2;

			cur = (cur-1)/2;
		}

		cout << res/2 << " " << (res-1)/2 << endl;
	}
}
