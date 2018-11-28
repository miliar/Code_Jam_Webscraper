#include<bits/stdc++.h>
using namespace std;
const int maxn=2088;
int dp[maxn][725][2][2];
int n,m;
struct seg{
	int l,r,must;
	bool operator<(seg oth)const{
		return l<oth.l;
	}
	int len(){return r-l;}
	void print(){
		printf("[%d,%d) %d\n",l,r,must);
	}
}se[maxn];
int sum[maxn];
void up(int &x,int y){
	x=min(x,y);
}
int solve(){
	scanf("%d%d",&n,&m);
	memset(dp,0x7f,sizeof dp);
	const int inf=dp[0][0][0][0];
	int s=0;
	for(int i=1;i<=n;i++){
		int l,r;
		scanf("%d%d",&l,&r);
		se[++s]=(seg){l,r,1};
	}
	for(int i=1;i<=m;i++){
		int l,r;
		scanf("%d%d",&l,&r);
		se[++s]=(seg){l,r,0};
	}
	sort(se+1,se+1+s);
	int _s=s;
	for(int i=1;i<_s;i++){
		if(se[i].r<se[i+1].l)
			se[++s]=(seg){se[i].r,se[i+1].l,-1};
	}
	if(se[1].l!=0)
		se[++s]=(seg){0,se[1].l,-1};
	if(se[_s].r!=24*60)
		se[++s]=(seg){se[_s].r,24*60,-1};
	sort(se+1,se+1+s);

	for(int i=1;i<=s;i++)
		sum[i]=sum[i-1]+se[i].len();

//	for(int i=1;i<=s;i++)
//		se[i].print();

	if(se[1].must==-1){

		for(int l=0;l<=se[1].len();l++){
			if(l==0){
				dp[1][0][1][1]=0;
			}else
			if(l==se[1].len()){
				dp[1][l][0][0]=0;
			}else{
				dp[1][l][0][1]=1;
				dp[1][l][1][0]=1;
			}
		}
	}else{
		dp[1][se[1].len()][se[1].must][se[1].must]=0;
	}

	for(int m=0;m<2;m++)
	for(int i=1;i<s;i++){
		for(int j=0;j<=720;j++){
			for(int k=0;k<2;k++)if(dp[i][j][k][m]!=inf){
				//if(j%30==0)printf("dp[%d][%d][%d]=%d\n",i,j,k,dp[i][j][k]);
				if(se[i+1].must==0){
					if(j+se[i+1].len()<=720)
						up(dp[i+1][j+se[i+1].len()][0][m],dp[i][j][k][m]+(k!=0));
				}else
				if(se[i+1].must==1){
					up(dp[i+1][j][1][m],dp[i][j][k][m]+(k!=1));
				}else{
					for(int l=0;l<=se[i+1].len();l++){

						if(l==0){
							up(dp[i+1][j][1][m],dp[i][j][k][m]+(k!=1));
						}else
						if(l==se[i+1].len()){
							if(j+l<=720)up(dp[i+1][j+l][0][m],dp[i][j][k][m]+(k!=0));
						}else{
							if(j+l<=720)
								up(dp[i+1][j+l][0][m],dp[i][j][k][m]+(k!=1)+1);
							if(j+l<=720)
								up(dp[i+1][j+l][1][m],dp[i][j][k][m]+(k!=0)+1);
						}
					}
				}
			}
		}
	}


	return min(min(dp[s][720][0][0],dp[s][720][1][0]+1),min(dp[s][720][0][1]+1,dp[s][720][1][1]));
}

int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		printf("Case #%d: ",t);
		cout<<solve()<<endl;
	}
	return 0;
}
