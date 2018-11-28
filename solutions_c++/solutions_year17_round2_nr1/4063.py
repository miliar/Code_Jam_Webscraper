#define _CodeJam

#ifdef _CodeJam

#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
using namespace std;

int main(){
	fstream flin, flout;
	flin.open("C:\\Users\\HamedA\\Downloads\\A-small-attempt0.in", ios::in);
	flout.open("C:\\Users\\HamedA\\Downloads\\A-small-attempt0.out", ios::out);
	istream& fin = flin; ostream& fout = flout;
	int t, t1;
	long long d, n;
	fin >> t;
	t1 = t;
	while (t--){
		fin >> d >> n;
		long long*hd = new long long[n];
		int* hs = new int[n];
		double *ht = new double[n];
		for (int i = 0; i < n; i++)
		{
			fin >> hd[i] >> hs[i];
			ht[i] = (double)(d-hd[i]) / hs[i];
		}

		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n - i - 1; j++)
			{
				if (hd[j] > hd[j + 1]){
					long long h = hd[i];
					hd[i] = hd[i + 1];
					hd[i + 1] = h;
					h = hs[i];
					hs[i] = hs[i + 1];
					hs[i + 1] = h;
					h = ht[i];
					ht[i] = ht[i + 1];
					ht[i + 1] = h;
				}
			}
		}

		for (int i = n-1; i > 0; i--)
		{
			if (ht[i] > ht[i - 1]) ht[i-1] = ht[i];
		}

		double v = d / (float)ht[0];
		fout << "Case #" << t1 - t << ": " << fixed << setprecision(6) << v << endl;
		delete[]hd;
		delete[]hs;
		delete[]ht;
	}
	return 0;
}

#endif