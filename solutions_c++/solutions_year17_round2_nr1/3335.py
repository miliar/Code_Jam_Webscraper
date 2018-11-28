#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <bitset> 
#include <queue>
#include<algorithm>

using namespace std;



void main()
{
//	ifstream f_in ("test.in");
//	ofstream f_out("test.out");

	//ifstream f_in ("A-small.in");
	//ofstream f_out("A-small.out");

	ifstream f_in ("A-large.in");
	ofstream f_out("A-large.out");
		int case_num;
		f_in >> case_num;
		string tstr;
		getline(f_in,tstr);

	for(int k = 1; k <= case_num; ++k)
	{
		/*if(k==48)
			cout<<endl;*/
		int D,N;
		int num;
		f_in>>D>>N;

		int *pos;
		pos = new int [N];

		int *vel;
		vel = new int [N];
		double *time;
		time = new double[N];
		bool *flag;
		flag = new bool[N];
		double *sum;
		sum = new double[N];

		for(int i = 0; i < N; ++i)
			f_in>>pos[i]>>vel[i];

		time[N-1] = ((double)(D-pos[N-1]))/vel[N-1];
		flag[N-1] = false;
		sum[N-1] = time[N-1];
		for(int i = N-2; i>=0; --i)
		{
			if(((double)(D-sum[i]))/vel[i] < time[i+1])
			{
				double t = (double)((pos[i+1] - pos[i]))/(vel[i] - vel[i+1]);
				if((t*vel[i]+pos[i])>(time[i+1]*vel[i+1]+pos[i+1]))
				{
					time[i] = time[i+1];
					flag[i] = true;	
					sum[i] = time[i]+time[i+1];
				} else {
					flag[i] = false;
					time[i] = t;
					sum[i] = time[i]+time[i+1];
				}
			}
			else
			{
				time[i] = ((double)(D-pos[i]))/vel[i];
				flag[i] = false;
				sum[i] = time[i];
			}
		}
		double max = 0;
		int max_i = -1;
		for(int i =0 ;i < N; ++i)
		if(max <sum[i])
		{
			max = sum[i];
			max_i = i;
		}
		double res = (double)D/(double)max;

		f_out.setf(ios::fixed);
		f_out<<"Case #"<<k<<": "<<setprecision(6)<<res<<endl;

		delete []pos;
		delete []vel;
		delete []flag;
		delete []time;
		delete []sum;
	}

	f_in.close();
	f_out.close();
}