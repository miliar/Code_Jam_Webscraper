#include <stdio.h>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

#define pii pair<int,int>

using namespace std;

const int INF=1e9+10;

int t;

pair <pii,int> inter[300];
vector <int> exc[2];

int main(){
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++){
		int ac,aj;
		scanf("%d %d",&ac,&aj);
		for(int i=0;i<ac;i++){
			int a,b;
			scanf("%d %d",&a,&b);
			inter[i]=make_pair( make_pair(a,b) , 0 );
		}
		for(int i=0;i<aj;i++){
			int a,b;
			scanf("%d %d",&a,&b);
			inter[ac+i]=make_pair( make_pair(a,b) , 1 );
		}
		int n=ac+aj;
		sort(inter,inter+n);
		
		
		int nec[2],excs[2],op=0,resp=0;
		nec[0]=nec[1]=excs[0]=excs[1]=0;
		inter[n]=inter[0];
		inter[n].first.first+=1440;
		inter[n].first.second+=1440;
		for(int i=1;i<n+1;i++){
			nec[inter[i].second]+=inter[i].first.second-inter[i].first.first;
			if(i!=0){
				if(inter[i].second==inter[i-1].second){
					excs[inter[i].second]+=inter[i].first.first-inter[i-1].first.second;
					exc[inter[i].second].push_back(inter[i].first.first-inter[i-1].first.second);
				}
				else{
					resp++;
					op+=inter[i].first.first-inter[i-1].first.second;
				}
			}
		}
		int at=2;
		if(nec[0]+excs[0]>720) at=0;
		if(nec[1]+excs[1]>720) at=1;
		if(at<2){
//			printf("at==%d\n",at);
			int sum=nec[1-at]+excs[1-at];
			sort(exc[at].begin(),exc[at].end());
			for(int i=exc[at].size()-1;i>=0 && sum<720;i--){
				resp+=2;
				sum+=exc[at][i];
//				printf("*   %d\n",exc[at][i]);
			}
		}
		exc[0].clear();
		exc[1].clear();
		printf("Case #%d: ",tt);
		printf("%d\n",resp);
	}
	return 0;
}
