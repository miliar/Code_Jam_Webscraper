#include<bits/stdc++.h>
using namespace std;
int tidy( long long n )
{
    int temp = n%10;
    n /= 10;
    while( n/10 != 0 ){
        if( temp < (n%10) ) return 0;
        temp = n%10;
        n/= 10;
    }
    if( temp < n ) return 0;
    return 1;
}
int main()
{
    freopen("B-small-attempt2.in.","r",stdin);
    int t;
    cin >> t;
    freopen("output.txt","w",stdout);
    long long n;
    for( long long i = 1; i <= t; i++){
        cin >> n;
        for( long long j = n; j >= 0; j-- ){
            if( tidy(j) == 1 ){
                cout<< "Case #" << i << ": " << j << endl;
                break;
            }
        }
    }
    return 0;
}
