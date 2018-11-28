#include <bits/stdc++.h>
using namespace std;
int main()
{
	std::ios_base::sync_with_stdio(false);
  int t,l=1;
  pair<int,int> a[105];
  cin>>t;
  while(t--)
  {
  	int n,k,cnt=0,ls,rs,j;
  	multiset<int> s;
  	multiset<int>::iterator it; 
  	cin>>n>>k;
  	s.insert(n);
   	while(cnt<k-1)
  	{
  		
  		it=s.end();
  		it--;
  		j=*it;
  		
  		if(j%2==0)
  			{ls=j/2;rs=j/2-1;}
  		else
  			{ls=j/2;rs=j/2;}
  		s.erase(it);
  		s.insert(ls);
  		s.insert(rs);
  		cnt++;
  		
  	}
  	it=s.end();
  		it--;
  		j=*it;
  		
  		if(j%2==0)
  			{ls=j/2;rs=j/2-1;}
  		else
  			{ls=j/2;rs=j/2;}
  	if(rs<0)rs=0;
  	a[l].second=rs;
  	a[l].first=ls;
  	l++;
  	
  }
  for(int i=1;i<l;i++)
  {
  	cout<<"Case #"<<i<<": "<<a[i].first<<' '<<a[i].second<<endl;
  }
}

