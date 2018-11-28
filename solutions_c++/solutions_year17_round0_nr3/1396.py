#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

void solve(long long n, long long k, int c, ofstream& out)
{
    out<<"Case #"<<c<<": ";
	map<long long, long long> mp;
	mp[n]=1;
	for (long long i=0; i<k;)
	{
	    map<long long, long long>::iterator it=(--mp.end());
		long long t=it->first;
		long long h=t/2;
		long long h1=t&1?h:h-1;
		if (it->second>=k-i) {
			out<<h<<" "<<h1<<"\n";
			return;
		}
		else {
			mp[h]+=it->second;
			mp[h1]+=it->second;
			i+=it->second;
			mp.erase(it);
		}
	}
}

int main()
{
    ifstream in("C-large.in");
	ofstream out("c_output.txt");
    int t;
	in>>t;
	int i=1;
	while (t--)
	{
	    long long n, k;
		in>>n>>k;
		solve(n, k, i, out);
		++i;
	}
	return 0;
}