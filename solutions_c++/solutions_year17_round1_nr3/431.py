#include <cstdio>
#include <queue>
#include <map>

#define mp(x,y) make_pair(x,y)
using namespace std;

const int Maxn=100;

int Hd,Ad,Hk,Ak,B,D;
int fHP;

struct Node{
	int hp,atk;
	int ehp,eatk;
	int step;
	Node(){}
	Node(int h0,int a0,int eh0,int ea0,int s0){
		hp=h0;
		atk=a0;
		ehp=eh0;
		eatk=ea0;
		step=s0;
	}
};

queue<Node> que;
map<pair<pair<int,int>,pair<int,int> >,bool> vis;

inline void solve(int T){
	vis.clear();
	while(!que.empty()) que.pop();
	scanf("%d%d%d%d%d%d",&Hd,&Ad,&Hk,&Ak,&B,&D);
	fHP=Hd;
	que.push(Node(Hd,Ad,Hk,Ak,0));
	vis[mp(mp(Hd,Ad),mp(Hk,Ak))]=true;


	int Ans=-1;

	while(!que.empty()){
		int mHp=que.front().hp,mAt=que.front().atk;
		int eHp=que.front().ehp,eAt=que.front().eatk;
		int step=que.front().step;
		que.pop();
		//ATK
		if (eHp<=mAt){
			Ans=step;
			break;
		}else if (mHp>eAt){
			if (!vis[mp(mp(mHp-eAt,mAt),mp(eHp-mAt,eAt))]){
				vis[mp(mp(mHp-eAt,mAt),mp(eHp-mAt,eAt))]=true;
				que.push(Node(mHp-eAt,mAt,eHp-mAt,eAt,step+1));
			}
		}
		//RECOVERY
		if (fHP>eAt){
			if (!vis[mp(mp(fHP-eAt,mAt),mp(eHp,eAt))]){
				vis[mp(mp(fHP-eAt,mAt),mp(eHp,eAt))]=true;
				que.push(Node(fHP-eAt,mAt,eHp,eAt,step+1));
			}
		}

		//DECREASE ATK
		if (mHp>max(0,eAt-D)){
			if (!vis[mp(mp(mHp-max(0,eAt-D),mAt),mp(eHp,max(0,eAt-D)))]){
				vis[mp(mp(mHp-max(0,eAt-D),mAt),mp(eHp,max(0,eAt-D)))]=true;
				que.push(Node(mHp-max(0,eAt-D),mAt,eHp,max(0,eAt-D),step+1));
			}
		}

		//INCREASE ATK
		if (mHp>eAt){
			if (!vis[mp(mp(mHp-eAt,mAt+B),mp(eHp,eAt))]){
				vis[mp(mp(mHp-eAt,mAt+B),mp(eHp,eAt))]=true;
				que.push(Node(mHp-eAt,mAt+B,eHp,eAt,step+1));
			}
		}
	}

	if (Ans==-1) printf("Case #%d: IMPOSSIBLE\n",T); else printf("Case #%d: %d\n",T,Ans+1);
}

int main(){
	freopen("C-small-attempt0.in.txt","r",stdin);
	freopen("COut.txt","w",stdout);
	int T=0;scanf("%d",&T);
	for (int i=1;i<=T;i++) solve(i);
	return 0;
}