#include<iostream>
#include<string>
#include<list>
#include<vector>
#include<algorithm>
#include <fstream>
using namespace std;

ifstream in;
ofstream out;


bool myfunction(int i, int j) { return (i>j); }

int main()
{
	in.open("C-small-2-attempt4.in");
	out.open("out.txt");
	int casses;
	in >> casses;

	for (int i = 0; i < casses; i++)
	{
		long long n;
		long long k;
		
		in >> n;
		in >> k;
		

		vector<long long> lsrs;
		long long ls;
		long long rs;
	/*	lsrs.push_back(n);
		for (long long j = 0; j < k-1; j++)
		{
			
			ls = (lsrs[0] - 1) / 2;
			rs = (lsrs[0] - 1) - ls;
			lsrs.push_back(ls>rs?ls:rs);
			lsrs.push_back(ls>rs ? rs : ls);
			lsrs.erase(lsrs.begin());
		}
		ls = (lsrs[0] - 1) / 2;
		rs = (lsrs[0] - 1) - ls;
		*/
		long long tmp = (long long)log2l(k);
		long long last=n / (pow(2,tmp));
		cout << "Case# " << i + 1<<" " << n << " " << k << endl;
		if (k - pow(2, tmp) > (n - last* pow(2, tmp)) )
		{
			last--;
		}
	
		ls = (last - 1) / 2;
		rs = (last - 1) - ls;

		out <<"Case #"<<i+1<< ": " <<((ls>rs)?ls:rs)<<" "<<((ls>rs)?rs:ls)<< endl;

	}
	cout << "unesi" << log2(262144)<< endl;
	cin >> casses;

	return 0;
}