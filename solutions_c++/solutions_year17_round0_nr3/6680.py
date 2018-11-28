#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <set>
using namespace std;

int main(int argc, char* argv[])
{
   int t;
   cin>>t;
   for (int p = 0; p < t; p++)
   {
   	int n,ss;
   	cin>>n>>ss;
   	multiset<long long> s;
   	
   	s.insert(n);
   	for (int i = 0; i < ss - 1; i++)
   	{
   		long long tmp = *(--s.end());
   		s.erase(--s.end());
   		s.insert(tmp / 2);
   		if (tmp % 2 == 0) 
   		{
   			s.insert(tmp/2 - 1);
   			
   		}	
   		else
   		{
   			s.insert(tmp / 2);
   		}
   	}
   	long long tmp = *(--s.end());
   	if (tmp % 2 == 0)
   	{
   		cout<<"Case #"<<p + 1<<": "<<tmp / 2<<" "<<tmp / 2 - 1<<endl; 
   	}
   	else
   	{
   		cout<<"Case #"<<p + 1<<": "<<tmp / 2<<" "<<tmp / 2<<endl; 
   	}
	/*set < pair<int, int> > s;
	set < pair<int, int> >::iterator st;
	pair<int, int> pa;
	s.insert(make_pair(n,0));
	
	for (int i = 0; i < ss - 1; i++)
	{
		pa = *(--s.end());
		s.erase(--s.end());
		pa.second *= -1;
		//s.insert(make_pair(pa.first, pa.second % 2 == 0 ? pa.second / 2 - 1 : pa.second / 2));
		s.insert(make_pair(pa.first % 2 == 0 ? pa.first / 2 - 1 : pa.first / 2,-pa.second));
		s.insert(make_pair( pa.first / 2, -(1 + pa.second + pa.first % 2 == 0 ? pa.first / 2 - 1 : pa.first / 2)));
		
	}
	pa = *(--s.end());
	cout<<"Case #"<<p + 1<<": "<<max(pa.first % 2 == 0 ? pa.first / 2 - 1 : pa.first / 2,pa.first / 2)<<" "<<max(min(pa.first % 2 == 0 ? pa.first / 2 - 1 : pa.first / 2,pa.first / 2),0)<<endl;
	*/
	/*for(auto a : s)
	{
		cout<<a.first<<" "<<a.second<<endl;
	}*/

   }   
   return 0;
}
