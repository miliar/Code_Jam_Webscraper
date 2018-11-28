#include <bits/stdc++.h>
using namespace std;

#define   f(i,n) 			for(int i=0;i<(n);i++)
#define   ff(i,n)           for(int i=1;i<=(n);i++)
#define   m0(X) 			memset((X), 0, sizeof((X)))
#define   m1(X) 			memset((X), -1, sizeof((X)))
#define   pb(x) 			push_back(x)
#define   mx 				9999999999999
#define   ay                100005
#define   rt                return 0
#define   sr(x,n)           sort(x+1,x+n+1)
#define   sv(v)             sort(v.begin(),v.end())
#define   fs                first
#define   sc                second
typedef long long ll;
typedef unsigned long long ull;

const double pi = acos(-1.0);
const int mod = 1000 * 1000 * 1000 + 7;
const ll inf = 1e18;

void rd(int &x){scanf("%d",&x);}
void rd(ll &x){scanf("%lld",&x);}
void rd(double &x){scanf("%lf",&x);}
void rd(int &x,int &y){scanf("%d%d",&x,&y);}
void rd(ll &x,ll &y){scanf("%lld%lld",&x,&y);}

void rd(int &x,int &y,int &z){scanf("%d%d%d",&x,&y,&z);}
void rd(ll &x,ll &y,ll &z){scanf("%lld%lld%lld",&x,&y,&z);}

void rd(double &x,double &y){scanf("%lf%lf",&x,&y);}
void rd(double &x,double &y,double &z){scanf("%lf%lf%lf",&x,&y,&z);}
void rd(char *s){scanf("%s",s);}
void rd(char &s){scanf("%c",&s);}
void rd(string &s){getline(cin,s);}
 
void pf(int x) {printf("%d\n",x);}
void pf(int x,int y) {printf("%d %d\n",x,y);}
void pf(ll x) {printf("%lld\n",x);}
void pf(char x) {printf("%c\n",x);}
void pf(char *x) {printf("%s\n",x);}
void pf(string x) {cout<<x<<endl;}
int p=1,ara[12000];map<string,ll>mp;
void bfs(string s,ll a ){
	mp[s]=p++;
	ara[mp[s]]=0;
	queue<string>q;
	q.push(s);
	while(!q.empty()){
		string s1=q.front();
		q.pop();
		for(int i=0;i<=s1.size()-a;i++){
			string s5=s1;
			for(int j=i;j<i+a;j++){
			if(s1[j]=='+')s5[j]='-';
			else s5[j]='+';
		}
		if(mp[s5]==0){
			
			mp[s5]=p++;
			ara[mp[s5]]=ara[mp[s1]]+1;
			q.push(s5);
		}
		}
		
		
	}
	
	
	
}
ll a,b,c=1,d,e,f,g,h,l,m,n,q,r,s,t,u,v,w,x,y,z;
int main()
{
	ofstream out;
	out.open("file.txt");
	cin>>t;
	while(t--){
		mp.clear();
		m1(ara);
		string s;cin>>s;
		cin>>n;
		//mp[s]=1;
	//	ara[mp[s]]=0;
		bfs(s,n);
		m=s.size();
		string s2;
		ff(i,m)s2+='+';
		if(mp[s2]==0)out<<"Case #"<<c++<<": impossible\n";
		else out<<"Case #"<<c++<<": "<<ara[mp[s2]]<<"\n";
		
		
		
	}
}
