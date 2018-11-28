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

void func(int s)
{
  int len , i ;
  len= str.size() ; 
  str[s] = str[s] -1 ;
  loop(i,s+1,len)
  {
    str[i] = (char)(57) ;
  }
}

int main() 
{
  int t , i ; 
  cin>>t ; 
  loop(i,0,t)
  {
    cin>>str ;
    int j , len=str.size() ;
    for(j=(len-1);j>=1;j--)
    {
      if((int)str[j-1]>(int)str[j])
        {
          func(j-1) ;
        }
    }

    int k ;
    loop(k,0,str.size())
    {
      if(str[k]!='0')
        break ;
    }
    cout<<"Case #"<<(i+1)<<": " ;
    loop(j,k,str.size())
    {
     cout<<str[j]; 
    }
    cout<<endl ;
  }
  return 0 ;
}