#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;



int main()
{
	int T;
	int D, N, K, S;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		cin>>D>>N;
		vector<double> t;
		for(int j=0;j<N;j++)
		{
			cin>>K>>S;
			t.push_back((D-K)*1.0/S);
		}
		sort(t.begin(),t.end());
		double slowest = t.back();
		double speed = D*1.0/slowest;
		printf("Case #%d: %0.6f\n",i+1,speed);
	}
	return 0;
}

