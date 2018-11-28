#include <iostream>
#include <iomanip>
using namespace std;
double getAns(int *k,int *s,int d,int n)
{
	int ans=0;
	double max=0;
	int i=0;
	while(i<n)
	{
		double temp= (d-k[i])/((double)s[i]);
		if(temp>max)
			max=temp;
		i++;
	}
	//cout << max;
	return d/(double)max;
}
int main()
{
	std::cout << std::fixed << std::showpoint;
    std::cout << std::setprecision(6);
	int t;
	cin >> t;
	int i;
	for(i=0;i<t;i++)
	{
		int d,n;
		cin >> d;
		cin >> n;
		int j;
		int k[n];
		int s[n];
		for(j=0;j<n;j++)
		{
			cin >> k[j];
			cin >> s[j];
		}
		cout<<"Case #"<<(i+1)<<": "<< std::setprecision(6)<<getAns(k,s,d,n)<<"\n";
	}
	return 0;
}