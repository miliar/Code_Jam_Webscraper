#include <bits/stdc++.h>
using namespace std;

#define FOR(n) for(int i = 0; i < n; i++) // From 0 to n-1
#define FORA(a, b) for(int i = (a); i <= (b); i++) // From a to b to increasing
#define DFOR(n) for(int i = n; i >= 0; i--) // From n to 0
#define DFORA(a, b) for(int i = (a); i >= (b); i--) // From a to b decrementing

#define N (int)1e5
#define INF 10000000000001
const int inf = 1e9 + 1 ;
const int mod = 1e9 + 7 ;

string solve(int n, int a[])
{
    bool all = false ;
    int i = 1;
    while(i < n)
    {
        if(a[i] < a[i-1])
        {
            while(i > 0 and a[i] <= a[i-1])
                i-- ;
            a[i] -= 1; i++;
            while(i < n)
            {
                a[i] = 9;
                i++;
            }
            break ;
        }
        i++;
    }

    string num ;
    i = 0;

    while(i < n and a[i] == 0) i++ ;
    if(i == n)
        num += '0';

    for(; i < n; i++)
        num += (char) ( a[i] + 48 ) ;
    return num ;
}

int main()
{
    ofstream fout("B-large.out");
    ifstream fin("B-large.in");

    int t; fin >> t ;
    for(int j = 1; j <= t; j++)
    {
        string s ; fin >> s ;
        int n = s.length() ;
        int a[n] ;
        FOR(n)
            a[i] = s[i] - '0' ;
        string ans = solve(n, a) ;
        cout << "Input: " << s << " \nCase #" << j << ": " << ans << endl << endl ;
        fout << "Case #" << j << ": " << ans << endl ;
    }

    return 0;
}

