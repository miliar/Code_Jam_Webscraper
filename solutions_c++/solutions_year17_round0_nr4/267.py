#include <bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define itt ::iterator
#define ritt ::reverse_iterator
#define MAXPQ(T) priority_queue<T>
#define MINPQ(T) priority_queue<T,vector<T>,greater<T> >
const int NSIZ=1010;
const int MSIZ=1000010;
const int inf=1010580540;
const int mxint=2147483647;
const long long mxll=9223372036854775807LL;
const long long prime15=1000000000000037LL;
const long long mod=1000000007LL;
const long long mod9=1000000009LL;
typedef pair<int,int> pii;
typedef pair<long long,int> pli;
typedef pair<long long,long long> pll;
typedef pair<double,double> pdd;
typedef pair<int,pair<int,int> > pip;
typedef pair<long long,pair<int,int> > plp;
typedef pair<pair<int,int>,pair<int,int> > ppp;

int n, m, o, re=0, test;
long long res=0;
char a[NSIZ][NSIZ], b[NSIZ][NSIZ];
bool row[NSIZ], col[NSIZ], dir[NSIZ], dic[NSIZ];
bool chk[NSIZ][NSIZ];
char conv[4]="+xo";
vector<pip> ans, ord;
vector<pii> ve[3];
void clean(){
	memset(row,0,sizeof(row));
	memset(col,0,sizeof(col));
	memset(dir,0,sizeof(dir));
	memset(dic,0,sizeof(dic));
	memset(chk,0,sizeof(chk));
	memset(b,0,sizeof(b));
	memset(a,0,sizeof(a));
	ans.clear();
	ord.clear();
	re=0;
	for(int i=0; i<3; i++)ve[i].clear();
}
void print(){
	for(int i=1; i<=n; i++){
		for(int j=1; j<=n; j++){
			int k=a[i][j]|b[i][j];
			if(k==1)printf("+");
			else if(k==2)printf("x");
			else if(k==3)printf("o");
			else printf(".");
		}printf("\n");
	}printf("\n");
}
int main(){
    int i, j, k, l;
    long long ll=0, rr=mxll, mid;
    scanf("%d", &test);
    for(int zz=1; zz<=test; zz++){
    	clean();
    	scanf("%d %d", &n, &m);
    	for(i=1; i<=n; i++){
    		for(j=1; j<=n; j++){
    			ord.push_back(pip(min(i-1,j-1)+min(n-i,j-1)+min(i-1,n-j)+min(n-i,n-j),pii(i,j)));
    		}
    	}
    	sort(ord.begin(),ord.end());
    	for(i=0; i<m; i++){
    		char c[2];
    		scanf("%s %d %d", c, &j, &k);
    		if(c[0]=='+' || c[0]=='o'){
    			a[j][k]++;
    			dir[j+n-k]=1;
    			dic[k+j]=1;
    		}
    		if(c[0]=='x' || c[0]=='o'){
    			a[j][k]+=2;
    			row[j]=1;
    			col[k]=1;
    		}
    	}
    	//++++++++
    	for(k=0; k<ord.size(); k++){
    		i=ord[k].S.F;j=ord[k].S.S;
			if(a[i][j]=='+' || a[i][j]=='o')continue;
			if(dir[i+n-j]==1 || dic[j+i]==1)continue;
			b[i][j]++;
			dir[i+n-j]=1;
			dic[j+i]=1;
    	}
    	//xxxxxxxx
    	for(k=0; k<ord.size(); k++){
    		i=ord[k].S.F;j=ord[k].S.S;
			if(a[i][j]=='x' || a[i][j]=='o')continue;
			if(row[i]==1 || col[j]==1)continue;
			b[i][j]+=2;
			row[i]=1;
			col[j]=1;
    	}
    	for(i=1; i<=n; i++){
    		for(j=1; j<=n; j++){
    			k=b[i][j]|a[i][j];
    			re+=(k>=1)+(k==3);
    			if(k==a[i][j])continue;
    			if(k==1)ans.push_back(pip('+',pii(i,j)));
    			if(k==2)ans.push_back(pip('x',pii(i,j)));
    			if(k==3)ans.push_back(pip('o',pii(i,j)));
    		}
    	}
    	printf("Case #%d: %d %d\n", zz, re, ans.size());
    	// if(re!=n*2+max(n-2,0))printf("!!!!!!!!!!\n");
    	for(i=0; i<ans.size(); i++){
    		printf("%c %d %d\n", ans[i]); 
    	}
    	// print();
    }
    return 0;
}
