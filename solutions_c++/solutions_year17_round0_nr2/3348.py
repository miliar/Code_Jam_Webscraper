#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <deque>
using namespace std;

string fname = "B";

int main()
{
	string ifname = fname + ".in";
	string ofname = fname + ".out";
	ifstream f;
	ofstream of;
	of.open(ofname);
	f.open(ifname);
	int t;
	f >> t;
	for (int tt=0;tt<t;++tt){
		long long n;
		f >> n;
		if (n < 10) 
		{
			of << "Case #" << tt+1 << ": " << n << "\n";
			continue;
		}
		deque<int> v;
		while (n > 0)
		{
			v.push_front(n%10);
			n/=10;
		}
		for (int i=0;i<v.size()-1;++i){
			if (v[i] > v[i+1])
			{
				for (int j=i+1;j<v.size();++j)
				{
					v[j] = 9;
				}
				do {
					--v[i];
					--i;
					if (i < 0) break;
					if (v[i] > v[i+1])
						v[i+1] = 9;
					else break;
				}		
				while (i >= 0);
				break;
			}
		}
		while (true)
		{
			if (v.front() == 0)
				v.pop_front();
			else
				break;
		}
		long long ret = 0;
		for (int i=0; i < v.size();++i)
		{
			ret *= 10;
			ret += v[i];
		}
		of << "Case #" << tt+1 << ": " << ret;
		of << "\n";
	}

	f.close();
	of.close();
}