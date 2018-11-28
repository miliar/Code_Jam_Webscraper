#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T ;
    cin>>T ;
    
   for(int t = 1 ; t <= T ; t++){
        string n ;
        cin>>n ;
        
        //long long ans =
        
        //int i = 0 ; 
        
        bool tidy  = false ;
        
        while(!tidy){
            tidy = true ;
            for(int i  = 1 ; i < n.length() ; i++){
                
                if(n[i] - '0' < n[i-1] - '0') { 
                    
                    n[i-1] = ((n[i-1] - '0') - 1 ) + '0' ;
                    while(i < n.length()) n[i++] = '9' ;
                    tidy = false ; 
                }
            }
        }
        
        //long long ans = 0 ;
        int i =  0 ;
        while(n[i] == '0') i++ ;
        cout<<"Case #"<<t<<": ";
        
        for(i = i ; i < n.length() ; i++) cout<<n[i] ;
        cout<<endl ;
    }
    
    return 0;
}

