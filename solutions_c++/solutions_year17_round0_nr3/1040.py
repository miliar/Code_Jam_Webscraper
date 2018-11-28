#include <vector>
#include <map>
#include <iostream>

using namespace std ;


inline pair<long long, long long> getNext(long long x)
{
    if(x == 0)
        return make_pair(0, 0) ;

    if(x % 2 == 0)
        return make_pair(x/2, (x/2)-1) ;
    
    return make_pair(x/2, x/2) ;
}

int main()
{
    ios::sync_with_stdio(false) ;
    cin.tie(0) ;

    int T ;

    cin >> T ;

    long long N, K, at, ans1, ans2, freq ;
    pair<long long, long long> tmp ;
    map<long long, long long>::iterator it ;
    map<long long ,long long> Q ;

    for(int c = 1 ; c <= T ; c++)
    {
        cin >> N >> K ;

        Q.clear() ;
        Q[-N]++ ;

        while(true)
        {
            it = Q.begin() ;
            at = it->first ;
            freq = it->second ;
            Q.erase(it) ;

            at *= -1 ;

            tmp = getNext(at) ;

            K -= freq ;
            if(K <= 0)
            {
                ans1 = tmp.first ;
                ans2 = tmp.second ;

                cout << "Case #" << c << ": " << ans1 << " " << ans2 << "\n" ;
                break ;
            }


            Q[-tmp.first] += freq ;
            Q[-tmp.second] += freq ;
        }   
    }   

    
    
    
    return 0;
}