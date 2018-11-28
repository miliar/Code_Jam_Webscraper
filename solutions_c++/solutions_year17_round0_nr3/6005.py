#include <iostream>
#include <string>
#include <fstream>
#include <math.h>
using namespace std;

int main()
{
	int T;
	unsigned long long K, N,a,b,num,tmp;
	
	string in;
	ifstream st("in.in");
	ofstream write;
	write.open("out.expect");
	//cin >> T;
	st >> T;
	for (int i = 1; i <= T; i++)
	{
		//cin >> N >> K;
		st >> N >> K;
		if (K == 1)
		{
			a = N / 2;
			if (N % 2 == 0)
				b = a - 1;
			else
				b = a;
		}
		else{
			num = (unsigned long long int)log2(K);
			num = pow(2, num);
			tmp = (N - K) / num;
			if (tmp % 2 == 0)
			{
				a = tmp / 2;
				b = a;
			}
			else
			{
				a = (tmp / 2) + 1;
				b = a - 1;
			}
		}
		cout << "Case #" << i << ": " << a << " " << b << endl;
		write << "Case #" << i << ": " << a << " " << b << endl;
	
	}
}