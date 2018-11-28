#include <cstdio>
#include <cstring>

struct Node{
	int P;
	int ID;
}a[1010];

bool usedP[1010][1010];
bool usedID[1010][1010];
int ans1,ans2;

bool T1(int num){
	for(int i=0;i<ans1;++i){
		if(!usedID[i][a[num].ID] && !usedP[i][a[num].P]){
			usedID[i][a[num].ID] = true;
			usedP[i][a[num].P] = true;
			return true;
			break;
		}
	}
	return false;
}

void T2(int num){
	++ans2;
	for(int i=0;i<ans1;++i){
		if(!usedID[i][a[num].ID]){
			for(int j = a[num].P - 1; j>0 ; --j){
				if(!usedP[i][j]){
					usedID[i][a[num].ID] = true;
					usedP[i][j] = true;
					return ;
				}
			}
		}
	}
}

int main(){
	int T,N,C,M;
	int count[3];
	int pos[1010];
	bool OK[1010];
	scanf("%d",&T);
	for(int ca = 1; ca <= T; ++ca ){
		scanf("%d %d %d",&N,&C,&M);
		memset(pos,0,sizeof(pos));
		memset(usedP,false,sizeof(usedP));
		memset(usedID,false,sizeof(usedID));
		memset(OK,false,sizeof(OK));
		count[2] = count[1] = 0;
		for(int i=0;i<M;++i){
			scanf("%d %d",&a[i].P,&a[i].ID);
			++count[a[i].ID];
			++pos[a[i].P];
		}
		ans1 = count[2] > count[1] ? count[2] : count[1];
		ans2 = 0;
		if(pos[1] > ans1) ans1 = pos[1];

//		printf("%d %d %d %d\n",count[1],count[2],pos[1],pos[2]);

		for(int i=1;i<=N;++i)
			if(pos[i] > ans1)
				ans2 += pos[i] - ans1;
/*		
		for(int i=0;i<M;++i){
			if(T1(i)){
				OK[i] = true;
			}
		}

		for(int i=0;i<M;++i){
			if(!OK[i])
				T2(i);
		}
*/
		printf("Case #%d: %d %d\n",ca,ans1,ans2);
	}
	return 0;
}
