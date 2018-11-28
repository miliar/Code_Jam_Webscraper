#include<bits/stdc++.h>
using namespace std;
int main()
{
 int t,nt=1;
 cin>>t;

 while(t--)
 {
  long long int n,k,l,r,i,j,temp;
  cin>>n>>k;
  vector<long long int>v;
  v.push_back(n);
  make_heap(v.begin(),v.end());
  for(i=0LL;i < k-1LL;i++)
    {
      j= v.front();
      pop_heap(v.begin(),v.end());
      v.pop_back();
      if( j%2LL == 0LL)
      {   
          v.push_back( j/2LL );
          push_heap(v.begin(),v.end());
          v.push_back( (j/2LL) - 1LL);
          push_heap(v.begin(),v.end());
      }
      else
        {
          v.push_back( j/2LL );
          push_heap(v.begin(),v.end());
          v.push_back( j/2LL );
          push_heap(v.begin(),v.end());
        }

    }   
     j= v.front();
     if(j%2LL == 0LL)
      {
         l= (j/2LL);
         r=(j/2LL)-1LL;
        if( l < r)
          {  temp=l;l=r; r=temp; }
      } 
      else
         { l= j/2LL ; r= j/2LL   ;}
    cout<<"Case #"<<nt<<": "<<l<<" "<<r<<endl;
     nt++;
 }  
 return 0;
}