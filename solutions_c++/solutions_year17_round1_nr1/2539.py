#include <bits/stdc++.h> 
#define vi vector<int> 
#define ii pair<int,int>
#define vii vector <ii> 
#define pb push_back 
#define mp make_pair
#define F first 
#define S second 
#define loop(A,B,C) for(A=B;A<C;A++) 
#define fio ios_base::sync_with_stdio(false) 
#define div 1000000007

using namespace std ; 

int main() 
{
   fio ;
   int t , i ;
   cin>>t ;
   loop(i , 0 , t)
   {
    int r , c , j , k  ;
    cin>>r>>c ;
    string temp ;
    vector <string> vect ; 
    loop(j , 0 , r)
    {
      cin>>temp ;
      vect.pb(temp) ;
    }
    int le  , ri ;
    loop(j , 0 , r)
    {
      loop(k , 0 , c)
      {
        if(vect[j][k]!='?')
        {
          char ch = vect[j][k]; 
          le = k-1 ; 
          while(le>=0)
          {
            if(vect[j][le]!='?')
              break ;
            if(vect[j][le]=='?')
             vect[j][le]=ch  ;
            le-- ; 
          } 
          ri = k+1 ;
          while(ri<c )
          {
            if(vect[j][ri]!='?')
              break ;
            if(vect[j][ri]=='?')
             vect[j][ri]=ch  ;
            ri++ ;
          }  
        }
      }
    } 
    loop(j , 0 , r-1)
    {
      loop(k , 0 , c)
      {
        if(vect[j+1][k]=='?')
          vect[j+1][k] = vect[j][k] ; 
      }
    }
    for(j=r-1;j>0;j--)
    {
      loop(k , 0 , c)
      {
        if(vect[j-1][k]=='?')
          vect[j-1][k] = vect[j][k] ; 
      }
    }
    cout<<"Case #"<<(i+1)<<":"<<endl ;
    loop(j , 0 , r)
    {
      cout<<vect[j]<<endl ;
    }
   }

  return 0 ;
}