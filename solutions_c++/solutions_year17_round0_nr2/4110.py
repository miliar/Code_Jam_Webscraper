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

int tidy(string n){
	rforn(i,n.length()-1)if(n[i]>n[i+1])return i;
	return -1;
}

void without0(string n){
	int i;
	for(i=0;i<(int)n.length();i++)if(n[i]!='0')break;
	for(;i<(int)n.length();i++)cout << n[i];
	jmp;
}

int main(void){
	set_cin;
	
	int t,i;
	string n;
	
	cin >> t;
	forn(c,t){
		cin >> n;
		if(n.length()==1){
			cout << "Case #" << c+1 << ": " << n << '\n';
			continue;
		}
		while((i=tidy(n))!=-1){
			n[i]--;
			forr(j,i+1,n.length())n[j]='9';
		}
		cout << "Case #" << c+1 << ": ";
		without0(n);
	}
	
	return 0;
}
