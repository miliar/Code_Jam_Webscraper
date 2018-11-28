#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <functional>
#include <map>

using namespace std;

auto &out = cout;
auto &in = cin;

int main()
{
	/*
	ofstream out("out.txt");
	ifstream in("in.txt");
	*/
	int T;
	in >> T;
	for (int cn = 1; cn <= T; cn++)
	{
		long long int N, K;
		in >> N >> K;
		map<long long int, long long int, greater<long long int>> M;
		M[N] = 1;
		long long int A, B;
		long long int Key, Val;
		while (true)
		{
			Key = M.begin()->first;
			Val = M.begin()->second;
			K = K - Val;
			M[Key / 2 - 1 + (Key % 2)] += Val;
			M[Key / 2] += Val;
			M.erase(M.begin());
			if (K <= 0)
			{
				B = Key / 2;
				A = B - 1 + (Key % 2);
				break;
			}
		}
		out << "case #" << cn << ": " << B << " " << A << endl;

	}

}
