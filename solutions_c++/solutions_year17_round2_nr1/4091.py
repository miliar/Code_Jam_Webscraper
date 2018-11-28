#include <bits/stdc++.h>
using namespace std;
#define trace(v) cout<<"   " << #v<<"  =   "<<v<<endl;
typedef pair<double , double > pdd;
pdd array[1000];
double desired[1000];
bool compare(const pdd &a ,const  pdd &b)
{
	if(a.first == b.first)
		return a.second > b.second;
	return a.first > b.first;
}

double Solve()
{
	double dist;
	int N;
	//scanf("%d",&N);
	cin>>dist>>N;
	for(int i=0;i<N;++i)
	{
		double a,b;
		cin>>a>>b;
		array[i].first = a;
		array[i].second = b;
	}

	sort(array , array+N );


	desired[N-1] = dist;

	for(int i=N-2;i>=0;--i)
	{
		double v1 = array[i].second;
		double v2 = array[i+1].second;
		if(v1 < v2)
		{
			desired[i] = desired[i+1];
		}
		else
		{
			double dist1 = array[i+1].first - array[i].first;
			double eff_v = v1 - v2;
			double time1 = dist1/eff_v;
		//	trace(eff_v);
		//	trace(time1);
			dist1 = v2*time1;
			desired[i] = min( array[i+1].first + dist1 , desired[i+1]);
		}
	}
//	for(int i=0;i<N;++i)
//		cout<<desired[i]<<" ";
	double time1 = 0.0;
	for(int i=N-2;i>=0;--i)
	{
		double dist1 = desired[i+1]-desired[i];// - array[i+1].second*time1;
	//	trace(dist1/array[i+1].second);
		if(dist > 0)
			time1 += dist1/array[i+1].second;
		//trace(time1);
		//time1 += ()/array[i+1].second;
	}
	double dist1 = desired[0] - array[0].first;//- array[0].second*time1;
	time1 += dist1/array[0].second;
	//trace(time1);

	//cout<<time1<<endl;

	return dist/time1;
}

int main()
{
	int T;
	cin>>T;
	for(int i=1;i<=T;++i)
	{
		double K = Solve();
		printf("Case #%d: %0.6llf\n",i,K);
	}
	return 0;
}