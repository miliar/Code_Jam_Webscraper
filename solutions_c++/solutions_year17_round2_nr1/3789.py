#include <bits/stdc++.h>

using namespace std;

struct horse_s
{
	long double speed;
	long double d;
};

int cmp(horse_s a, horse_s b)
{
	return a.d > b.d;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int T;
	cin>>T;
	horse_s horse[1005];
	
	for(int i=1;i<=T;i++)
	{

		long double dest;
		int  n;
		cin>>dest>>n;


		for(int t=0;t<n;t++)
		{
			cin>> horse[t].d >> horse[t].speed;			
		}



		sort(horse,horse+n,cmp);

		long double min_s=1000000.0;
		long double min_d=0;

		long double max_hr=0.0;

		for(int t=0;t<n;t++)
		{
			long double hr;
			hr= (dest-horse[t].d)/horse[t].speed;

			max_hr=max(hr,max_hr);
			
		}

		cout<<"Case #"<<i<<": "<<fixed<<setprecision(6)<<dest/max_hr<<"\n";



	}
	return 0;
}