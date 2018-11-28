#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;
FILE *in, *out;
struct horseinfo
{
	int k;
	int s;
	double mergetime;//앞에 있는 느린 말에 합류하는 시간, 합류하지 않는다면 도착하는 시간
};
void CalculateMerge(vector<horseinfo> &horse,int d,int n);
double CheckOptimalSpeed(vector<horseinfo> &horse,int d,int n);
bool sortbyk(horseinfo a, horseinfo b) { return a.k < b.k; }
int main()
{
	in = fopen("input.txt", "r");
	out = fopen("output.txt", "w");
	int cy;
	int d, n;
	double minspeed;
	fscanf(in, "%d", &cy);
	for (int i = 1; i <= cy; i++)
	{
		fscanf(in, "%d %d", &d, &n);
		vector<horseinfo> horse(n + 1);
		for (int j = 1; j <= n; j++)
		{
			int i1, i2;
			fscanf(in,"%d %d", &i1, &i2);
			horse[j].k = i1;
			horse[j].s = i2;
		}
		sort(horse.begin() + 1, horse.end(), sortbyk);
		CalculateMerge(horse, d, n);
		minspeed = CheckOptimalSpeed(horse, d, n);
		fprintf(out, "Case #%d: %lf\n", i, minspeed);
	}
	fclose(in);
	fclose(out);
}
void CalculateMerge(vector<horseinfo> &horse, int d,int n)
{
	int pos=1;//각 말이 가장 먼저 합류하게 되는 말의 번호.
	int t1, t2;
	double tmin = 1000000000;
	for (int i = 1; i <= n; i++)
	{
		for (int j = i + 1; j <= n; j++)
		{
			if (horse[i].s > horse[j].s)
			{
				t1 = (d - horse[i].k) / horse[i].s;
				t2 = (d - horse[j].k) / horse[j].s;
				if (t1 >= (horse[j].k - horse[i].k) / (horse[i].s - horse[j].s) || t2 >= (horse[j].k - horse[i].k) / (horse[i].s - horse[j].s))
				{
					if (tmin >= (horse[j].k - horse[i].k) / (horse[i].s - horse[j].s))
					{
						pos = j;
						tmin = (horse[j].k - horse[i].k) / (horse[i].s - horse[j].s);
					}
				}
			}
		}
		if (horse[i].k + tmin * horse[pos].s > d)
		{
			horse[i].mergetime = (d - horse[i].k) / (double)horse[i].s;
		}
		else
			horse[i].mergetime = (horse[pos].k - horse[i].k) / (double)(horse[i].s - horse[pos].s);
	}
	horse[n].mergetime = (d - horse[n].k) /(double)horse[n].s;
}
double CheckOptimalSpeed(vector<horseinfo> &horse, int d, int n)
{
	double minspeed = 0;
	double immin;
	for (int i = 1; i <= n; i++)
	{
		if (horse[i].mergetime == (d - horse[i].k) / (double)horse[i].s)
		{
			immin = horse[i].k / (double)horse[i].mergetime + horse[i].s;
			if (immin < minspeed || minspeed == 0)
				minspeed = immin;
		}

	}
	return minspeed;
}
