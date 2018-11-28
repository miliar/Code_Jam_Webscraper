using namespace std;
#include <bits/stdc++.h>
#define rep(i,n) for(int i=0; i<(n); i++)
#define mem(x,val) memset((x),(val),sizeof(x));
#define rite(x) freopen(x,"w",stdout);
#define read(x) freopen(x,"r",stdin);
#define all(x) x.begin(),x.end()
#define sz(x) ((int)x.size())
#define sqr(x) ((x)*(x))
#define pb push_back
#define clr clear()
#define inf (1<<30)
#define ins insert
#define xx first
#define yy second
#define eps 1e-9
typedef long long i64;
typedef unsigned long long ui64;
typedef string st;
typedef vector<int> vi;
typedef vector<st> vs;
typedef map<int,int> mii;
typedef map<st,int> msi;
typedef set<int> si;
typedef set<st> ss;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
#define mx 0
int main() {
   	ios_base::sync_with_stdio(0);cin.tie(NULL);
   	//Solution
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t){

		string s = "";
		int k;
		char c = getchar();
		while(c!=' '){ 
			s+=c;
			c = getchar();
		}
		scanf("%d", &k);
		bitset<10010> bs;
		int len = s.length();
		for (int i = 0; i < len; ++i)
		{
			bs[i] = s[i]=='-'?0:1;
		}
		int res = 0;
		// for (int i = 1; i < len+4; ++i) cout << bs[i];
		// cout << endl;
		// cout << len-k+1 << endl;
		for (int i = 1; i < len-k+1; ++i)
		{
			if(bs[i]==0){
				for (int j = i; j < i+k; ++j) {bs[j]=~bs[j];}
				res++;
			}
		}

		
		// for (int i = 1; i < len; ++i) cout << bs[i];
		// cout << endl;
		bool fl = true;
		for (int i = 1; i < len; ++i)
		{
			if(bs[i]==0){
				fl = false;
			}
		}
		// for (int i = 1; i < len+4; ++i) cout << bs[i];
		// cout << endl;
		if(fl)	
			printf("Case #%d: %d\n",t, res);
		else
			printf("Case #%d: IMPOSSIBLE\n",t, res);
		
		
	}
   	
   	
   	return 0;
}


//g++-4.9 pancake.cpp -o pancake && ./pancake < pancake.in > pancake.txt