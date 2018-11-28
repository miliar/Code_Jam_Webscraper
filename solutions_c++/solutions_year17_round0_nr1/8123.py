#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T ;
    cin>>T ;
    
   for(int t = 1 ; t <= T ; t++){
        int k ;
        string s ;
        cin>>s>>k ;
        
        bool flag = true ;
        int ans = 0 ;
        
        for(int i = 0 ; i < s.length() ; i++){
            if(s[i] == '-') { flag = false ; break ; }
        }
        
        if(!flag){
            for(int i = 0 ; i < s.length() ; ){
                if(s[i] == '+') i++ ;
                
                else if(s.length() - i < k){
                    ans = -1 ;
                    break ;
                }
                
                else {
                    int j = i ;
                    for(j = i ; j < i+k ; j++){
                        if(s[j] == '-') s[j] = '+' ;
                        else s[j] = '-' ;
                     }   
                    ans++ ;
                }
                
            }
        }
        
        if(ans == -1) cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl ;
        else cout<<"Case #"<<t<<": "<<ans<<endl ;
    }
    
    return 0;
}

