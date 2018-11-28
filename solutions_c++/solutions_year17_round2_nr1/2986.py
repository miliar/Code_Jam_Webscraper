#include<iostream>
#include<vector>
#include<iomanip>
#include<fstream>
using namespace std;
int main()
{
	ifstream fin("A-large.doc",ios::in);
	ofstream fout("khan.txt",ios::out);
	long int t;
	char ch;
	fin>>t;
	fin.get(ch);
	long int w=1;
	while(t--)
	{
		long double d;
		long long int n;
		fin>>d>>n;
		 long double min=0;
		fin.get(ch);
		//vector<long long int>t;
		
		while(n--)
		{
			long double a,b;
			fin>>a>>b;
			fin.get(ch);
			long double l=d-a;
			long double m=l/b;
			if(m>min)
				min=m;
		}
		//cout<<"min"<<min<<endl;
		double x=double(d)/double(min);
		fout<< "Case #" << w << ": ";
		fout<<fixed<<setprecision(6)<<x;
		fout<<endl;
		w++;
	}
}