#include<iostream>
#include<vector>
#include<fstream>
#include<algorithm>
#define all(c) c.begin(),c.end()
using namespace std;
int main()
{
    ifstream fin("A-large.in");
    ofstream fout("oflarge.out");
	ios_base::sync_with_stdio(false);
	int t;
	fin>>t;
	for(int tc=1;tc<=t;tc++)
	{
	    string x;
	    fin>>x;
	    int k;
	    fin>>k;
		vector<char> pm(x.size()+1);
		for(int i=1;i<=x.size();i++)
            pm[i]=x[i-1];
        int count(0);
        int i,j;
        for(i=1;i<pm.size()-k+1;i++)
        {
            if(pm[i]=='-')
            {
                for(j=i;j<=(i+k-1);j++)
                    if(pm[j] == '+') pm[j] = '-';
                    else pm[j] = '+';
                count++;
            }
        }
        if(find(pm.begin()+1,pm.end(),'-')!=pm.end())
            fout<<"Case #"<<tc<<": "<<"IMPOSSIBLE"<<endl;
        else
            fout<<"Case #"<<tc<<": "<<count<<endl;
	}
	fin.close();
    fout.close();
	return 0;
}
