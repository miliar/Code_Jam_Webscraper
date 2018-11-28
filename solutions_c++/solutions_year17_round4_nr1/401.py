#include<bits/stdc++.h>


using namespace std;

int n,p,cas,tot;

int has[5];

void Work(){
	printf("Case #%d: ",++cas);
	if(p==2){
		printf("%d\n",has[0]+has[1]/2+1-(tot==0));
	}
	else if(p==3){
		printf("%d\n",has[0]+min(has[1],has[2])+(has[1]+has[2]-2*min(has[1],has[2]))/3+1-(tot==0));
	}
	else{
		int ans=has[0]+has[2]/2;
		has[2]%=2;
		ans+=min(has[1],has[3]);
		int t=min(has[1],has[3]);
		has[1]-=t;has[3]-=t;
		if(!has[2]){
			ans+=max(has[1],has[3])/4;
		}
		else{
			if(max(has[1],has[3])>=2){
				ans+=1+(max(has[1],has[3])-2)/4;
			}
		}
		printf("%d\n",ans+1-(tot==0));
	}
}

void Init(){
	scanf("%d%d",&n,&p);
	for(int i=0;i<4;i++)has[i]=0;
	tot=0;
	for(int i=1;i<=n;i++){
		int x;
		scanf("%d",&x);
		has[x%p]++;
		tot+=x;
		tot%=p;
	}
}

int main(){
	freopen("A2.in","r",stdin);
	freopen("A2.out","w",stdout);
	int T;
	scanf("%d",&T);
	while(T--){
		Init();
		Work();
	}
	return 0;
}
