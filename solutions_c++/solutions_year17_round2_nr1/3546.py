#include<iostream>
#include<algorithm>
#include<iomanip>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.txt","w",stdout);
	
	int test;
	cin>>test;
	
	int j = 1;
	while(test--)
	{
		int D, N;
		cin>>D>>N;
		
		double Arr[N];
		int K, S;
		for(int i=0;i<N;i++)
		{
			cin>>K>>S;
			Arr[i] = (D - K)/(double)S;
		}
		
		sort(Arr, Arr+N,  greater<double>());
		
		cout<<"Case #"<<j++<<": "<<std::fixed<<setprecision(6)<<D/Arr[0]<<endl;
		
	}
	
	return 0;
}
