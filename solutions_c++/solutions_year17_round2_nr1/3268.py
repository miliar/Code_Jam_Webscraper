#include<iostream>
#include<iomanip>
using namespace std;

int main()
{
	int T;
	cin >> T;
	int round=1;
	while(T-- > 0)
	{
	int D,N;
	cin >> D >> N;
	double dist[N], speed[N];
	for(int i=0; i<N; i++)
		cin >> dist[i] >> speed[i];
	double max=(D-dist[0])/speed[0];
	double t=0.0;
	for(int i=1; i<N; i++)
	{
		t = (D-dist[i])/speed[i];
		if(t > max)
			max = t;
	}
	double ans = D/max;
	if(max==0.0)
		ans = D;
	cout << setprecision(6) << fixed;

	cout<<"Case #"<<round<<": "<<ans<<"\n";
	round++;
	}
}
