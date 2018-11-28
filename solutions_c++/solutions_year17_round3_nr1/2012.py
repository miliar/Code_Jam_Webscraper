#include <iostream>
#include <algorithm>
#include <vector>
#include <bitset>
#define PI 3.14159265358979323846
using namespace std;
int main()
{
	int t;
	cin>>t;
	
	for(int tc=1;tc<=t;tc++)
	{
		int n,k;
		cin>>n>>k;

		vector<bitset<16>>bits;
		for(int a=1;a<1024;a++)
		{
			bits.push_back(a);
			if(bits[bits.size()-1].count()!=k)
				bits.pop_back();
		}


		int l=bits.size();
		vector<vector<float>>data;
		for(int a=0;a<n;a++)
		{
			vector<float>temp(2,0.0);
			cin>>temp[0]>>temp[1];
			data.push_back(temp);
		}

		sort(data.rbegin(),data.rend());
		vector<float>comp;
		for(int a=0;a<l;a++)
		{
			float pro=0;
			bool flag=true;
			for(int b=0;b<=10&& b<n ;b++)
			{

				if(bits[a][b])
				{
					pro+=(2*data[b][1]*data[b][0]);
					if (flag)
					{
						pro+=(data[b][0]*data[b][0]);
						flag=false;
					}
				}
			}
			comp.push_back(pro);
		}
		long double ans=*max_element(comp.begin(),comp.end());
		printf("Case #%d: %.9Lf\n",tc,ans*PI);
	}
	return 0;
}