#include<bits/stdc++.h>
using namespace std ; 
typedef long long int ll ;
int main() 
{
   freopen("output.txt" , "w" , stdout ) ;
   freopen("input.txt"  , "r" , stdin ) ;
    ll  t ; 
    cin >> t; 
    int k1 = 1 ;
    while( t-- )
    {
        string s ; 
        ll ans =  0 , flag = 0 ;
        cin >> s ;
        int k ; 
        cin >> k ;
        for(int i = 0 ;i  < s.size() - k + 1  ; i++ ) 
        {
            if(s[i] == '-')
            {
                ans++ ;
                for(int j = i , cnt = 0 ; cnt < k ; j++ , cnt++ ) 
                {
                
                    if(s[j] == '-') 
                        s[j] = '+' ; 
                        else
                        s[j] = '-' ; 
                }
            } 
        } 
        cout << "Case #" << k1 << ": " ; 
        for(int i = 0 ; i < s.size() ; i++  ) 
        {
            if(s[i] == '-' ) 
            {
                flag = 1 ;
            }
        } 
        if(flag == 1) 
        {
            cout<<"IMPOSSIBLE" <<endl;
        }
        else
        cout << ans << endl; 
        
        k1++ ; 
    }
    return  0 ;
    
}
