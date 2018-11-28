#include <iostream>
#include <fstream>
#include<conio.h>
#include<stdio.h>
#include<iomanip>
#include<string>
#include<ctype.h>
#include<math.h>
#include<map>
#include<vector>
#include<assert.h>
#include<algorithm>

using namespace std;

#define FOR(k,a,b) for(int k=a; k <(b); ++k)
#define MIN(x,y) ((x)<(y)?(x):(y))
#define MAX(x,y) ((x)>(y)?(x):(y))

ifstream fin;
ofstream fout;
bool sortinrev(const pair<double, double> &a,
	const pair<double, double> &b)
{
	return (a.first > b.first);
}
void _main(int t)
{
	int n,k;
	int arr[1000][2];
		fin >> n>>k;
		FOR(i, 0, n)
		{
			fin>>arr[i][0];
			fin >> arr[i][1];
		}
		double max,pi= 3.14159265358979323846;
		int c = 0;
		max = pi*pow(arr[0][0], 2) + 2 * pi*arr[0][0] * arr[0][1];
		FOR(i, 1, n)
		{
			double temp= pi*pow(arr[i][0], 2) + 2 * pi*arr[i][0] * arr[i][1];
			if (max < temp)
			{
				max = temp;
				c = i;
			}
		}
	//fout << c << "K";
		if (k == 1)
		{
			fout << fixed << setprecision(9)<< max;
		}
		else
		{
			vector<pair<double, double>> p;
			FOR(i, 0, n)
			{
				p.push_back(make_pair(2 * pi*arr[i][0] * arr[i][1], pi*pow(arr[i][0], 2)));
			}
			sort(p.begin(),p.end(),sortinrev);
			//double temp= 2 * pi*arr[c][0] * arr[c][1],max1= pi*pow(arr[c][0], 2),tempmax=0;
			double temp = 0, max1 = 0, tempmax = 0;
			FOR(i, 0, k-1)
			{
				tempmax = p[0].second;
				temp +=p[0].first;
				p.erase(p.begin());
				//fout << p[i].second<<"k";
				max1 = MAX(max1, tempmax);
			}
			double max2 = 0,temp1=0;
			FOR(i, 0, p.size())
			{
				temp1 = 0;
				if (max1 < p[i].second)
					temp1 = p[i].second-max1;
				temp1 += p[i].first;
				max2 = MAX(max2, temp1);
			}
			fout << fixed << setprecision(9)<< temp+max1+max2;
			p.clear();

		}
}
int main()
{
	int t;
	fin.open("input.txt", ios::in);
	fout.open("output.txt", ios::out);
	fin >> t;
	for (int i = 1; i <= t; i++)
	{
		fout << "Case #" << i << ": ";
		_main(i);
		fout << "\n";
	}
	return 0;
}