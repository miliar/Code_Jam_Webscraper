#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <set>
#include <iomanip>

using namespace std;

const double INF=1000000000000000;
std::vector<double> djextra(std::vector<std::vector<double> >& graph, int v1)
{
    int n=graph.size();
    std::vector<double> djx(n);
    for (int i=0; i<n; ++i)
        djx[i]=INF;
    std::vector<bool> used(n, false);
    
    std::set<std::pair<double, int> > st;
    std::pair<double, int> p=std::make_pair(0, v1);
    st.insert(p);
    djx[v1]=0;
    std::set<std::pair<double, int> >::iterator it;
    while (!st.empty())
    {
        it=st.begin();
        int v=it->second;
        st.erase(it);
        if (used[v]==false)
        {
            used[v]=true;
            for (int i=0; i<n; ++i)
            {
                if (graph[v][i]!=-1 && djx[i]>djx[v]+graph[v][i])
                {
                    djx[i]=djx[v]+graph[v][i];
                    st.insert(std::make_pair(djx[i], i));
                }
            }   
        }        
    }
    return djx;
}

void solve(int n, int q, vector<pair<double, double> >& horses, vector<vector<double> >& gr, vector<pair<int, int> >& queries, int c, ofstream& out)
{
    out<<"Case #"<<c<<": ";
	int mx=0, sum=0;
	vector<vector<double> > new_gr(n, vector<double>(n));
	for (int i=0; i<n; ++i) {
		std::vector<double> djx=djextra(gr, i);
		for (int j=0; j<n; ++j)
			new_gr[i][j]=djx[j]>horses[i].first?-1:djx[j]/horses[i].second;
	}

	for (int i=0; i<q; ++i) {
		std::vector<double> djx=djextra(new_gr, queries[i].first-1);
		out<<setprecision(8)<<fixed<<djx[queries[i].second-1]<<" ";
	}
	out<<"\n";
}

int main()
{
    ifstream in("C-large.in");
	ofstream out("output.txt");
    int t;
	in>>t;
	int i=1;
	while (t--)
	{
	    int n, q;
		in>>n>>q;
		vector<pair<double, double> > horses(n);
		for (int i=0; i<n; ++i)
			in>>horses[i].first>>horses[i].second;
		vector<vector<double> > gr(n, vector<double>(n));
		for (int i=0; i<n; ++i)
			for (int j=0; j<n; ++j)
				in>>gr[i][j];
		vector<pair<int, int> > queries(q);
		for (int i=0; i<q; ++i)
			in>>queries[i].first>>queries[i].second;
	    solve(n, q, horses, gr, queries, i, out);
		++i;
	}
	return 0;
}