#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <bitset> 
#include <queue>
#include<algorithm>

using namespace std;

bool comp (long double a, long double b)
{
	return (a>b);
}
void main()
{
//	ifstream f_in ("C-large-practice.in");
	ifstream f_in ("C-small-1.in");
	//ifstream f_in ("small_input.txt");
//	ifstream f_in ("test.in");
//	ofstream f_out("test.out");
ofstream f_out("C-small-1.out");
//	ofstream f_out("C-large-practice.out");
		int case_num;
		f_in >> case_num;
		string tstr;
		getline(f_in,tstr);

	for(int k = 1; k <= case_num; ++k)
	{
		if(k==7)
			cout <<endl;
		long double N,K;
		f_in>>N>>K;
		vector<long double> q;
		long double max = floor(N/2);
		long double min = N - floor(N/2) - 1;
		double cur = 0.5;

		if(N==K)
			f_out<<"Case #"<<k<<": "<<0<<" "<<0<<endl;
		else
		{
			q.push_back(max);
			q.push_back(min);
			sort(q.begin(), q.end(),comp);
			K-=1;
		
			while (K > 0)
			{
				if(K==1)
					cout<<endl;
				--K;
				cur = q.front();
				q.erase(q.begin());

				max = floor(cur/2);
				min = cur - floor(cur/2) - 1;

				q.push_back(max);
				q.push_back(min);
				sort(q.begin(), q.end(),comp);
			}
			f_out<<"Case #"<<k<<": "<<max<<" "<<min<<endl;
		}

	}
	f_in.close();
	f_out.close();
}