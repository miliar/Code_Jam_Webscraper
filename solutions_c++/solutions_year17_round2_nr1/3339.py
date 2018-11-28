/*###########################################################################
				CRUISE CONTROL
############################################################################*/
#include "bits/stdc++.h"
#define ll long long
#define lld long long int
#define ulld unsigned long long int
#define u_ unsigned
#define ui unsigned int
#define mod 1000000007
#define pi 3.14159265

using namespace std;

int main(int argc, char const *argv[])
{
	lld t;
	scanf("%lld",&t);
	int caseno = 1;
	while(t--){
		long K, D;
		cin>>D>>K;
		double hor[K], spd[K];
		//pair<double, double> pr[K];
		double rem[K], time[K];
		for (int i = 0; i < K; ++i)
		{
			//scanf("%Lf %Lf",&hor[i], &spd[i]);
			cin>>hor[i]>>spd[i];
			rem[i]=D-hor[i];
			time[i]=rem[i]/spd[i];
			//pr[i].make_pair();
		}
		//for (int i = 0; i < K; ++i)
		//{
		//	cout<<time[i]<<" ";
		//}
		//cout<<endl;
        sort(time, time+K);
        double ans=(double)D/time[K-1];

        printf("Case #%d: %0.6f\n",caseno, ans);
		caseno++;
	}

	return 0;
}
