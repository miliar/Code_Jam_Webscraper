// by ξ
// program sky  :)

#include <vector>
#include <string>
#include <complex>
#include <stdio.h>
#include <cassert>
#include <algorithm>

#define Rin register int
#define oo (c=getchar())
#define For(i,l,r) for(int _r=r,i=l;i<=_r;++i)
#define rep(i,l,r) for(int _r=r,i=l;i<_r;++i)
#define dto(i,r,l) for(int _l=l,i=r;i>=_l;--i)
#define ALL(V) V.begin(),V.end()
#define SZ(A) (int(A.size()))
#define pb push_back
#define mk make_pair
#define x first
#define y second

using namespace std;

typedef double db;
typedef long long LL;
typedef pair<int ,int> PII;
typedef complex<db> cpx;
typedef vector<int> VI;
typedef vector<PII> VII;

inline int IN(){
	char c;Rin x=0;
	for(;oo<48 && c^'-' || c>57;);bool f=c=='-';if(f)oo;
	for(;c>47 && c<58;oo)x=(x<<3)+(x<<1)+c-48;if(f)x=-x;return x;
}

inline void hello(){
	freopen("ha.in","r",stdin);
//	freopen("ha.out","w",stdout);
}

inline bool ok(int a,int b,int c){
	if(a<0 || b<0 || c<0)return 0;
	if(a<b)swap(a,b);
	if(a<c)swap(a,c);
	return a<=b+c;
}

inline string gao(int R,int Y,int B){
	int ma = max(max(R,Y),B);
	string a = "",b = "",c = "";
	if(ma == R){
		For(i,1,R)a+='R';
		For(i,1,Y)b+='Y';
		For(i,1,B)c+='B';
	}else if(ma == Y){
		For(i,1,Y)a+='Y';
		For(i,1,R)b+='R';
		For(i,1,B)c+='B';
	}else{
		For(i,1,B)a+='B';
		For(i,1,Y)b+='Y';
		For(i,1,R)c+='R';
	}
	string d = "";
	rep(i,0,a.length()){
		d+=a[i];
		if(i<b.length())d+=b[i];
	}
	string e = "";
	dto(i,d.length()-1,0){
		if(d.length()-i<=c.length())e=c[c.length()-d.length()+i]+e;
		e=d[i]+e;
	}
	return e;
}

int main(){
// say hello
	hello();
	For(tc,1,IN()){
		printf("Case #%d: ",tc);
		int n,a[7];
		n=IN();
		a[1]=IN();a[3]=IN();a[2]=IN();a[6]=IN();a[4]=IN();a[5]=IN();
		int R=a[1]-a[6];
		int Y=a[2]-a[5];
		int B=a[4]-a[3];
		if(!ok(R,Y,B)){
			puts("IMPOSSIBLE");
			continue;
		}
		if(!R && a[1] || !Y && a[2] || !B && a[4]){
			if(!R && a[1]){
				if(a[2] || a[4])puts("IMPOSSIBLE");
				else{
					For(i,1,a[1]){
						putchar('R');
						putchar('G');
					}
					puts("");
				}
			}else if(!Y && a[2]){
				if(a[1] || a[4])puts("IMPOSSIBLE");
				else{
					For(i,1,a[2]){
						putchar('Y');
						putchar('V');
					}
					puts("");
				}
			}else{
				if(a[1] || a[2])puts("IMPOSSIBLE");
				else{
					For(i,1,a[4]){
						putchar('B');
						putchar('O');
					}
					puts("");
				}
			}
			continue;
		}
		string str = gao(R,Y,B);
		bool fR=0,fY=0,fB=0;
		rep(i,0,str.length()){
			if(str[i]=='R'){
				if(!fR){
					fR=1;
					putchar('R');
					For(j,1,a[6])putchar('G'),putchar('R');
				}else putchar('R');
			}else if(str[i]=='B'){
				if(!fB){
					fB=1;
					putchar('B');
					For(i,1,a[3])putchar('O'),putchar('B');
				}else putchar('B');
			}else{
				if(!fY){
					fY=1;
					putchar('Y');
					For(i,1,a[5])putchar('V'),putchar('Y');
				}else putchar('Y');
			}
		}
		puts("");
	}
// never say goodbye
}