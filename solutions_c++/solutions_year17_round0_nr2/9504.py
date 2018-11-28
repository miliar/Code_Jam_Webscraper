#include<bits/stdc++.h>
using namespace std ; 
typedef long long int ll ;
int main() 
{
    freopen("output.txt" , "w" , stdout ) ;
    freopen("input.txt"  , "r" , stdin ) ;
    ll t  ; 
    int k1 = 1 ; 
    cin >> t ; 
    while( t-- )
    {
        string s , s1; 
        cin >> s ;
        s1 = s ;
        int k = 0 , flag = 0 , flag1 = 0 ;
        int m = 0 ; 
        for(int i = 1 ; i < s.size() ; i++ ) 
        {
            if( s[i] < s[i-1] )
            {
                k = i  ;
                m = i - 1 ;   
                flag1 = 1 ;             
            }
                
        } 
        
        while(s[k] < s[k-1] && k > 0)
        {
                    
                s[k-1] = s[k-1] - 1 ;          
                m = k - 1 ;  
                k-- ;    
        }   
        
        if(m == 0 && s[m] == '0' && flag1 == 1) 
        {
                flag = 1 ;
        }     

        cout << "Case #" << k1 << ": " ; 
        if(flag1==1 )
        {
            if(flag == 1) 
            {
                for(int i = 0 ; i < s.size() - 1 ; i++ ) 
                {
                        cout<<9 ; 
                } 
            }
            else
            {
                int  i ; 
                for( i = 0 ; i <= m ; i++ ) 
                { 
                    cout << s[i] ; 
                }  
            
                for( ; i <s.size() ; i++ )
                cout<<9 ; 
            }
          }
          else
          {
               cout<<s1 ;
          }
        cout << endl ;
        k1++ ;
    }   
}
