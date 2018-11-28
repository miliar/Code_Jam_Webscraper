/**
submitted by:
prakhar8795
SLEEP. EAT. CODE. REPEAT.
*/

#include<bits/stdc++.h>
using namespace std ;


int main()
{
    freopen("A-large.in","r", stdin) ;
    //freopen("A-large-out.out","w",stdout) ;
    int test ;
    cin>>test ;
    int k=1 ;
    while(test--) {
        int n ;
        long long int d ;
        cin>>d ;
        cin>>n ;
        double currMax=-1 ;
        for(int i=0 ; i<n ; i++) {
            long long int k1 ;
            int s ;
            cin>>k1>>s ;
            double ti = (d-k1)/ (double)s ;
            if(ti>currMax) {
                currMax = ti ;
            }
        }
        double res = d/currMax ;
        cout << "Case #"<<k <<":" << " " ;
        printf("%f\n",res) ;
        k++ ;
    }

    return 0 ;
}

