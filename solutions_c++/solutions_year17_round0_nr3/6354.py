#include<iostream>
#include<map>
using namespace std;
int main()
{
	long long int T;
	cin>>T;
	long long int totcase=T;
	while(T--)
	{
		long long int n,k,min,max;
		cin>>n;
		cin>>k;
		map<long long int,long long int> ma;
		map<long long int,long long int> ::reverse_iterator rit;
		ma[n]=1;
		while (k>0) {
		rit = ma.rbegin();
		long long int val = rit->first;
		long long int count = rit->second;
		ma.erase(ma.find(val));
		min = (val+1)/2 -1;
		max = val - (val+1)/2;
		ma[min]=ma[min]+count;
		ma[max]=ma[max]+count;
		k=k-count;
		}
		ma.clear();
	   cout<<"Case #"<<totcase-T<<": "<<max<<" "<<min<<"\n";
	}
}