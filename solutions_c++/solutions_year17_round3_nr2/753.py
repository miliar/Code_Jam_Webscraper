#include <cstdio>
#include <algorithm>

using namespace std;

//1440

struct Node{
	int start,end;
	int belong;
}WorkA[110],WorkB[110],Total[220];

struct Node2{
	int pre,next;
	int OK;
	int dis;
}DIS[220];

bool cmp(Node a,Node b){
	return a.start < b.start;
}

bool cmp2(Node2 a,Node2 b){
	return a.dis < b.dis;
}

int main(){
	int T;
	int AC,AJ;
	int leftA,leftB;
	scanf("%d",&T);
	for(int ca = 1; ca <= T; ++ca){
		scanf("%d %d",&AC,&AJ);
		leftA = leftB = 720;
		for(int i=0;i<AC;++i){
			scanf("%d %d",&WorkA[i].start,&WorkA[i].end);
			Total[i].start = WorkA[i].start;
			Total[i].end = WorkA[i].end;
			Total[i].belong = 1;
			leftA -= WorkA[i].end - WorkA[i].start;
		}
		for(int i=0;i<AJ;++i){
			scanf("%d %d",&WorkB[i].start,&WorkB[i].end);
			Total[i+AC].start = WorkB[i].start;
			Total[i+AC].end = WorkB[i].end;
			Total[i+AC].belong = 2;
			leftB -= WorkB[i].end - WorkB[i].start;
		}
		
		sort(Total,Total+AC+AJ,cmp);

		for(int i=0;i<AC+AJ-1;++i){
			DIS[i].pre = i;
			DIS[i].next = i+1;
			if(Total[i].belong == Total[i+1].belong)
				DIS[i].OK = 1;
			else 
				DIS[i].OK = 0;
			DIS[i].dis = Total[i+1].start - Total[i].end;
		}
		DIS[AC+AJ-1].pre = AC+AJ-1;
		DIS[AC+AJ-1].next = 0;
		if(Total[AC+AJ-1].belong == Total[0].belong)
			DIS[AC+AJ-1].OK = 1;
		else 
			DIS[AC+AJ-1].OK = 0;
		DIS[AC+AJ-1].dis = 1440 - Total[AC+AJ-1].end + Total[0].start;


		sort(DIS,DIS+AC+AJ,cmp2);

		for(int i=0;i<AC+AJ;++i){
			if(DIS[i].OK == 1){
				if(Total[DIS[i].pre].belong == 1){
					if(leftA >= DIS[i].dis){
						leftA -= DIS[i].dis;
						DIS[i].OK = -1;
					}
					else{
						leftA = 0;
						DIS[i].dis -= leftA;
					}
				}
				else{
					if(leftB >= DIS[i].dis){
						leftB -= DIS[i].dis;
						DIS[i].OK = -1;
					}
					else{
						leftB = 0;
						DIS[i].dis -= leftB;
					}
				}
			}
		}

		int ans = 0;

		for(int i=0;i<AC+AJ;++i){
			if(DIS[i].OK == 0){
				++ans;
			}
			else if(DIS[i].OK==1){
				ans += 2;
			}
		}

		printf("Case #%d: %d\n",ca,ans);
	}
	return 0;
}
