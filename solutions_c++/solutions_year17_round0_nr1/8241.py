#include<bits/stdc++.h>
using namespace std;
#define INF 0x3f3f3f3f
#define DINF 1e10
#define EPS 1e-15
#define PII acos(-1)
#define LL long long
#define Pii pair<int,int>
#define For(i,n) for(int i=0;i<n;i++)
#define ileer(n) scanf("%d",&n)
#define i2leer(n,m) scanf("%d %d",&n,&m)
#define fleer(n) scanf("%lf",&n)
#define f2leer(n,m) scanf("%Lf %Lf",&n,&m)
#define MK make_pair
#define PB push_back
#define llenar(arr,val) memset(arr,val,sizeof(arr))
#define VLL vector< LL >
#define matrix vector<VI >
#define F first
#define S second
#define MAXN 1005

int main(){
	//freopen("entrada.in","r",stdin);
	//freopen("salida.out","w",stdout);
	int t;
	ileer(t);
	For(c,t){
		string g;
		string g2;
		int k;
		cin>>g>>k;
		g2=g;
		int n=g.size();
		bool sepuede=true;
		bool sepuede2=true;
		int pasos=0;
		int mejor;
		
		int pasos2=0;
		for(int i=0;i<n;i++){
			if(g[i]=='-'){
				if(i+k-1>=n){ sepuede=false; break;}
				pasos++;
				for(int j=0;j<k;j++){
					g[i+j]=g[i+j]=='+'?'-':'+';
				}
			}
			//cout<<g<<" "<<i<<" "<<i+k<<endl;
		}
		
		for(int i=n-1;i>=0;i--){
			if(g2[i]=='-'){
				if(i-k+1<0){ sepuede2=false; break;}
				pasos2++;
				for(int j=0;j<k;j++){
					g2[i-j]=g2[i-j]=='+'?'-':'+';
				}
			}
			//cout<<g<<" "<<i<<" "<<i+k<<endl;
		}
		
		if(sepuede && sepuede2){
			mejor=min(pasos,pasos2);
		}else if(sepuede){
			mejor=pasos;
		}else if(sepuede2){
			mejor=pasos2;
		}
		
		
		
		if(sepuede || sepuede2){
			printf("Case #%d: %d\n",c+1,mejor);
		}else{
			printf("Case #%d: IMPOSSIBLE\n",c+1);
		}
		
	}
	
}