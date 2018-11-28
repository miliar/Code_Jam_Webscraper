#include <iostream>
#include <utility>
#include <algorithm>
#include <cstdlib>
#include <map>
#define ii pair<int,int>
#define ll long long
using namespace std;


int N,K;



ii ans()
{
	map<int,int> s;
	s[N]=1;
	for(int i=0;i<K-1;i++)
	{
		int k = (s.rbegin())->first;
		s[k]--;
		if(s[k]==0)s.erase(k);
		int r1 = (k-1)/2;
		int r2 = k-1-r1;
		//cerr<<r1<<" "<<r2<<endl;
		if(s.find(r1)==s.end())s[r1]=0;s[r1]++;
		if(s.find(r2)==s.end())s[r2]=0;s[r2]++;
		//cerr<<s[r1]<<" "<<s[r2]<<endl;
	}
	int k = (s.rbegin())->first;
	int ls = (k-1)/2 , rs = k-ls-1;
	return ii(max(ls,rs),min(ls,rs));
}





int main()
{
	freopen ("C-small-2-attempt0.in","r",stdin);
	//freopen ("in.txt","r",stdin);
	freopen ("out.txt","w",stdout);
	int tc;
	cin>>tc;
	for(int i=1;i<=tc;i++)
	{
		cerr<<"Case #"<<i<<"...\n";
		cin>>N>>K;
		ii x = ans();
		cout<<"Case #"<<i<<": "<<x.first<<" "<<x.second<<endl;
	}
}