#include <fstream>
#include <vector>
#include <iomanip>

using namespace std;

double min_time(int u, int v, int e, int s, const vector<vector<int>> &map, const vector<int> &edge, const vector<int> &speed){
    if(u==v) return 0;
    if(e>=edge[u] && s>=speed[u])
        return static_cast<double>(map[u][u+1])/s + min_time(u+1, v, e-map[u][u+1], s, map, edge, speed);

    if(edge[u]>=e && speed[u]>=s)
        return static_cast<double>(map[u][u+1])/speed[u] + min_time(u+1, v, edge[u]-map[u][u+1], speed[u], map, edge, speed);

    double x = 1e12;
    if(e>=map[u][u+1])
        x = static_cast<double>(map[u][u+1])/s + min_time(u+1, v, e-map[u][u+1], s, map, edge, speed);
    double y = 1e12;
    if(edge[u]>=map[u][u+1])
        y = static_cast<double>(map[u][u+1])/speed[u] + min_time(u+1, v, edge[u]-map[u][u+1], speed[u], map, edge, speed);

    return min(x, y);
}

int main() {
    ifstream infile("C-small-attempt0.in");
    ofstream outfile("C-small-attempt0.out");

    int T;
    infile>>T;
    for(int t=1;t<=T;++t){
        int n, q;
        infile>>n>>q;
        vector<int> e(n+1, 0);
        vector<int> s(n+1, 0);
        for(int i=1;i<=n;++i){
            infile>>e[i]>>s[i];
        }

        vector<vector<int>> d(n+1, vector<int>(n+1, 0));

        for(int i=1;i<=n;++i){
            for(int j=1;j<=n;++j){
                infile>>d[i][j];
            }
        }
        outfile<<"Case #"<<t<<": ";
        for(int qi=0;qi<q;++qi){
            int u, v;
            infile>>u>>v;
            outfile<<setprecision(16)<<min_time(u, v, e[u], s[u], d, e, s)<<' ';
        }
        outfile<<endl;
    }

    infile.close();
    outfile.close();
    return 0;
}