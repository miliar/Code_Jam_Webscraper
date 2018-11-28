#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

int main(){
	int T;
	cin >> T;
	int index = 0;
	
	int seat_c[1024];
	int tick_c[1024];
	
	while (index++ < T){
		int N, C, M;
		int P, B;
		int ans = 0;
		memset(seat_c, 0, sizeof(seat_c));
		memset(tick_c, 0, sizeof(tick_c));
		scanf("%d%d%d", &N, &C, &M);
		while(M --)
		{
			scanf("%d%d", &P, &B);
			seat_c[P] ++;
			tick_c[B] ++;
			
			ans = max(ans, tick_c[B]);
		}
		
		int free = 0;
		int ans2 = 0;
		
		for(int i = 1; i <= N; i ++)
		{
			while(ans+free < seat_c[i])
			{
				ans ++;
				free += i-1; 
			}
			free += (ans - seat_c[i]);
		}
		
		for(int i = 1; i <= N; i ++)
		{
			if(seat_c[i] > ans)
			{
				ans2 += seat_c[i] - ans;
			}
		}

		cout << "Case #" << index << ": " << ans << ' ' << ans2 << endl;
	}
	return 0;
}
