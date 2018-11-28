#include<bits/stdc++.h>

#define pii pair<int,int>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define pf push_front
#define pb2 pop_back
#define pf2 pop_front
#define line printf("\n")
#define pq priority_queue
#define rep(k,i,j) for(int k = (int)i;k<(int)j;k++)
#define repd(k,i,j) for(int k = (int)i;k>=(int)j;k--)
#define ll long long

using namespace std;

double EPS = 1e-9;
int INF = 1e9+7;;
long long INFLL = 1e17;
double pi = acos(-1);
int dirx[8] = {-1,0,0,1,-1,-1,1,1};
int diry[8] = {0,1,-1,0,-1,1,-1,1};

inline void OPEN (string s) {
  freopen ((s + ".in").c_str (), "r", stdin);
  freopen ((s + ".out").c_str (), "w", stdout);
}

//end of template

string s;
int t;

void fix_zero(string &a){
	string b = a;
	a = "";
	int cnt = 1;
	rep(k,0,b.size()){
		if(b[k]!='0')cnt = 0;
		if(!cnt)a += b[k];
	}
	
	if(a.size()==0)a = "0";
}

ll to_ll(string a){
	ll x =0 ;
	
	rep(k,0,a.size())x = x*10 + a[k]-'0';
	return x;
}
int main(){
	cin>>t;
	
	rep(tt,1,t+1){
		cin>>s;
		printf("Case #%d: ",tt);
		
		string ret = s;
		int last = 0;
		rep(k,0,s.size()){
			repd(i,9,last){
				rep(j,k,ret.size())ret[j] = i + '0';
				if(to_ll(ret)<=to_ll(s)){last = i;break;}
			}
		}
		
		fix_zero(ret);
		cout<<ret<<endl;
	}
	return 0;
}
