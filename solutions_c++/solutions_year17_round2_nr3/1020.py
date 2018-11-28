#include <iostream>
#include <vector>
#include <iomanip>
#include <set>
#include <cmath>


using namespace std ;


const int maxN = 101 ;

long long lim_dist[maxN+2], speed[maxN+2], nxt_dist[maxN+2] ;
double memo[maxN+2] ;

void solve()
{
	int N, Q ;

	cin >> N >> Q ;

	for(int i = 1 ; i <= N ; i++)
		cin >> lim_dist[i] >> speed[i] ;

	int tmp ;
	for(int i = 1 ; i <= N ; i++)
		for(int j = 1 ; j <= N ; j++)
		{
			cin >> tmp ;

			if(i + 1 == j)	
				nxt_dist[i] = tmp ;
		}

	int u, v ;
	cin >> u >> v ;

	memo[N] = 0 ;

	long long covered = 0 ;
	for(int i = N-1 ; i >= 1 ; i--)
	{
		covered = 0 ;
		memo[i] = 1e30 ;
		for(int j = i+1 ; j <= N ; j++)
		{
			covered += nxt_dist[j-1] ;

			if(covered > lim_dist[i])
				break ;

			memo[i] = min(memo[i], (1.0 * covered / speed[i]) + memo[j]) ;
		}
	}

	cout << fixed << setprecision(12) << memo[1] ;
}

int main()
{
    ios::sync_with_stdio(false) ;
    cin.tie(0) ;
    
    int T ;
    cin >> T ;
    
    for(int i = 1 ; i <= T ; i++)
    {
        cout << "Case #" << i << ": " ;
        solve() ;
        cout << "\n" ;
    }
    
    
    return 0 ;
}