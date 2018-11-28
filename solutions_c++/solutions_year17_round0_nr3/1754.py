#include <iostream>
#include <bits/stdc++.h>


using namespace std;

pair<long long , long long> solve(long long n , long long k)
{

    if (n == 1) return make_pair(0,0) ;
    if (k == 1)
    {
        if (n % 2 == 1) return make_pair(n/2 , n/2) ;
        return make_pair(n/2 , max(n/2-1 , 0ll)) ;
    }

    if (n % 2 == 0 && k % 2 != 0)
    {
       return solve(n/2-1ll, k/2) ;
    }
    else
    {
       return solve(n/2 , k/2) ;
    }
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("o3.txt", "w", stdout);
    long long t , n , k ;
    cin >> t ;
    for(int i = 1 ; i <= t ; i++)
    {
        cin >> n >> k ;

        cout << "Case #" << i << ": "<<solve(n , k).first << " " <<  solve(n , k).second << endl ;
    }
    return 0;
}
