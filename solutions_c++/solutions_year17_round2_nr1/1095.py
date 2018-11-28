#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>

using namespace std ;


void solve()
{
	long long D, N, K, S ;
	double cur_t, max_t = 1e-31, ans ;

	cin >> D >> N ;

	for(int i = 1 ; i <= N ; i++)
	{
		cin >> K >> S ;

		cur_t = (1.0 * (D-K)) / S ;

		if(i == 1)
			max_t = cur_t ;
		else
			max_t = max(max_t, cur_t) ;
	}

	ans = D / max_t ;
	cout << fixed << setprecision(12) << ans ;
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