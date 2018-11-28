#define dsfi(x) int x; scanf("%d",&x)
#define dsfll(x) ll x; scanf("%lld",&x)
#define dsff(x) float x; scanf("%f",&x)
#define dsfd(x) double x; scanf("%g",&x)
#define dsfc(x) char x; scanf("%c",&x)
#define sfi(x) scanf("%d",&x)
#define sfll(x) scanf("%lld",&x)
#define sfd(x) scanf("%g",&x)
#define sfc(x) scanf("%c",&x)
#define pfi(x) printf("%d",x)
#define pfll(x) printf("%lld",x)
#define pfd(x) printf("%g",x)
#define pfc(x) printf("%c",x)
#define pfin(x) printf("%d\n",x)
#define pflln(x) printf("%lld\n",x)
#define pfdn(x) printf("%g\n",x)
#define pfcn(x) printf("%c\n",x)
#define nl printf("\n")
#define pfis(x) printf("%d ",x)
#define pflls(x) printf("%lld ",x)
#define pfds(x) printf("%g ",x)
#define pfcs(x) printf("%c ",x)
#define vi vector<int>
#define si set<int>
#define ll long long
#define vll vector<ll>
#define sll set<ll>
#define msi map<string,int>
#define pb(x) push_back(x)
#define repvi(it,v) for(vi it=v.begin();it!=v.end();it++)
#define repsi(it,s)  for(si it=s.begin();it!=s.end();it++)
#define repvll(it,v) for(vll it=v.begin();it!=v.end();it++)
#define repsll(it,s)  for(sll it=s.begin();it!=s.end();it++)
#define rep(cursor,beg,end) for(int cursor=beg;cursor<end;cursor++)
#define repll(cursor,beg,end) for(ll cursor=beg;cursor<end;cursor++)
#define repr(cursor,end,beg) for(int cursor=end;cursor>=beg;cursor--)
#define reprll(cursor,end,beg) for(ll cursor=end;cursor>=beg;cursor--)
#define alloc(a,n)  a=(int*)malloc(n*sizeof(int))
#define arralloc(a,r,c) a=(int**)malloc(r*sizeof(int*)); rep(cur,0,r) alloc(a[cur],c)
#define min3(a,b,c) min(a,min(b,c))
#define min4(a,b,c,d) min(a,min3(b,c,d))
#define max3(a,b,c) max(a,max(a,b))
#define max4(a,b,c,d) max(a,max(a,b,c,d))
#define on(i,x) ( x | (1<<i) )
#define off(i,x) ( x & ~(1<<i) )
#define ifon(i,x) ( x & (1<<i) )
#define toggle(i,x) ( x ^ (1<<i) )
#include <bits/stdc++.h>

using namespace std;

void change(string s){
	int ind=0,prob=-1,len=s.length();
	
	rep(i,0,len-1){
		if( s[i]!=s[ind] ) ind=i;
		if( s[i]>s[i+1] ){   prob=ind;	break; 	}
	}
	if( prob==-1 ) cout<<s;
	else{
		rep(i,0,prob) if(s[i]!='0') cout<<s[i];
		if( s[prob]-49!=0 ) cout<<(s[prob]-49);
		rep(i,prob+1,len) cout<<'9';
	}
}

int main(void){
	dsfi(t);
	rep(c,1,t+1){
		string s;
		cin>>s;
		cout<<"Case #"<<c<<": ";
		change(s);
		nl;
	}
}