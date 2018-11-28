#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <set>
#include <iomanip>

using namespace std;

void solve(int n, int *colors, int c, ofstream& out)
{
char cl[6]={'R', 'O', 'Y', 'G', 'B', 'V'};
    out<<"Case #"<<c<<": ";
	int mx=0, sum=0;

	for (int i=0; i<6; ++i) {
		if (mx<colors[i])
			mx=colors[i];
		sum+=colors[i];
	}
	if (mx>sum/2)
		out<<"IMPOSSIBLE\n";
	else
	{
	    int first, prev=-1;
	    int i=0;
		while (i<n)
		{
		    int ind=-1, ind0=-1, mx0;
			mx=0;
		    for (int j=0; j<6; ++j) {
				if (j!=prev && mx<=colors[j]) {
					mx0=mx;
					mx=colors[j];
					ind0 = ind;
					ind = j;
				}
			}
			int index;
			if (i==n-2 && mx==mx0 && ind0==first)
				index=ind0;
			else
				index=ind;
			
			out<<cl[index];
			--colors[index];
			if (i==0)
				first=index;
			prev=index;
			++i;
		}
		out<<"\n";
	}
}

int main()
{
    ifstream in("B-small-attempt0.in");
	ofstream out("output.txt");
    int t;
	in>>t;
	int i=1;
	while (t--)
	{
	    int n;
		in>>n;
		int colors[6];
		for (int i=0; i<6; ++i)
			in>>colors[i];
	    solve(n, colors, i, out);
		++i;
	}
	return 0;
}