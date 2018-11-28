#include<bits/stdc++.h>
using namespace std ;

int main()
{
    int t ;
    cin>>t ;
    int f=1 ;
    while(f<=t)
    {
        string s ;
        int k ;
        cin>>s ;
        cin>>k ;
        int len=s.size() ;
            len-- ;
            int i=0 ;
        for(i=0 ; i<=len ; i++){
            if(s[i]=='+'){
                continue ;
            }
            else{
                break ;
            }
        }
     //   cout<<"i"<<endl ;
        bool flag=true ;
        int ctr=0 ;
        for( ; i<=len ; i++)
        {
            if(s[i]=='-' && (i+k-1)<=len){
                    ctr++ ;
                for(int j=i ; j<=(i+k-1) ; j++){
                    if(s[j]=='+'){
                        s[j]='-' ;
                    }
                    else{
                        s[j]='+' ;
                    }
                }
            }
            else if(s[i]=='-'){
                    flag=false ;
                    break ;
            }
       //     cout<<s<<endl ;

        }
        if(flag==false){
            cout<<"Case #"<<f<<": IMPOSSIBLE"<<endl ;
        }
        else{
            cout<<"Case #"<<f<<": "<<ctr<<endl ;
        }
        f++ ;
    }
    return 0 ;
}
