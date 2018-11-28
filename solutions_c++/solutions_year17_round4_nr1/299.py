#include <bits/stdc++.h>
using namespace std;

int arr[100];
int cnt[4];

int main()
{
	int t;
	cin >> t;

	for(int cn=1; cn<=t; cn++)
	{
		int n,p;
		cin >> n >> p;
		for(int i=0; i<n; i++)
			cin >> arr[i];

		int ans = 0;

		for(int i=0; i<p; i++)
			cnt[i] = 0;
		for(int i=0; i<n; i++)
			cnt[arr[i]%p]++;

		if(p==2)
		{
			ans = cnt[0] + (cnt[1]+1)/2;
		}
		else if(p==3)
		{
			ans = cnt[0];

			int m = min(cnt[1],cnt[2]);
			ans += m;
			cnt[1] -= m;
			cnt[2] -= m;

			if(cnt[1])
				ans += (cnt[1]+2)/3;
			else
				ans += (cnt[2]+2)/3;
		}
		else if(p==4)
		{
			ans = cnt[0];
			ans += cnt[2]/2;
			cnt[2] %= 2;

			int m = min(cnt[1],cnt[3]);
			ans += m;
			cnt[1] -= m;
			cnt[3] -= m;

			if(cnt[2])
			{
				ans += 1+(max(cnt[1],cnt[3])+1)/4;
			}
			else
			{
				ans += (max(cnt[1],cnt[3])+3)/4;
			}
		}

		cout << "Case #" << cn << ": " << ans << endl;
	}

	return 0;
}