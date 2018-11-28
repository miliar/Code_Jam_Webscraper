#include<bits/stdc++.h>

#define s(a) scanf("%d",&a)
#define ss(a) scanf("%s",a)

#define MP           make_pair
#define PB           push_back
#define REP(i, n)    for(int i = 0; i < n; i++)
#define INC(i, a, b) for(int i = a; i <= b; i++)
#define DEC(i, a, b) for(int i = a; i >= b; i--)
#define CLEAR(a)     memset(a, 0, sizeof a)

using namespace std;

typedef long long          LL;
typedef unsigned long long ULL;
typedef vector<int>        VI;
typedef pair<int, int>     II;
typedef vector<II>         VII;

const int N = 1005;
int R[N];
int Q[N][N];
int lb[N][N];
int ub[N][N];
int ind[N];
int r[N];
bool check(int sc, int n, int p){
	for(int i=0;i<n;i++){
		if(ind[i]==p)
			return false;
		for(int j=ind[i];j<p;j++){
			if(lb[i][j]<=sc && ub[i][j]>=sc)
				break;
			if(ub[i][j]<sc || j==p-1)
				return false;
		}
	}
	return true;
}
bool update(int sc, int n, int p){
	for(int i=0;i<n;i++){
		for(int j=ind[i];j<p;j++){
			if(lb[i][j]<=sc && ub[i][j]>=sc){
				ind[i] = j+1;
				break;
			}
			if(j==p-1)
				return false;
		}
	}
	return true;
}
int solve(){
	set<int> st;
	set<int>::iterator it;
	VI cands;
	int n,p, ret = 0;
	s(n);s(p);
	REP(i,n)
		s(r[i]);
	REP(i,n){
		REP(j,p)
			s(Q[i][j]);
		sort(Q[i], Q[i]+p, std::greater<int>());
		REP(j,p){
			lb[i][j] = ceil(Q[i][j]/1.1/r[i]);
			ub[i][j] = (Q[i][j]/0.9/r[i]);
			//cout<<Q[i][j]<<" "<<lb[i][j]<<" "<<ub[i][j]<<endl;
			if(lb[i][j]<=ub[i][j])
				for(int k=lb[i][j];k<=ub[i][j];k++)
					st.insert(k);
		}
	}
	for(it=st.begin();it!=st.end();++it){
		cands.PB(*it);
	}
	reverse(cands.begin(),cands.end());
	CLEAR(ind);
	for(int j=0;j<cands.size();j++){
		int c = cands[j];
		//cout<<"check "<<c<<endl;
		while(check(c,n,p)){
				update(c,n,p);
				ret += 1;
			}
	}
	/*for(int ind1 = 0;ind1<p;ind1++){
		int f=lb[0][ind1], l = ub[0][ind1], m;
		if(l<f)
			continue;
		//cout<<"LB = "<<f<<" UB = "<<l<<endl;
		/*while(f<l){
			m = (f+l+1)/2;
			if(check(m,n,p))
				f = m;
			else 
				l = m-1;
		}
		if(check(f,n,p)){
			update(f,n,p);
			ret += 1;
		}*/
		/*for(int m=f;m<=l;m++){
			if(check(m,n,p)){
				update(f,n,p);
				ret += 1;
				break;
			}
		}
	}*/
	return ret;
}
int main()
{	
	int t;
	s(t);
	REP(tt,t){
		cout<<"Case #"<<tt+1<<": "<<solve()<<endl;
	}
    return 0;
}
