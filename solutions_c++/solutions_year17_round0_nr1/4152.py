#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
#define MAXN 1010
#define forr(i,a,b) for(int (i)=(int)(a);(i)<(int)(b);(i)++)
#define forn(i,n) forr(i,0,n)
#define forall(it,v) for(auto it=v.begin();it!=v.end();++it)
#define rforr(i,a,b) for(int (i)=((int)a-1);(i)>=(int)b;(i)--)
#define rforn(i,n) rforr(i,n,0)
#define rforall(it,v) for(auto it=v.rbegin();it!=v.rend();++it)
#define zero(v) memset(v, 0, sizeof(v))
#define jmp cout << '\n'
#ifdef ACM
#define dcout(v) cout << #v"=" << v << '\n'
#define dprint(v) cout << v
#define set_cin 
#else
#define dcout(v)
#define dprint(v)
#define set_cin ios::sync_with_stdio(0);cin.tie(0)
#endif

string s;

int flip(int p,int k){
	forr(i,p,k)if(s[i]=='-')s[i]='+';
	else s[i]='-';
	return 1;
}

int main(void){
	set_cin;
	int t,k,j;
	cin >> t;
	forn(c,t){
		j=0;cin >> s >> k;
		forn(i,s.length()-k+1)if(s[i]=='-')j+=flip(i,i+k);
		forn(i,s.length())if(s[i]=='-')j=-1;
		if(j==-1)cout << "Case #" << c+1 << ": IMPOSSIBLE\n";
		else cout << "Case #" << c+1 << ": " << j << '\n';
	}
	
	return 0;
}
