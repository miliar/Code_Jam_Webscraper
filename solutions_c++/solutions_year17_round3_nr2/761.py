#include<bits/stdc++.h>
using namespace std;
struct Section{
	int l,r,type;
	bool operator<(const Section& rhs) const{
		return l<rhs.l;
	}
};
struct Node{
	int minus,type;
	bool operator<(const Node& rhs) const{
		return minus<rhs.minus;
	}
};
int C[105],D[105],J[105],K[105];
vector<Section> sec;
vector<Node> CNode,JNode;
vector<int> tmp;
int main(){
	int AC,AJ,tcase,kase=0;
	scanf("%d",&tcase);
	while(tcase--){
		scanf("%d%d",&AC,&AJ);
		sec.clear();
		CNode.clear();
		JNode.clear();
		tmp.clear();
		int reC=720,reJ=720;
		for(int i=0;i<AC;i++){
			scanf("%d%d",C+i,D+i);
			sec.push_back((Section){C[i],D[i],1});
			sec.push_back((Section){C[i]+1440,D[i]+1440,1});
			reC-=D[i]-C[i];
		}
		for(int i=0;i<AJ;i++){
			scanf("%d%d",J+i,K+i);
			sec.push_back((Section){J[i],K[i],2});
			sec.push_back((Section){J[i]+1440,K[i]+1440,2});
			reJ-=K[i]-J[i];
		}
		sort(sec.begin(),sec.end());
		for(int i=0;i<(int)sec.size() && sec[i].l<1440;i++){
			if(sec[i].type==sec[i+1].type){
				if(sec[i].type==1){
					CNode.push_back((Node){sec[i+1].l-sec[i].r,1});
				}else{
					JNode.push_back((Node){sec[i+1].l-sec[i].r,2});
				}
			}
		}
		sort(CNode.begin(),CNode.end());
		sort(JNode.begin(),JNode.end());
		for(int i=0;i<(int)CNode.size();i++){
			if(CNode[i].minus<=reC){
				reC-=CNode[i].minus;
				AC--;
			}
		}
		for(int i=0;i<(int)JNode.size();i++){
			if(JNode[i].minus<=reJ){
				reJ-=JNode[i].minus;
				AJ--;
			}
		}
		int minus=0;
		for(int i=0;i<(int)sec.size() && sec[i].l<1440;i++){
			if(sec[i].type!=sec[i+1].type){
				tmp.push_back(sec[i+1].l-sec[i].r);
			}
		}
		sort(tmp.begin(),tmp.end());
		for(int i=0;i<tmp.size();i++){
			int t=min(tmp[i],reC);
			reC-=t;
			tmp[i]-=t;
			t=min(tmp[i],reJ);
			reJ-=t;
			tmp[i]-=t;
			if(tmp[i]==0) minus++;
		}
		printf("Case #%d: %d\n",++kase,(AC+AJ)*2-minus);
	}
	return 0;
}
