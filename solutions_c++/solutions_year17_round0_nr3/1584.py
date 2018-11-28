#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define all(v) v.begin(), v.end()
#define F first
#define S second
#define make0 memset(a,0,sizeof(a))
#define p push_back
#define fast_cin() ios_base::sync_with_stdio(false)
#define pi pair <int,int>
#define pll pair <ll,ll>

ll ceil(ll A, ll B)
{
	if(A%B == 0)
		return A/B;
	return A/B + 1;
}



int main()
{
	fast_cin();
	ll p2[61];
	for(int i=1;i<=60;i++)
		p2[i] = pow(2,i);
	int T;
	cin >> T;
	for(int f=1;f<=T;f++)
	{
		cout << "Case #" << f << ": " ;
		ll N,K;
		cin >> N >> K;
		N--;
		if(K == 1)
		{
			cout << ceil(N,2) << ' ' << N/2 << endl;
			continue;
		}
		ll ct=1;
		ll counter = 1;
		pll nums[2] = {{N/2,1},{ceil(N,2),1}};
		sort(nums,nums+2);
		while(true)
		{
			sort(nums,nums+2);
			reverse(nums,nums+2);
				// cout << nums[0].F << ' ' << nums[0].S << "	" << nums[1].F << ' ' << nums[1].S << endl;
			if(counter + p2[ct] >= K)
			{
				// cout << ct << ' ' << counter << ' ' << K << endl;
				if(nums[0].S + counter >= K)
				{
					nums[0].F --;
					cout << ceil(nums[0].F, 2) << ' ' << nums[0].F/2 << endl;
				}
				else
				{
					nums[1].F --;
					cout << ceil(nums[1].F, 2) << ' ' << nums[1].F/2 << endl;
				}
				break;

			}
			pll a = {nums[0].F - 1, nums[0].S};
			pll b = {nums[1].F - 1, nums[1].S};
			pll nn[4];
			nn[0] = {ceil(a.F,2), a.S};
			nn[1] = {a.F/2, a.S};
			nn[2] = {ceil(b.F,2), b.S};
			nn[3] = {b.F/2, b.S};
			sort(nn, nn+4);
			reverse(nn,nn+4);
			int idx = -1;
			for(int i=0;i<3;i++)
			{
				if(nn[i].F != nn[i+1].F)
				{
					idx = i;
					break;
				}
			}
			// cout << "idx: " << idx << endl;
			// for(int i=0;i<4;i++)
			// 	cout << nn[i].F << ' ' << nn[i].S << "	";
			// cout << endl;
			if(idx == -1)
			{
				nums[0] = {nn[0].F, nn[0].S + nn[1].S + nn[2].S + nn[3].S};
				nums[1] = {0,0};
			}
			else
			{
				ll sum = 0;
				for(int i=0;i<=idx;i++)
					sum += nn[i].S;
				nums[0] = {nn[0].F,sum };
				sum = 0;
				for(int i=idx+1;i<4;i++)
					sum += nn[i].S;
				nums[1] = {nn[idx+1].F, sum};
			}
			counter += p2[ct];
			ct++;
		}
	}
	return 0;
}