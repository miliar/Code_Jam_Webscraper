#include <iostream>
#include <math.h>
#include <vector>
#include <set>
#include <fstream>
#include <map>
#include <deque>
#include <string>
using namespace std;
#define fori(v) for(int i=0; i<v; i++)
#define forj(v) for(int j=0; j<v; j++)
#define fork(v) for(int k=0; k<v; k++)
#define forl(v) for(int l=0; l<v; l++)
#define forz(v) for(int z=0; z<v; z++)
#define mp(a,b) make_pair(a,b)
#define ff first
#define ss second
#define lli long long int
#define MAX 100001
int main()
{
	ifstream input;
	ofstream output;
	input.open("input.txt");
	output.open("output.txt");
	int t;
	input>>t;
	forl(t)
	{
		lli n,k;
		input>>n>>k;
		map<lli,lli> xamisi;
		xamisi.insert(mp(n,1));
		lli say1,say2;
		lli sum = 0;
		while(1)
		{
			map<lli,lli> :: iterator bir = xamisi.begin();
			map<lli,lli> :: iterator it = xamisi.end();
			--it;
			lli check = (*it).ff;
			lli dene = (*it).ss;
			sum+=dene;
			int qaa1 = check/2, qaa2 =  (check-1)/2;
			if(sum>=k)
			{
				say1 = qaa1;
				say2 = qaa2;
				break;
			}
			xamisi.erase(it);
		    it = xamisi.find(qaa1);
		    lli pox1 = dene;
			if(it!=xamisi.end())
			{
				pox1 += (*it).ss;
				xamisi.erase(it);
			}
			xamisi.insert(mp(qaa1,pox1));
			//
			if(check!=2)
			{
				it = xamisi.find(qaa2);
				if(it!=xamisi.end())
				{
					dene += (*it).ss;
					xamisi.erase(it);
				}
				xamisi.insert(mp(qaa2,dene));
			}
		}
		output<<"Case #"<<l+1<<": "<<say1<<" "<<say2<<"\n";
	}
}
