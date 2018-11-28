#include<fstream>
#include<iomanip>
#include<vector>

using namespace std;

int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	int t;
	fin>>t;
	for(int ca=1; ca<=t; ca++)
	{
		long long int D;
		int n;
		fin>>D>>n;
		vector<long long int>k(n);
		vector<int>s(n);
		for(int i=0; i<n; i++)
			fin>>k[i]>>s[i];
		double time=(double)(D-k[n-1])/s[n-1];
		for(int i=n-2; i>=0; i--)
		{
			double curtime= (double)(D-k[i])/s[i];
			if(curtime>=time)
				time=curtime;
		}
		double ans=(double)D/time;
		fout<<"Case #"<<ca<<": ";
		fout.setf(ios::fixed);
		fout<<setprecision(6)<<ans<<"\n";
	}
}