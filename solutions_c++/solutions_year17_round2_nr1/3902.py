#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define DEBUG 0 

int main() {
	int t;
	cin >> t;
	for (int i=0; i<t; i++)
	{
		double speed=0;
		double dest;
		int horses;
		cin >> dest >> horses;
		vector<pair<double,double> > horse_vec;
		for (int j=0; j<horses; j++)
		{
			double pos,speed;
			cin >> pos >> speed;
			pair<double,double> entry(pos,speed);
			horse_vec.push_back(entry);
		}
		double max_hours=0;
		for (int j=0; j<horses; j++)
		{
			double horse_pos=horse_vec[j].first;
			double horse_speed=horse_vec[j].second;
			double horse_hours=(dest-horse_pos)/horse_speed;
			max_hours=max(max_hours,horse_hours);
		}

		speed=dest/max_hours;

		printf ("Case #%d: %.6lf\n",i+1,speed);
	}
}
