#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long int ull;
typedef long double ld;
#define MAXN 1000010
#define forr(i,a,b) for(int (i)=(int)(a);(i)<(int)(b);(i)++)
#define forn(i,n) forr(i,0,n)
#define forall(it,v) for(auto it=v.begin();it!=v.end();++it)
#define rforr(i,a,b) for(int (i)=((int)a-1);(i)>=(int)b;(i)--)
#define rforn(i,n) rforr(i,n,0)
#define rforall(it,v) for(auto it=v.rbegin();it!=v.rend();++it)
#define zero(v) memset(v, 0, sizeof(v))
#define jmp cout << '\n'
#ifdef ACM
#define dcout(v) cout << #v"=" << v << ' ';
#define dprint(v) cout << v
#define set_cin 
#else
#define dcout(v)
#define dprint(v)
#define set_cin ios::sync_with_stdio(0);cin.tie(0)
#endif

pair <ull,ull> res;

void situar(ull n,ull d,ull h,ull m){
	if(m<=0){
		if(abs(h-d)>=abs(res.second-res.first)){res.first=min(h,d);res.second=max(h,d);}
		return;
	}
	int p=d+(h-d)/2;m--;
	if(m%2==0){situar(n,d,p,m/2);situar(n,p,h,m/2);
	}else if((h-d)%2==0){situar(n,d,p,(m/2)+1);situar(n,p,h,m/2);
	}else{situar(n,d,p,m/2);situar(n,p,h,(m/2)+1);
	}
}

//~ int nextp(ull n){
	//~ int k=-1,r,l,p,q;
	//~ p=q=0;
	//~ forn(i,n+2)if(!S[i]){
			//~ for(r=i+1;!S[r];r++);
			//~ for(l=i-1;!S[l];l--);
			//~ r=abs(r-i);l=abs(i-l);
			//~ if(p<min(r,l) || (p==min(r,l) && q<max(r,l))){
				//~ p=min(r,l);q=max(r,l);
				//~ k=i;
			//~ }
	//~ }
	//~ return k;
//~ }

int main(void){
	set_cin;
	
	ull t,n,l,r,k;
	
	cin >> t;
	forn(c,t){
		cin >> n >> k;
		res.first=res.second=0;
		situar(n,0,n+1,k-1);
		k=res.first+(res.second-res.first)/2;
		l=max(abs(k-res.first),abs(res.second-k))-1;
		r=min(abs(k-res.first),abs(res.second-k))-1;
		cout << "Case #" << c+1 << ": " << l << ' ' << r << '\n';
	}
	
	return 0;
}
