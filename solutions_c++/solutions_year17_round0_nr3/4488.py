#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

const int MAX_N = 1000000 + 10 ;

struct rarea
{
	int x , y ;
}area[MAX_N] ;
struct data
{
	long long x , y , s ;
}queue[MAX_N] ;

int cur , n , k ;

int main()
{
	freopen("input.txt" , "r" , stdin) ;
	freopen("output.txt" , "w" , stdout) ;

	int T , caseNUM = 1 ; scanf("%d" , &T) ;
	for (; T-- ; ++caseNUM)
	{
		int L = 1 , R = 1 ;
		scanf("%d %d" , &n , &k) ;

		///
		
		cur = 0 ; area[1].x = area[1].y = 1 ;
		queue[1].x = 1 ; queue[1].y = n ; queue[1].s = n ;
		for (;;)
		{
			int maxa = 0 ;
			++cur ;
			for (int i = area[cur].x ; i <= area[cur].y ; ++i)
			{
				int x = queue[i].x , y = queue[i].y , mid = (x + y) / 2 , s = std::max(mid - x , y - mid) ;
				maxa = std::max(maxa , s) ;
			}

			if (!maxa) break ;

			for (int i = area[cur].x ; i <= area[cur].y ; ++i)
			{
				int x = queue[i].x , y = queue[i].y , mid = (x + y) / 2 ;
				data lson = (data){x , mid - 1 , mid - x} ,
					 rson = (data){mid + 1 , y , y - mid} ;

				if (lson.s == maxa && lson.s) queue[++R] = lson ;
				if (rson.s == maxa && rson.s) queue[++R] = rson ;
			}
			for (int i = area[cur].x ; i <= area[cur].y ; ++i)
			{
				int x = queue[i].x , y = queue[i].y , mid = (x + y) / 2 ;
				data lson = (data){x , mid - 1 , mid - x} ,
					 rson = (data){mid + 1 , y , y - mid} ;

				if (lson.s != maxa && lson.s) queue[++R] = lson ;
				if (rson.s != maxa && rson.s) queue[++R] = rson ;
			}
			
			area[cur + 1].x = L + 1 ; area[cur + 1].y = R ;
			L = R ;
		}

		///

		printf("Case #%d: " , caseNUM) ;
		int x = queue[k].x , y = queue[k].y , mid = (x + y) / 2 ,
			s1 = y - mid , s2 = mid - x ;
		printf("%d %d\n" , std::max(s1 , s2) , std::min(s1 , s2)) ;
	}

	return 0 ;
}
