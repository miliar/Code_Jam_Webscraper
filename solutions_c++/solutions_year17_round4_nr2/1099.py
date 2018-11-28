#include <bits/stdc++.h>
using namespace std;
typedef long long				ll;
typedef pair<int,int >			pii;
#define V						vector
#define SYNC					ios_base::sync_with_stdio(0);cin.tie(0);
#define rep(i,b)				for(int i=0;i<b;i++)
#define repn(i,n)				for(int i=1;i<=n;i++)
#define ALL(x)					(x).begin(),(x).end()
#define fi						first
#define se						second
#define pb						push_back
#define dzx						cerr<<"here";
const ll MOD=1e9+7,INF=9e18;
const int inf=2e8;
/* cent π */
int fre[2][1010];
int fno[2][2];
bool g[1010][1010];
V<int> m1;
V<int> m2;
int N,M;
// A DFS based recursive function that returns true if a
// matching for vertex u is possible
bool bpm(int u, bool seen[], int matchR[])
{
    // Try every job one by one
    for (int v = 0; v < N; v++)
    {
        // If applicant u is interested in job v and v is
        // not visited
        if (g[u][v] && !seen[v])
        {
            seen[v] = true; // Mark v as visited
 
            // If job 'v' is not assigned to an applicant OR
            // previously assigned applicant for job v (which is matchR[v]) 
            // has an alternate job available. 
            // Since v is marked as visited in the above line, matchR[v] 
            // in the following recursive call will not get job 'v' again
            if ((matchR[v] < 0) || bpm(matchR[v], seen, matchR))
            {
                matchR[v] = u;
                return true;
            }
        }
    }
    return false;
}
// Returns maximum number of matching from M to N
int maxBPM()
{
    // An array to keep track of the applicants assigned to
    // jobs. The value of matchR[i] is the applicant number
    // assigned to job i, the value -1 indicates nobody is
    // assigned.
    int matchR[N];
 
    // Initially all jobs are available
    memset(matchR, -1, sizeof(matchR));
 
    int result = 0; // Count of jobs assigned to applicants
    for (int u = 0; u < M; u++)
    {
        // Mark all jobs as not seen for next applicant.
        bool seen[N];
        memset(seen, 0, sizeof(seen));
 
        // Find if the applicant 'u' can get a job
        if (bpm(u, seen, matchR))
            result++;
    }
    return result;
}

int main(){SYNC
	int T;
	cin>>T;
	repn(tc,T){
		N=0;
		M=0;
		m1.clear();
		m2.clear();
		memset(g,0,sizeof g);
		memset(fre,0,sizeof fre);
		memset(fno,0,sizeof fno);
		cout<<"Case #"<<tc<<": ";
		int n,c,m,p,b;
		cin>>n>>c>>m;
		int y=0,z=0;
		rep(i,m){
			cin>>p;
			cin>>b;
			fre[b-1][p-1]++;
			b--;
			p--;
			if(p){
				if(b){
					N++;
					m1.pb(p);
				}
				else{		
					M++;
					m2.pb(p);
				}
			}
			if(p)
				p=1;
			fno[b][p]++;
			
		}
		int t1=min(fno[0][0],fno[1][1]);
		int t2=min(fno[0][1],fno[1][0]);
		fno[0][0]-=t1;
		fno[1][1]-=t1;
		fno[1][0]-=t2;
		fno[0][1]-=t2;
		y+=t1;
		y+=t2;
		y+=fno[0][0];
		y+=fno[1][0];
		y+=max(fno[0][1],fno[1][1]);
		int temp=min(fno[0][1],fno[1][1]);
		cout<<y<<" ";
		M=m1.size();
		N=m2.size();
		for(int i=0;i<m1.size();i++){
			for(int j=0;j<m2.size();j++){
				if(m1[i]!=m2[j]){
					g[i][j]=1;
				}
			}
		}
		int ul=maxBPM();
		if(ul>=temp){
			cout<<0;
		}
		else{
			z=temp-ul;
			cout<<z;
		}
		cout<<"\n";
	}
	return 0;
}