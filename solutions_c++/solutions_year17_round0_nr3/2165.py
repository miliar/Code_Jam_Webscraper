#include <bits/stdc++.h>

using namespace std;

#define ll long long

int main()
{
	ll t,tt,n,k,index1,index2,val,ans1,ans2,val1,val2;
	cin >> t;
	for(tt=1;tt<=t;tt++)
	{
		cin >> n >> k;
		cout << "Case #" << tt << ": " ;
		pair<ll,ll> a[2][2];
		a[0][0] = make_pair(n/2,1);
		a[0][1] = make_pair((n-1)/2,1);
		a[1][0] = make_pair(-1,0);
		a[1][1] = make_pair(-1,0);
		index1 = 0;
		index2 = 1;
		val = 1;
		if(k==1)
		{
			cout << a[0][0].first << " " << a[0][1].first << endl;
		}
		else
		{
			while(1)
			{
				if(val+a[index1][0].second>=k)
				{
					ans1 = a[index1][0].first/2;
					ans2 = (a[index1][0].first-1)/2;
					break;
				}
				else
				{
					val += a[index1][0].second;
					val1 = a[index1][0].first/2;
					val2 = (a[index1][0].first-1)/2;
					if(val1!=val2)
					{
						a[index2][0].first = val1;
						a[index2][1].first = val2;
						a[index2][0].second += a[index1][0].second;
						a[index2][1].second += a[index1][0].second;
					}
					else
					{
						a[index2][0].first = val1;
						a[index2][0].second += (2*a[index1][0].second);
					}
				}

				if(a[index1][1].first!=-1&&(val+a[index1][1].second>=k))
				{
					ans1 = a[index1][1].first/2;
					ans2 = (a[index1][1].first-1)/2;
					break;
				}
				else
				{
					val += a[index1][1].second;
					val1 = a[index1][1].first/2;
					val2 = (a[index1][1].first-1)/2;
					if(val1!=val2)
					{
						a[index2][0].first = val1;
						a[index2][1].first = val2;
						a[index2][0].second += a[index1][1].second;
						a[index2][1].second += a[index1][1].second;
					}
					else
					{
						a[index2][1].first = val1;
						a[index2][1].second += (2*a[index1][1].second);
					}
				}

				if(index1==0)
				{
					index1 = 1;
					index2 = 0;
				}
				else
				{
					index1 = 0;
					index2 = 1;
				}
				a[index2][0] = make_pair(-1,0);
				a[index2][1] = make_pair(-1,0);
			}
			cout << ans1 << " " << ans2 << endl;
		}
	}
	return 0;
}