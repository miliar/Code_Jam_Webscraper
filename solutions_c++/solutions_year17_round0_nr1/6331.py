#include <bits/stdc++.h> 
#define vi vector<int> 
#define ii pair<int,int>
#define vii vector <ii> 
#define pb push_back 
#define mp make_pair
#define F first 
#define S second 
#define loop(A,B,C) for(A=B;A<C;A++) 
#define div 1000000007

using namespace std ; 
string str ; 
int k  ;

void func(int j)
{
  int i ;
  loop(i , j , j+k)
  {
    if(str[i]=='-')
      str[i]='+' ; 
    else
      str[i]='-' ;
  }
}

bool check()
{
  int l = str.size() , j ; 
  loop(j , 0 , l)
  {
    if(str[j]=='-')
      return false ;
  }
  return true ;
}

int main() 
{
  int t , i ; 
  cin>>t ; 
  loop(i,0,t)
  {

    int l , j , count=0 ;
    cin>>str ;
    cin>>k ;
    l = str.size() ;
    loop(j , 0 , l-k+1 )
    {
      if(str[j]=='-')
      {
        func(j) ; 
        count++ ;
      }
      // cout<<str<<endl ;
    }
    if(check())
    cout<<"Case #"<<(i+1)<<": "<<count<<endl ;
    else
    cout<<"Case #"<<(i+1)<<": IMPOSSIBLE"<<endl ;
  }
  return 0 ;
}