#include<iostream>
#include<math.h>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;
int main()
{
	freopen("C-small-1-attempt3.in","r",stdin);
    freopen("submit.out","w",stdout);
	int l;
	cin>>l;
	for(int i1=0;i1<l;i1++)
	{
	int n;
	cin>>n;
	int k;
	cin>>k;
	vector<int> v;
	v.push_back(n);
	int a,b;
	for(int i=1;i<k;i++)
	{
		int k1=v.back();
		//cout<<"first "<<k1<<endl;
		if(k1%2==0)
		{
			v.pop_back();
			v.push_back(k1/2);
			v.push_back(k1/2-1);	
					
		}
		else
		{
			v.pop_back();
			v.push_back((k1-1)/2);
			v.push_back((k1-1)/2);
			
		}
	sort(v.begin(),v.end());
	}
	//cout<<"size is "<<v.size()<<endl;
	int k1=v.back();
	//cout<<"k1 is "<<k1<<endl;
	if(k1%2==0 && k1!=0)
		{
			a=k1/2;
			b=k1/2-1;		
		}
		else
		{
			a=(k1-1)/2;
			b=(k1-1)/2;
		}
	cout<<"Case #"<<i1+1<<": "<<a<<" "<<b<<endl;
	v.clear();
   }
	return 0;
}
