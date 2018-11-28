
// Example program
#include <bits/stdc++.h>
using namespace std;
#define mp(a,b) make_pair(a,b)
#define ff first
#define ss second
#define fori(v) for(int i=0; i<v; i++)
#define forj(v) for(int j=0; j<v; j++)
#define fork(v) for(int k=0; k<v; k++)
#define forl(v) for(int l=0; l<v; l++)
#define lli long long int
// #define cin in
// #define cout out
int MAX = pow(10,2);
int inf = pow(10,9);
int modulo = pow(10,9)+7;
double eps = 1e-7;
int main()
{
	ifstream in;
	ofstream out;
	in.open("input.txt");
	out.open("output.txt");
	int t;
	in>>t;
	fork(t)
	{
		int n,p;
		in>>n>>p;
		int qaliqlar[4] = { };
		fori(n)
		{
			int eded;
			in>>eded;
			qaliqlar[eded%p]++;
		}
		int cavab;
		if(p==2)
		{
			cavab = qaliqlar[0] + qaliqlar[1]/2 + qaliqlar[1]%2;
			
		}
		else if(p==3)
		{ 
			int say = min(qaliqlar[1],qaliqlar[2]);
			int maxx = max(qaliqlar[1],qaliqlar[2]);
			maxx-=say;
			
			cavab = qaliqlar[0] + say + maxx/3  ;
			if(maxx%3>0)
			++cavab;
			if(cavab>n)
			cavab = n;
		}
		else
		{
			int say = min(qaliqlar[1],qaliqlar[3]);
			int maxx = max(qaliqlar[1],qaliqlar[3]);
			maxx-=say;
			
			cavab = qaliqlar[0] + qaliqlar[2]/2 + say + maxx/4;
			if((maxx%4>0) || (qaliqlar[2]%2==1) )
			++cavab;
			if(cavab>n)
			cavab = n;
		}
		out<<"Case #"<<k+1<<": "<<cavab<<"\n";
	}
}
