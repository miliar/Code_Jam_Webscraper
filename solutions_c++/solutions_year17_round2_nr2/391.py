#include<cstdio>
#include<cstring>
#include<algorithm>
#include<set>
#include<map>
#include<string>
#include<iostream>
using namespace std;

typedef long long ll;

const char ch[]={'B','R','Y','O','G','V'};
int n,m,i,j,k,l,p,ca;
int a[7],b[7];
int c[11111];
string s;
int v[5][1001][1001][1001];

bool dfs(int n,int t,int b,int r,int y){
    if(b<0||r<0||y<0)return 0;
    if(v[t][b][r][y]==ca)return 0;v[t][b][r][y]=ca;
    if(n>m){
      if(c[m]!=c[1]){
        for(int i=1;i<=m;i++){
          s+=ch[c[i]];
          if(a[c[i]+3])a[c[i]+3]--,s+=ch[c[i]+3],s+=ch[c[i]];
        }
        return 1;
      }
      return 0;
    }
    if(t!=0){c[n]=0;if(dfs(n+1,0,b-1,r,y))return 1;}
    if(t!=1){c[n]=1;if(dfs(n+1,1,b,r-1,y))return 1;}
    if(t!=2){c[n]=2;if(dfs(n+1,2,b,r,y-1))return 1;}
    return 0;
}
int main(){
	//freopen("1.in","r",stdin);freopen("1.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(;T;T--){
		printf("Case #%d: ",++ca);
		scanf("%d",&n);
    scanf("%d%d%d%d%d%d",&a[1],&a[3],&a[2],&a[4],&a[0],&a[5]);
    memcpy(b,a,sizeof(a));

    int cnt=0;for(int j=0;j<3;j++)cnt+=(a[j]>0);

    a[0]-=a[3];
    a[1]-=a[4];
    a[2]-=a[5];
    s="";
    m=a[0]+a[1]+a[2];

    if(m==0&&cnt==1){
      for(int i=1;i<=n/2;i++)
      {
        for(int j=0;j<3;j++)if(b[j])s+=ch[j],s+=ch[j+3];
      }
      cout<<s<<endl;
    }
    else if(dfs(1,4,a[0],a[1],a[2])) cout<<s<<endl;
    else printf("IMPOSSIBLE\n");
	}

	return 0;
}
