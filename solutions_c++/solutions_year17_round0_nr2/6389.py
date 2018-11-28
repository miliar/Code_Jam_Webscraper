#include <bits/stdc++.h>
using namespace std ;

int main()
{
  ios_base::sync_with_stdio (false) ;
  int n, m, T, k ;
  long long int ans, temp, U ;
  vector<long long int>::iterator it ;
  cin>>T ;
  for(int tc=1 ; tc<=T ; tc++)
  {
     U=-1 ;
     ans=0 ;
     cin>> n >> m ;
     vector<vector<long long int> > dp(n, vector<long long int>(m)) ;
     vector< vector<long long int> > pie(n, vector<long long int>(m)) ;

     for(int i=0 ; i<n ; i++)
      {
       for(int j=0 ; j<m ; j++)
         cin>> pie[i][j] ;
       sort(pie[i].begin(), pie[i].end()) ;
      }
     for(int i=0 ; i<n ; i++)
      {
      	for(int j=0 ; j<m ; j++)
          dp[i][j]=pie[i][j] + (2*j + 1) ;
        if(U<dp[i][0]) U=dp[i][0] ;
      }

     for(int i=0 ; i<n ; i++)
     {
       it=lower_bound(dp[i].begin(), dp[i].end(), U+1) ;
       dp[i].erase(it, dp[i].end()) ;
     }

     for(int i=0 ; i<n-1 ; i++)
     {
       k=dp[i].size() ;
       while(k>1)
       {
         for(int j=i+1 ; j<n ; j++)
         {
           if(dp[j][0]>=dp[i][1])
           {
             temp= dp[i][1] ;
             it=dp[j].begin() ;
             dp[j].insert(it, temp) ;
             dp[i].erase(dp[i].begin()+1) ;
             k-- ;
             break ;
           }
           else if(j==n-1)
           {
           	 dp[i].erase(dp[i].begin()+1) ;
           	 k-- ;
           	 break ;
           }
         }
       }
     }
     for(int i=0 ; i<n ; i++)
       ans=ans+dp[i][0] ;

     cout<< "Case #" << tc << ": " << ans <<  endl ;
 }
 return 0 ;
 }
