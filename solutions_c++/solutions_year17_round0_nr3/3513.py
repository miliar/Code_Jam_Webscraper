#include<iostream>
#include<queue> 
#include<stdio.h>
#include<math.h>
using namespace std;
typedef pair<int,int> pii;
typedef pair<int, pii> piii;
int T;
void Gao(){
	scanf("%d",&T);
	for(int k =1;k<=T;k++){
		priority_queue<piii> q;
		int kk, nn;
		scanf("%d %d",&kk,&nn);
		int st = 0,ed = kk+1;
		q.push(make_pair(ed-st,make_pair(st,ed)));
		int ansMin =-1;
		int ansMax = -1;
		for(int i=0;i<nn;i++){
			piii tem = q.top();
			q.pop();
			int prevSt = tem.second.first;
			int prevEd = tem.second.second;
			int prevLen = tem.first;
			int curPos = prevSt + floor(prevLen*0.5);
			ansMin = min(curPos-prevSt-1,prevEd-curPos-1);
			ansMax = max(curPos-prevSt-1,prevEd-curPos-1);
			q.push(make_pair(curPos-prevSt,make_pair(prevSt,curPos)));
			q.push(make_pair(prevEd-curPos,make_pair(curPos,prevEd)));
		}
		printf("Case #%d: %d %d\n",k,ansMax,ansMin);
	}
}
int main(){
	freopen("C-small-2-attempt0.in","r",stdin);
	freopen("C-small-2-attempt0.out","w",stdout);
	Gao();
	
}
