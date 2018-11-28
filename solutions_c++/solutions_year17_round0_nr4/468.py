#include <bits/stdc++.h>
#include <iomanip>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef pair<LL, LL> PLL;
typedef long double LD;
typedef pair<LD, LD> PLDLD;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)
#define CLR(a) memset((a), 0 ,sizeof(a))
#define ALL(a) a.begin(),a.end()

const double eps=1e-5;
const int INF=1e9;

int main()
{
    int dx[4]={-1,1,1,-1},dy[4]={-1,-1,1,1};
    int t;
    cin>>t;
    
    REP(tt,t)
    {

        int n,m;
        cin>>n>>m;
        vector<vector<int>> table(n,vector<int>(n));
        vector<vector<int>> xt(n,vector<int>(n));
        vector<vector<int>> pt(n,vector<int>(n));

		vector<int> searchSeq(n);
		if(n>1)
		{
			iota(searchSeq.begin()+2,searchSeq.end(), 1);
			searchSeq[1]=n-1;
		}
        vector<PII> ansxy;
        vector<char> ansc;

        auto drawxt=[&](int x,int y){
            REP(i,n)
			{
                if(i!=x)
                	xt[i][y]=1;
				if(i!=y)
					xt[x][i]=1;
            }
        };
        auto drawpt=[&](int x, int y){
            REP(i,4)
            {
                int k=1;
                while(1)
                {
                    int px=x+dx[i]*k,py=y+dy[i]*k;
                    if(!(0 <= px && px<n && 0<= py && py < n)) break;
                    pt[px][py]=1;
					k++;
                }
            }
        };

        REP(i,m)
        {
            char c;
            int x,y;
            cin>>c>>x>>y;
            x--;y--;
            table[x][y]=c=='o'?3:(c=='x'?2:1);
            if((table[x][y]&2)>0)
                drawxt(x,y);
            if((table[x][y]&1)>0)
                drawpt(x,y);
        }


        for(auto&& i:searchSeq)
        REP(j,n)
        {
            if(table[i][j]==2)
            {
                if(xt[i][j]==0&&pt[i][j]==0)
                {
                    table[i][j]=3;
					drawpt(i,j);
					drawxt(i,j);
                    ansc.push_back('o');
                    ansxy.push_back(PII(i,j));
                }
            }
            if(table[i][j]==1)
            {
                if(xt[i][j]==0&&pt[i][j]==0)
                {
                    table[i][j]=3;
					drawpt(i,j);
					drawxt(i,j);
                    ansc.push_back('o');
                    ansxy.push_back(PII(i,j));
                }
            }
        }

        for(auto&& i:searchSeq)
        REP(j,n)
        {
            if(table[i][j]==0)
            {
                if(pt[i][j]==0&&xt[i][j]==0)
                {
                    table[i][j]=3;
					drawpt(i,j);
					drawxt(i,j);
                    ansc.push_back('o');
                    ansxy.push_back(PII(i,j));
                }
				else if(pt[i][j]==0)
				{
					table[i][j]=1;
					drawpt(i,j);
                    ansc.push_back('+');
                    ansxy.push_back(PII(i,j));
				}
            }
        }

        for(auto&& i:searchSeq)
        REP(j,n)
        {
            if(table[i][j]==0)
            {
                if(pt[i][j]==0&&xt[i][j]==0)
                {
                    table[i][j]=3;
					drawpt(i,j);
					drawxt(i,j);
                    ansc.push_back('o');
                    ansxy.push_back(PII(i,j));
                }
				else if(xt[i][j]==0)
				{
					table[i][j]=2;
					drawxt(i,j);
                    ansc.push_back('x');
                    ansxy.push_back(PII(i,j));
				}
            }
        }


		int ans=0;
		REP(i,n)
        REP(j,n)
		{
			ans+=(table[i][j]+1)/2;
		}
		cout<<"Case #"<<tt+1<<": "<<ans<<" "<<ansc.size()<<endl;
		REP(i,ansc.size())
		{
			cout<<ansc[i]<<" "<<ansxy[i].first+1<<" "<<ansxy[i].second+1<<endl;
		}

    }
}

