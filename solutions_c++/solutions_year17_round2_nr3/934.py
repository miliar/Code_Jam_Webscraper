#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<queue>

using namespace std;

struct node{
    int e,s;
    double t;
    int v;

    bool operator < (const node& n1) const
    {
	return (t > n1.t);
    }
}used[105];

vector<pair<int,int> > h;

priority_queue<node> pq;

int t,n,q;
int edges[105][105];
int u,v;

double sp(){
    while(!pq.empty()){
	node cn = pq.top();
	pq.pop();
	used[cn.v].e = cn.e;
	used[cn.v].s = cn.s;
	used[cn.v].v = 1;
	if(cn.v == v)
	    return cn.t;

	for(int i = 0 ; i < n; ++i)
	    if(edges[cn.v][i] != -1){
		if(cn.e >= edges[cn.v][i]){
		    node n1;
		    n1.e = cn.e - edges[cn.v][i];
		    n1.s = cn.s;
		    n1.t = cn.t + (double)edges[cn.v][i]/cn.s;
		    n1.v = i;
		    if(used[n1.v].v == 0 || (used[n1.v].e < n1.e || used[n1.v].s < n1.s))
			pq.push(n1);
		}
		if(h[cn.v].first >= edges[cn.v][i]){
		    node n2;
		    n2.e = h[cn.v].first - edges[cn.v][i];
		    n2.s = h[cn.v].second;
		    n2.t = cn.t + (double)edges[cn.v][i]/h[cn.v].second;
		    n2.v = i;
		    if(used[n2.v].v == 0 || (used[n2.v].e < n2.e || used[n2.v].s < n2.s))
			pq.push(n2);
		}
	    }
    }
}

void read_input(){
    cin >> t;
    cout.precision(10);
    for(int i = 0 ; i < t ; ++i){
	cin >> n >> q;
	int e,s;
	for(int j = 0 ; j < n; ++j){
	    cin >> e >> s;
	    h.push_back(make_pair(e,s));
	}
	for(int j = 0; j < n; ++j)
	    for(int k = 0 ; k < n; ++k)
		cin >> edges[j][k];

	cout << "Case #" << (i+1) << ": ";


	for(int j = 0 ; j < q; ++j){
	    cin >> u >> v;
	    --u; --v;

	    for(int k = 0 ; k < n; ++k)
		used[k].v = 0 ;
	    pq = priority_queue<node>();

	    node n1;
	    n1.e = n1.s = n1.t = 0;
	    n1.v = u ;

	    pq.push(n1);

	    cout << sp() << " ";
	}
	cout << endl;
	h.clear();
    }
}

void calc(){
}

int main(){
    read_input();
    calc();
    return 0;
}
