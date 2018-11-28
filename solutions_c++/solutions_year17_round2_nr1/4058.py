/*
ID: meet2dinesh
PROG: 
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
//#include <stdio.h>
#include <iomanip>

using namespace std;
int intialD[1001];
int speed[1001];

int main() {
	//FILE* fp1 = freopen("outp.txt", "w", stdout);
	//FILE* fp2 = freopen("outp.txt", "r", stdin);
	
	//ofstream fout("outp.txt");
	
	//ifstream fin("gift1.in");
	
	
	//ifstream fin("input.txt");
	int T;// N, Nn;

	cin >> T;
	
	for (int i = 0; i < T; i++)
	{
		int N; 
		long double D;
		long double time = 0, tt, max_t = 0, t_d;
		cin >> D >> N;
		for (int i = 0; i < N; i++)
		{
			cin >> intialD[i] >> speed[i];
		}
		tt = (D - intialD[0]) / speed[0];

		for (int i = 1; i < N; i++)
		{
			t_d = tt*speed[i]+intialD[i];
			if (D > t_d)
			{
				tt = tt+((D - t_d) / speed[i]);

			}
		}
		t_d = D / tt;
		cout << "Case #" << i + 1 <<":"<<" "<< std::fixed<< setprecision(6) << t_d << endl;
		//std::setprecision(3);
		//cout << setfill('0') << setw(4)
		
	}

	return 0;
}