#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <stdint.h>
#include <climits>
#include <algorithm>
using namespace std;
namespace maxflow
{
	/* O(N^2) memory is used for this one, be careful */
	/* cap[a][b] nonzero means there is an edge there */
	const int MAXV = 550;
	const int INF = INT_MAX;
	int cap[MAXV][MAXV];
	int flow[MAXV][MAXV];
	int pred[MAXV];
	int val[MAXV];
	int flow_size;

    void set_cap(int a, int b, int x) {
        cap[a][b] = x;
    }
    void clear(void) {
        memset(cap, 0, sizeof(cap));
    }
	//the output is visible in flow
	void find_maxflow(int N,int src,int sink)
	{
		flow_size = 0;
		memset(flow,0,sizeof(flow));
		while(1)
		{
			//remove labels
			memset(pred,-1,sizeof(pred));
			memset(val,-1,sizeof(val));
			//start with src
			pred[src] = -1;
			val[src] = INF;
			set<int> U;U.clear();
			U.insert(src);
			while(val[sink] == -1)
			{
				//check for done
				if(U.empty()){return;}
				int v = (*U.begin());U.erase(v);
				int delta = val[v];
				for(int i=0;i<N;++i)
				{
					if(val[i] != -1){continue;}
					if(cap[v][i] && flow[v][i] < cap[v][i])
					{
						pred[i] = v;
						val[i] = min(delta,cap[v][i]-flow[v][i]);
						U.insert(i);
					}
					if(cap[i][v] && flow[i][v]>0)
					{
						pred[i] = v;
						val[i] = min(delta,flow[i][v]);
						U.insert(i);
					}
				}
			}
			vector<int> w(1,sink);
			for(int t=0;w[t] != src;++t)
			{
				w.push_back(pred[w[t]]);
			}
			reverse(w.begin(),w.end());
			int delta = val[sink];
			flow_size += delta;
			for(int i=1;i<w.size();++i)
			{
				if(cap[w[i-1]][w[i]])
				{
					flow[w[i-1]][w[i]] += delta;
				}
				else
				{
					flow[w[i]][w[i-1]] -= delta;
				}
			}
		}
	}
};

const char *toout = ".x+o";
int main(int argc, char **argv) {
    int T;
    cin >> T;
    for(int cn=1;cn<=T;++cn) {
        int N,M;
        cin >> N >> M;
        maxflow::clear();
        vector<int> row_taken(N, 0);
        vector<int> col_taken(N, 0);
        vector<vector<int> > field(N, vector<int>(N, 0));
        int score = 0;
        const int SOURCE = 0;
        const int SINK = 1;
        const int ASTART=2;
        const int BSTART=2+2*N;
        const int NODES = BSTART + 2*N;
        for(int i=0;i+1<2*N;++i) {
            maxflow::set_cap(SOURCE, ASTART+i, 1);
            maxflow::set_cap(BSTART+i, SINK, 1);
        }
        for(int r=0;r<N;++r) {
            for(int c=0;c<N;++c) {
                int A = r-c+(N-1);
                int B = r+c;
                maxflow::set_cap(ASTART+A, BSTART+B, 1);
            }
        }
        for(int i=0;i<M;++i) {
            string s;
            int r;
            int c;
            cin >> s >> r >> c;
            --r;--c;
            bool is_x = false;
            bool is_p = false;
            switch(s[0]) {
                case 'x': {is_x = true;score += 1;}break;
                case '+': {is_p = true;score += 1;}break;
                case 'o': {is_p = is_x = true;score += 2;}break;
            }
            if(is_x) {
                field[r][c] |= 1;
                row_taken[r] = 1;
                col_taken[c] = 1;
            }
            if(is_p) {
                field[r][c] |= 2;
                int A = r-c+(N-1);
                int B = r+c;
                maxflow::set_cap(SOURCE, ASTART+A, 0);
                maxflow::set_cap(BSTART+B, SINK, 0);
            }
        }
        typedef map<pair<int,int>, int> MA;
        MA changes;
        //x's
        vector<int> row_miss;
        vector<int> col_miss;
        for(int i=0;i<N;++i) {
            if(!row_taken[i]){row_miss.push_back(i);}
            if(!col_taken[i]){col_miss.push_back(i);}
        }
        for(int i=0;i<row_miss.size();++i) {
            score += 1;
            changes[make_pair(row_miss[i], col_miss[i])] |= 1;
        }
        maxflow::find_maxflow(NODES, SOURCE, SINK);
        for(int r=0;r<N;++r) {
            for(int c=0;c<N;++c) {
                int A = r-c+(N-1);
                int B = r+c;
                if(maxflow::flow[ASTART+A][BSTART+B]) {
                    score += 1;
                    changes[make_pair(r,c)] |= 2;
                }
            }
        }
        vector<pair<pair<int,int>, char> > v;
        for(MA::const_iterator iter = changes.begin();iter != changes.end();++iter) {
            int r = iter->first.first;
            int c = iter->first.second;
            int dd = iter->second;
            int newd = (field[r][c] | dd);
            if(newd != field[r][c]) {
                v.push_back(make_pair(make_pair(r,c), toout[newd]));
            }
        }
        printf("Case #%d: %d %d\n", cn, score, (int)v.size());
        for(int i=0;i<v.size();++i) {
            printf("%c %d %d\n", v[i].second, v[i].first.first+1, v[i].first.second+1);
        }
    }
    return 0;
}
