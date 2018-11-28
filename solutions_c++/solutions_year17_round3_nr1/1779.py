#include<fstream>
#include<vector>
#include<algorithm>
#include<cmath>
#include<iomanip>

using namespace std;

const double PI = 3.14159;

struct cake
{
	double r,h;
};

bool comp(cake a, cake b)
{
	if(a.r > b.r)
		return true;
	return false;
}

int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	int t;
	fin>>t;
	for(int ca=1; ca<=t; ca++)
	{
		int n,k;
		fin>>n>>k;
		vector<cake>cakearr(n);
		for(int i=0; i<n; i++)
		{
			fin>>cakearr[i].r>>cakearr[i].h;
		}
		sort(cakearr.begin(),cakearr.end(),comp);
		vector<vector<double>>dp(n,vector<double>(k+1,-1));
		vector<double>maxarr(k+1,-1);
		for(int i=0; i<n; i++)
		{
			double cr=cakearr[i].r;
			double ch=cakearr[i].h;
			dp[i][1]=(double)(2*PI*cr*ch) + (double)(PI*cr*cr);
			//fout<<(double)dp[i][1]<<"\n";
			/*if(maxarr[1] == -1 || maxarr[1]<dp[i][1])
			{
				maxarr[1]=dp[i][1];
			}*/
			for(int j=2; j<=min(i+1,k); j++)
			{
				dp[i][j] = maxarr[j-1] + (double)(2*PI*cr*ch);
			}
			for(int j=1; j<=min(i+1,k); j++)
			{
				if(maxarr[j]==-1 || maxarr[j]<dp[i][j])
				{
					maxarr[j]=dp[i][j];
				}
			}
		}
		fout.setf(ios::fixed);
		fout<<"Case #"<<ca<<": ";
		fout<<setprecision(6)<<maxarr[k]<<"\n";
	}
}