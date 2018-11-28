#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;
typedef long long LL;

int main() 
{
	int t;
	cin>>t;
	
	for(int i=1;i<=t;i++)
	{
	   LL num,k,n;
	   cin>>num>>k;
	   n=num;
	   vector<int> v;
	   LL ls,rs;
	   if(num==k)
	   {
	       ls=0;
	       rs=0;
	   }
	   else
	   {
	       for(int j=0;j<k;j++)
	       {
	           if(j>0)
	           {
	               n = *max_element(v.begin(),v.end());
	           }
	           if(n%2==0)
	           {
	               ls = n/2 -1;
	               rs = n/2;
	               v.push_back(ls);
	                v.push_back(rs);
	           }
	           else
	           {
	               ls = n/2;
	               rs = n/2;
	               v.push_back(ls);
	                v.push_back(rs);
	           }
	       }
	   }
	   
	   cout<<"Case #"<<i<<": ";
	   cout<<max(ls,rs)<<" "<<min(ls,rs)<<endl;
	   
	}
	return 0;
}
