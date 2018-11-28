#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <stdio.h>

using namespace std;
struct horse
{
	int d;
	int s;
};

bool cmp(horse *a, horse *b)
{
	if (a->d > b->d)
		return true;
	return false;
}

int main()
{
	int T;
	int D, N;
	int k, S;
	int i, j;
	vector <horse *> vec;
	double tm, maxspeed;
	double global_tm;

	cin>>T;
	for(i=1; i<=T; i++)
	{
		cin>>D>>N;

		//cout<<"\n";
		//cout<<"D = "<<D<<" and N = "<<N<<"\n";
		vec.clear();
		for(j=0; j<N; j++)
		{
			cin>>k>>S;
			horse *h = new horse();
			h->d = k;
			h->s = S;

			vec.push_back(h);
		}

		//for(j=0; j<vec.size(); j++)
		//	cout<<vec[j]->d<<" "<<vec[j]->s<<"\n";

		sort(vec.begin(), vec.end(), cmp);
		//for(j=0; j<vec.size(); j++)
		//	cout<<vec[j]->d<<" "<<vec[j]->s<<"\n";

		if (N == 1)
		{
			//cout<<"Final horse at d = "<<vec[0]->d<<" and s = "<<vec[0]->s<<"\n";
			tm = (D-(vec[0]->d)) / (double)(vec[0]->s);
			maxspeed = D/tm;
		}
		else
		{
			int k1, k2;
			double t1, t2;
			double x;
			int sp;

			global_tm = 0;
			k1 = vec.size()-1;
			k2 = vec.size()-2;
			while(true)
			{
				t1 = (D - (vec[k1]->d)) / (double)(vec[k1]->s);
				t2 = (D - (vec[k2]->d)) / (double)(vec[k2]->s);

				//cout<<"curren t1 = "<<t1<<" and t2 = "<<t2<<"\n";
				if ( t1 > t2 )
				{
					tm = t1 + global_tm;;
					maxspeed = D/tm;
					break;
				}

				x = (vec[k2]->s) * ( ( (vec[k2]->d) - (vec[k1]->d) )  / ( (double) (vec[k1]->s) - (vec[k2]->s) ) );
				global_tm = x / vec[k2]->s;
				//cout<<"global_tm = "<<global_tm<<"\n";

				//cout<<"so they will meet at x = "<<x<<"\n";
				x = x + (vec[k2]->d);
				sp = vec[k2]->s;
				//cout<<"new d = "<<x<<" and new s = "<<sp<<"\n";

				vec.pop_back();

				//cout<<"vec.size() now = "<<vec.size()<<"\n";

				vec[vec.size()-1]->d = x;
				vec[vec.size()-1]->s = sp;

				if (vec.size() == 1)
				{
					//cout<<"Final horse at d = "<<vec[0]->d<<" and s = "<<vec[0]->s<<"\n";
					tm = (D-(vec[0]->d)) / (double)(vec[0]->s);
					//cout<<std::fixed;
					//cout<<std::setprecision(6);
					//cout<<"tm = "<<tm<<"\n";
					tm = tm + global_tm;
					maxspeed = ((double)D)/tm;
					//cout<<std::fixed;
					//cout<<std::setprecision(10);
					//cout<<"maxspeed = "<<(D/tm)<<"\n";
					break;
				}
			
				k1 = vec.size()-1;
				k2 = vec.size()-2;	
			}
		}

		cout<<"Case #"<<i<<": ";
		//cout<<std::fixed;
		//cout<<std::setprecision(12);
		//cout<<maxspeed<<"\n";
		printf("%0.18lf\n",maxspeed);
	}

	return 0;
}
