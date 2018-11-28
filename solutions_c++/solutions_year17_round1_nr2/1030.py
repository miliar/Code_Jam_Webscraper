
#include <cstdlib>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>
#include <cstdio>
#include <sstream>
#include <stack>
#include <cmath>
#include <string.h>
#include <queue>
#include <set>
using namespace std;
 
typedef vector < string > vs;
typedef vector <int> vi;
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define deb(x) cout << #x << ": " << x << endl;
#define debv(x) for(int i = 0; i < (x).size(); i++) cout << x[i] << ' '; cout << endl;


bool range(int ing, int servings, int total)
{
    if( 10*ing >= total*servings*9 && 10*ing <= total*servings*11)
        return true;
    else 
        return false;
}

const int MAXN = 55;
int marked[MAXN][MAXN];
int N, P;
int package[MAXN][MAXN];
int dfs(int cn, int looking)
{
    if(cn == N) return 1;

    for(int idx = 0; idx < P; idx++)
    {
        if(marked[cn][idx]) continue;
        if(package[cn][idx] == looking)
        {
            if(dfs(cn+1,looking))
            {
                marked[cn][idx] = 1;
                return 1;
            }
        }
    }
    return 0;
}

int main()
{
    int T;
	cin >> T;

	for(int test_case = 1; test_case <= T; test_case++)
	{
        cin >> N >> P;
        int recipe[N];
        for(int i = 0; i < N; i++)
            cin >> recipe[i];

        memset(package,-1,sizeof(package));

        priority_queue<pair<int,int>, vector<pair<int,int> >, greater<pair<int,int> > > PQ;
        for(int i = 0; i < N; i++)
        {
            for(int j = 0; j < P; j++)
            {
                int temp;
                cin >> temp;

                int serv_low = (double)temp / (double)recipe[i] / 1.1;
                int serv_high = (double)temp/(double)recipe[i] / 0.9;
                if(!range(temp, serv_low, recipe[i]))
                    serv_low++;
                if(!range(temp,serv_high, recipe[i]))
                    serv_high--;
                if(serv_low > 0 && range(temp,serv_low-1, recipe[i]))
                    serv_low--;
                if(serv_high > 0 && range(temp,serv_high+1, recipe[i]))
                    serv_high++;

                //deb(serv_low);
                //deb(serv_high);
                if(serv_low <= 0 || serv_high <= 0) continue;
                if(serv_low <= serv_high)
                {
                    PQ.push(make_pair(serv_low,-(i+1)));
                    PQ.push(make_pair(serv_high,i+1));
                }
                
            }
        }
        int ret = 0;
        //deb(PQ.size());
        int counts[MAXN], next[MAXN];
        memset(counts,0,sizeof(counts));
        memset(next,0,sizeof(next));
        int total_covered = 0;
        while(!PQ.empty())
        {
            int sv = PQ.top().first, cn = PQ.top().second;
            PQ.pop();
            
            //deb(sv);
            //deb(cn);
            if(cn < 0)
            {
                cn = -(cn+1);
                if(counts[cn] == 0)
                {
                    total_covered++;
                }
                counts[cn]++;
                if(total_covered == N)
                {
                    total_covered = 0;
                    ret++;
                    for(int j = 0; j < N; j++)
                    {
                        counts[j]--;
                        next[j]++;
                        if(counts[j] > 0) total_covered++;
                    }
                }
            }
            else if(cn > 0)
            {
                cn--;
                if(next[cn] > 0)
                {
                    next[cn]--;
                    continue;
                }
                if(counts[cn] == 0) { deb(cn); deb(sv); }
                counts[cn]--;
                if(counts[cn] == 0) total_covered--;
            }
        }

        printf("Case #%d: %d\n", test_case, ret);
	}
	return 0;
}