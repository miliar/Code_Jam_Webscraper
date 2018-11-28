#include<bits/stdc++.h>

#define REP(i,s,n) for(int (i)=s; (i)<(int)(n);(i)++)
#define RIT(it,c) for(__typeof(c.begin()) it = c.begin();it!=c.end();it++)
#define ALL(x) x.begin(), x.end()
#define SZ(x) (int)(x).size()
#define MSET(m,v) memset(m,v,sizeof(m))


using namespace std;


typedef long long LL;
typedef long double LD;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<LL> vL;
typedef vector<bool> vb;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    std::ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    freopen("A-large.in","r",stdin);
    freopen("output_large","w",stdout);
    int T;
    cin>>T;
    cerr<<T<<endl;
    for(int t=1;t<=T;++t){
        cout<<"Case #"<<t<<": ";
		LL D,N;
		cin>>D>>N;
		LD tm = 0;
		for(int i = 0; i<N;++i){
			LL K,S;
			cin>>K>>S;
			if(K>=D) continue;
			tm = max(tm,LD(D-K)/S);
		}
		LD ans = LD(D)/tm;
		cout << setprecision(18);
		cout <<ans<<endl;
		cerr <<ans<<endl;
    }
    return 0;
}


