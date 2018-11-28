#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("output.txt", "w", stdout);
	ifstream fin;
	fin.open ("input.txt");
	
	int t;
	fin>>t;
	for(int mcase=1;mcase<=t;mcase++)
	{
		double d;
		int n;
		fin>>d>>n;
		double max_time = 0;
		for(int i=0;i<n;i++)
		{
			double pos,speed;
			fin>>pos>>speed;
			double time = (d-pos)/speed;
			if(time>max_time)
				max_time = time;
		}
		cout<<"Case #"<<mcase<<": ";
		cout << fixed << setprecision(6);
		cout << d/max_time << endl;
	}
}
