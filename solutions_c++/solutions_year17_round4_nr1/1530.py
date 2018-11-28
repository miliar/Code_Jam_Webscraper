#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector> 

using namespace std;

#define ll long long
#define endl '\n'



int main()
{
//	ios::sync_with_stdio(false);
//	cin.tie(0);
	
	int g[1000];
	
	int T;
	cin >>T;
	for(int t=1; t<=T; t++)
	{
		int n,P;
		cin >> n >> P;
		for(int i=0; i<n; i++)
		{
			cin >> g[i];
			g[i] %= P;
		}
		
		int ans = 0;
		int cnt[5] = {0,0,0,0,0};
		for(int i=0; i<n; i++)
			cnt[g[i]]++;
		
		
		switch(P){
			case 2:
			{
				ans = cnt[0];
				ans += cnt[1]/2;
				cnt[1] = (cnt[1]&1);
				break;
			}
			case 3:
			{
				ans = cnt[0];
				
				int set_12 = min(cnt[1],cnt[2]);
				ans += set_12;
				cnt[1] -= set_12;
				cnt[2] -= set_12;
				
				ans += cnt[1]/3;
				ans += cnt[2]/3;
				cnt[1] %= 3;
				cnt[2] %= 3;
				break;
			}
			case 4:
			{
				ans = cnt[0];
				int set_13 = min(cnt[1],cnt[3]);
				int set_22 = cnt[2]/2;
				cnt[1] -= set_13;
				cnt[3] -= set_13;
				cnt[2] -= set_22*2;
				ans += set_13;
				ans += set_22;
				
				int set_233 = min(cnt[2], cnt[3]/2);
				int set_211 = min(cnt[2], cnt[1]/2);
				cnt[2] -= set_233;
				cnt[2] -= set_211;
				cnt[1] -= set_211*2;
				cnt[3] -= set_233*2;
				ans += set_233;
				ans += set_211;
				
				ans += cnt[1]/4 + cnt[3]/4;
				cnt[1] %= 4;
				cnt[3] %= 4;
				
				break;
			}
		}
		
	//	cout << "ans_0 = " <<ans <<endl;
		
		bool left = 0;
		for(int i=1; i<P; i++)
			if(cnt[i]>0)
				left = true;
		if(left)
			ans++;
		
		cout << "Case #"<< t <<": "<< ans <<endl;
	}
	
	return 0;
}


