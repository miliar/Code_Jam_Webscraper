#include<stdio.h>
#include<string.h>
double E[1010],S[1010],D[1010][1010],d[1010];
int n;
double DO(int x,int y){
	//puts("GO");
	int i,s,j;
	for(i=0;i<n;i++)
		d[i]=-1;
	d[x]=0;
	/*for(i=0;i<n;i++){
		for(j=0;j<n;j++)
			printf("%.0lf ",D[i][j]);
			puts("");
			}
	*/
	while(1){
		for(s=-1,i=0;i<n;i++)
			if(d[i]>=0&&(s==-1||d[s]>d[i]))
				s = i;
		//printf("%d %lf\n",s,d[s]);
		if(s==y)
			return d[y];
		if(s==-1)
			break;
		for(i=0;i<n;i++){
			if(D[s][i]==-1)
				continue;
			if(D[s][i]<=E[s]&&(d[i]==-1||d[i]>d[s]+D[s][i]/S[s]))
				d[i] = d[s]+D[s][i]/S[s];
			//printf("~%lf %lf\n",d[s]+D[s][i]/S[s],d[i]);
		}
		d[s]=-2;
		
	}
	puts("QQ");
}
int main(){
	int T,t,i,q,j,x,y,k;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d%d",&n,&q);
		for(i=0;i<n;i++)
			scanf("%lf%lf",&E[i],&S[i]);
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				scanf("%lf",&D[i][j]);
		for(k=0;k<n;k++){
			for(i=0;i<n;i++){
				for(j=0;j<n;j++){
					if(D[i][k]==-1||D[k][j]==-1)
						continue;
					if(D[i][j]==-1||D[i][j]>D[i][k]+D[k][j])
						D[i][j] = D[i][k]+D[k][j];
				}
			}
		}
			
		printf("Case #%d:",t);
		for(i=0;i<q;i++){
			scanf("%d%d",&x,&y);
			printf(" %lf",DO(x-1,y-1));
		}
		puts("");
	}
}
