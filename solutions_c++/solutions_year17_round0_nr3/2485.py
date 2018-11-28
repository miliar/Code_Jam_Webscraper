/*
ID: meetdi1
PROG: gift1
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>


using namespace std;

class data1
{
public:
	data1() : a(0), count(0) {}
	data1(long long aa, long long c):a(aa), count(c) {}
	long long a, count;
};
void breakin2(long long a, data1 &t1, data1 &t2)
{
	if (a == 0)
	{
		t1.a = 0;
		t2.a = 0;
		return;
	}
	if (a % 2 == 0)
	{
		t1.a = a / 2;
		t2.a = t1.a - 1;
	}
	else
	{
		t1.a = t2.a = a / 2;
	}
}

int main() {
	//ofstream fout("outp.txt");
	//ifstream fin("gift1.in");
	//ifstream fin("input.txt");
	int T;// N, Nn;

	cin >> T;
	for (int i = 0; i < T; i++)
	{
		long long N, K, minL =0, minR = 0;
		//int d[10] = { 0, }, t, m = 1;
		cin >> N;
		cin >> K;
		data1 da, db, tmp1, tmp2, tmp3, tmp4;
		if (N % 2 == 0)
		{
			da.a = N / 2;
			db.a = da.a - 1;
			da.count = db.count = 1;
		}
		else
		{
			db.a = da.a = N/2;
			da.count = db.count = 1;
		}
		//if (K <= ((N+1)/2))
		for (long long t = 1; t < K ;)
		{
			
			//
			if (da.a == 0 && db.a == 0)
			{
				break;
			}
			tmp1 = da;//a is bigger.
			tmp2 = da;
			breakin2(da.a, tmp1, tmp2);
			t+=da.count;
			if (t >= K)
			{
				da.a = tmp1.a; db.a = tmp2.a;
				break;
			}
			tmp3 = db;
			tmp4 = db;
			breakin2(db.a, tmp3, tmp4);
			t+=db.count;
			if (t >= K)
			{
				da.a = tmp3.a; db.a = tmp4.a;
				break;
			}
			//now merge count 
			if (tmp1.a == tmp3.a)
			{
				tmp1.count += tmp3.count;
				tmp3.a = -1;
			}
			if (tmp1.a == tmp4.a)
			{
				tmp1.count += tmp4.count;
				tmp4.a = -1;
			}
			if (tmp1.a == tmp2.a)
			{
				//now fill temp 2 with tmp3 or tmp4 which is valid. 
				if (tmp3.a != -1)
				{
					tmp1.count += tmp2.count;
					tmp2 = tmp3;
					tmp3.a = -1;
				}
				else if (tmp4.a != -1)
				{
					tmp1.count += tmp2.count;
					tmp2 = tmp4;
					tmp4.a = -1;
				}
			}
		
			if (tmp2.a == tmp3.a)
				{
					tmp2.count += tmp3.count;
					tmp3.a = -1;
				}

			if (tmp2.a == tmp4.a)
				{
					tmp2.count += tmp4.count;
					tmp4.a = -1;
				}
			
			//assign two variables
			da = tmp1;
			db = tmp2;

		}
	//	if (K > ((N + 1) / 2))
		{
	//		fout << "Case #" << i + 1 << ": " << 0 << " " << 0 << endl;
		}
	//	else
		{
			if (da.a > db.a)
				cout << "Case #" << i + 1 << ": " << da.a << " " << db.a << endl;
			else
				cout << "Case #" << i + 1 << ": " << db.a << " " << da.a << endl;
		}
		
	}
	return 0;
}