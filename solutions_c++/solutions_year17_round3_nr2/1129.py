#include <bits/stdc++.h>
using namespace std;

typedef pair<int,int> ii;
int t,ac,aj,ans;
ii C[105],J[105];

int main(){
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small.out","w",stdout);
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		scanf("%d%d",&ac,&aj);
		for(int i=0;i<ac;i++){
			int a,b;
			scanf("%d%d",&a,&b);
			C[i]=ii(a,b);
		}
		for(int i=0;i<aj;i++){
			int a,b;
			scanf("%d%d",&a,&b);
			J[i]=ii(a,b);
		}
		if(ac==0){
			sort(J,J+aj);
			if(aj==1) ans=2;
			else{
				int time=J[1].second-J[1].first+J[0].second-J[0].first;
				if(time==720){
					time=J[1].second-J[0].first;
					if(time>720&&time<1440) ans=4;
					else ans=2;
				}
				else{
					time=J[1].second-J[0].first;
					if(time<=720) ans=2;
					else{
						if(J[1].first-J[0].second>=720) ans=2;
						else ans=4;
					}
				}
			}
		}
		else if(aj==0){
			sort(C,C+ac);
			if(ac==1) ans=2;
			else{
				int time=C[1].second-C[1].first+C[0].second-C[0].first;
				if(time==720){
					time=C[1].second-C[0].first;
					if(time>720&&time<1440) ans=4;
					else ans=2;
				}
				else{
					time=C[1].second-C[0].first;
					if(time<=720) ans=2;
					else{
						if(C[1].first-C[0].second>=720) ans=2;
						else ans=4;
					}
				}
			}
		}
		else{
			ans=2;
		}
		printf("Case #%d: %d\n",tc,ans);
	}
}
