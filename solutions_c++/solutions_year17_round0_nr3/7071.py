#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;
int main()
{
	int t;
	ifstream w("inps.in");
	ofstream r("outputs.txt");
	w>>t;
	int n[t],k[t];
	for(int i=0;i<t;i++)
	{
        w>>n[i]>>k[i];
	}
	for(int i=0;i<t;i++)
	{
	    int ls,rs;
	    vector<int> h;
	    h.push_back(n[i]);
	    for(int j=0;j<k[i];j++)
	    {
	      int l=h.size()-1;
	      ls=h[l]/2;
	      rs=(h[l]-1)/2;
	      h[l]=ls;
	      h.push_back(rs);
	      sort(h.begin(),h.end());
	    }
	    r<<"Case #"<<i+1<<": "<<max(ls,rs)<<" "<<min(ls,rs)<<endl;
	}return 0;
}
