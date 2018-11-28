#include<fstream>
#include<vector>
#include<climits>
#include<cmath>

using namespace std;

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
		vector<int>L(n+2);
		vector<int>R(n+2);
		vector<int>occ(n+2);
		for(int i=1; i<=n; i++)
		{
			L[i]=i-1;
			R[i]=(n+1)-(i+1);
			occ[i]=0;
		}
		for(int j=1; j<k; j++)
		{
			int curmin=INT_MIN, curmax=INT_MIN, pos=-1;
			for(int i=1; i<=n; i++)
			{
				if(occ[i]==1)
					continue;
				int thismin=min(L[i],R[i]);
				int thismax=max(L[i],R[i]);
				if(thismin > curmin)
				{
					curmin=thismin;
					curmax=thismax;
					pos=i;
				}
				else if(thismin==curmin && thismax>curmax)
				{
					curmin=thismin;
					curmax=thismax;
					pos=i;
				}
			}
			occ[pos]=1;
			for(int x=pos-1; x>=1 && occ[x]==0; x--)
				R[x]=pos-x-1;
			for(int x=pos+1; x<=n && occ[x]==0; x++)
				L[x]=x-pos-1;
		}
		int curmin=INT_MIN, curmax=INT_MIN, pos=-1;
		for(int i=1; i<=n; i++)
		{
			if(occ[i]==1)
				continue;
			int thismin=min(L[i],R[i]);
			int thismax=max(L[i],R[i]);
			if(thismin > curmin)
			{
				curmin=thismin;
				curmax=thismax;
				pos=i;
			}
			else if(thismin==curmin && thismax>curmax)
			{
				curmin=thismin;
				curmax=thismax;
				pos=i;
			}
		}
		fout<<"Case #"<<ca<<": "<<curmax<<" "<<curmin<<"\n";
	}
}