#include <vector>
#include <deque>
#include <iostream>

using namespace std ;


int main()
{
    ios::sync_with_stdio(false) ;
    cin.tie(0) ;

    int T ;

    cin >> T ;

    long long N, ans ;
    deque<int> ar ;
    for(int c = 1 ; c <= T ; c++)
    {
        cin >> N ;

        ar.clear() ;

        while(N > 0)
        {
            ar.push_front(N % 10) ;
            N /= 10 ; 
        }

        int till = ar.size() ;

        for(int i = till-1 ; i >= 1 ; i--)
        {
            if(ar[i] >= ar[i-1])
                continue ;

            ar[i-1]-- ;

            for(int j = i ; j < till ; j++)
                ar[j] = 9 ;
        }

        ans = 0 ;

        for(int i = 0 ; i < till ; i++)
        {
            ans *= 10 ;
            ans += ar[i] ;
        }

        cout << "Case #" << c << ": " << ans << "\n" ;
    }   

    
    
    
    return 0;
}