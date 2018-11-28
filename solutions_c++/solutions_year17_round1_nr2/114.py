#include <iostream>
#include <algorithm>
#include <string>
#include <fstream>
#include <vector>

using namespace std;
typedef long long ll;
typedef vector<ll> vi;
typedef vector<vi> vvi;
int main() {
	ofstream fout;
	ifstream fin;
	fout.open("output.txt");
	fin.open("B-large.in");
	ll t;
	fin >> t;
	for(ll h=0;h<t;h++)
	{
		ll n,p;
		fin >> n >> p;
		vi r(n);
		for(ll i=0;i<n;i++)
			fin >> r[i];
		vvi prices(n,vi(p));
		for(ll i=0;i<n;i++)
			for(ll j=0;j<p;j++)
				fin >> prices[i][j];
		for(ll i=0;i<n;i++)
			sort(prices[i].begin(),prices[i].end());
		vi pollers(n);
		ll num=1;
		ll res=0;
		bool finish=false;
		while(pollers[0]<p)
		{
			bool change=false;
			for(ll i=0;i<n;i++)
			{
				while(pollers[i]<p&&r[i]*num*9>prices[i][pollers[i]]*10)
				{
					pollers[i]++;
					change=true;
				}
				if(pollers[i]==p)
				{
					finish=true;
					break;
				}
				while(r[i]*num*11<prices[i][pollers[i]]*10)
				{
					if(r[i]*(num+1000)*11<prices[i][pollers[i]]*10)
						num+=1000;
					num++;
					change=true;
				}
			}
			if(finish)
				break;
			if(change)
				continue;
			res++;
			for(ll i=0;i<n;i++)
				pollers[i]++;
		}
		fout << "Case #" << h+1 << ": ";
		fout << res << endl;
	}
	fout.close();
	fin.close();
    return 0;
}
