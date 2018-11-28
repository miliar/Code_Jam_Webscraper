
#include <bits/stdc++.h>

#define REP(i, a) for( int i = 0; i < a; i++ )
#define RFOR(i,x,y) for(int i = x; i>= y; i--)
#define FOR(i,x,y) for (int i = x; i < y; i++)
#define ITFOR(it,A) for(typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define VE vector <int>
#define mset(A,x) memset(A, x, sizeof A)
#define PB push_back
#define ones(x) __builtin_popcount(x)
#define cua(x) (x)*(x)
#define debug(x) cout <<#x << " = " << x << endl
#define adebug(x,n) cout <<#x<<endl; REP(i,n)cout<<x[i]<<char(i+1==n?10:32)
#define mdebug(x,m,n) cout <<#x<<endl; REP(i,m)REP(j,n)cout<<x[i][j]<<char(j+1==n?10:32)
#define LSOne(S) (S&(-S))

using namespace std;

#define ll long long
#define lli long long int
#define PI acos(-1.0)
#define ii pair<int,int>
#define inf_ll (((1LL<<62)-1)<<1)+1
#define inf_i (1<<30)-1

int main(){
/*
   freopen("B-large.in", "r", stdin);
   freopen("out.txt", "w", stdout);
*/
	int n;
	string cad;
	scanf("%d",&n);
	cin.ignore();
	REP(t,n)
	{
		getline(cin,cad);
		if(cad.length()==1)
		{
			printf("Case #%d: %s\n",t+1,cad.c_str());
			continue;
		}
		int idx=-1;
		REP(i,cad.length()-1)
		{
			if(cad[i]>cad[i+1])
			{
				idx=i+1;
				cad[i]--;
				break;
			}
		}
		if(idx!=-1)
		{
			string sol="";
			int temp=idx-1;
			RFOR(i,temp,1)
			{
				if(cad[i-1]>cad[i])
				{
					cad[i-1]--;
					idx=i;
				}
			}
			REP(i,idx)
				sol+=cad[i];
			FOR(i,idx,cad.length())
				sol+="9";
			lli resp;
			sscanf(sol.c_str(),"%lld",&resp);
			printf("Case #%d: %lld\n",t+1,resp);
		}
		else
		{
		    lli resp;
			sscanf(cad.c_str(),"%lld",&resp);
			printf("Case #%d: %lld\n",t+1,resp);
		}
	}

/*
    fclose(stdin);
    fclose(stdout);
*/

    return 0;
}

