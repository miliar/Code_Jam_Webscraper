#include<iostream>
#include<math.h>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;
int main()
{
	freopen("C-small-1-attempt0.in","r",stdin);
    freopen("submit.out","w",stdout);
	int test;
	cin>>test;
	for(int i1=0;i1<test;i1++)
	{
	int n,k;
	cin>>n;
	cin>>k;
	vector<int> s;
	s.push_back(n);
	int min,max;
	for(int i=1;i<k;i++)
	{
		int k1=s.back();
		if(k1%2==0)
		{
			s.pop_back();
			s.push_back(k1/2);
			s.push_back(k1/2-1);	
					
		}
		else
		{
			s.pop_back();
			s.push_back((k1-1)/2);
			s.push_back((k1-1)/2);
			
		}
	sort(s.begin(),s.end());
	}
	int k1=s.back();
	if(k1%2==0 && k1!=0)
		{
			min=k1/2;
			max=k1/2-1;		
		}
		else
		{
			min=(k1-1)/2;
			max=(k1-1)/2;
		}
	cout<<"Case #"<<i1+1<<": "<<min<<" "<<max<<endl;
	s.clear();
   }
	return 0;
}
