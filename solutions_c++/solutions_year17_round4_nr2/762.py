
/* 
Take yourself as work in progress.
-Bhai
*/

#include<bits/stdc++.h>
using namespace std;

#define LL long long
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define VI vector<int>
#define SZ(a) int(a.size())
#define TR(c, it) for(typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++ )
#define SET(a, b) memset(a, b, sizeof(a))

int N, M, C;
int arr[1005][1005];
int tickets[1005];

int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	int nahoy = 1;
	while(t--)
	{
		cin >> N >> C >> M;
		SET(arr, 0);
		SET(tickets, 0);
		assert(C==2);
		for(int i=0; i<M; i++)
		{
			int B, P;
			cin >> P >> B;
			arr[B][P]++;
			tickets[B]++;
		}
		int ans = max(tickets[1], tickets[2]);
		
		if(arr[1][1] + arr[2][1] > ans)
			ans = arr[1][1] + arr[2][1];

		int pro = 0;
		for(int i=2; i<1005; i++)
		{
			if(arr[1][i] + arr[2][i] > ans)
				pro += arr[1][i] + arr[2][i] - ans;
		}
		printf("Case #%d: %d %d\n", nahoy, ans, pro);
		nahoy++;
	}
	return 0;
}
