#include <bits/stdc++.h>

using namespace std;

const int N = 70;
int n,k ;
long double wiiiiw ;
long double T[N] ;

int main()
{

    ifstream cin("C-small-1-attempt0.in");
    ofstream cout("out");
    int t ;
    cin >> t ;
    int test_case(1) ;
    while(t--)
    {
        cin >> n >> k ;
        cin >> wiiiiw ;
        for(int i = 0 ; i < n ; i++)cin >> T[i] ;
        sort(T,T+n) ;
        for(int i = 1 ; i < n ; i++)
        {
            long double somme = (T[i]-T[i-1])*i ;
            if(somme<=wiiiiw)
            {
                for(int j = 0 ; j < i ; j++)T[j] = T[i] ;
                wiiiiw -= somme ;
            }
            else
            {
                for(int j = 0 ; j < i ; j++)T[j] += (wiiiiw/(long double)i) ;
                wiiiiw = 0.0 ;
                break;
            }
        }
        for(int i = 0 ; i < n ; i++)T[i] += ( wiiiiw/(long double)n ) ;
        long double ans = 1.0 ;
        for(int i = 0 ; i < n ; i++)ans *= T[i] ;
        cout << "Case #"<<test_case++<<": "<<fixed << setprecision(6) << ans << endl;
    }


    return 0;
}
