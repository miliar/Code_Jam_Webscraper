#include<bits/stdc++.h>
#define fi first
#define se second
using namespace std;

struct candidate{
	int pos , ls , rs;
	candidate() : pos(0) , ls(0) , rs(0) {};
	bool operator < (const candidate &b){
		if(min(ls, rs) == min(b.ls , b.rs)){
			if(max(ls , rs) == max(b.ls , b.rs)) return (pos < b.pos);
			return max(ls , rs) > max(b.ls , b.rs);
		}
		return (min(ls , rs) > min(b.ls , b.rs));
	}
	void assign(int start,int finish){
		pos = (start + finish)/2;
		ls = pos - start;
		rs = finish - pos;
	}
};
int n , k;

struct seg{
	int start , finish;
	seg(int _start = 0,int _finish = 0) : start(_start) , finish(_finish) {};
	bool operator < (const seg &b) const{
		candidate candidate, candidateB;
		candidate.assign(start , finish);
		candidateB.assign(b.start , b.finish);
		return (candidate < candidateB);
	}
};

set < seg > ss;

void solve(int Tc){
	printf("Case #%d: ",Tc);
	ss.clear();
	scanf("%d %d",&n,&k);
	ss.insert(seg(1 , n));
	for(int i = 1 ; i <= k ; i++){
		set < seg > :: iterator it;
		it = ss.begin(); 
		ss.erase((*it));
		int start = it -> start , finish = it -> finish;
		candidate cur;
		cur.assign(start , finish);
		if(i == k)	printf("%d %d\n",max(cur.ls , cur.rs) , min(cur.ls,cur.rs));
		else{
			if(cur.pos - 1 >= start)	ss.insert(seg(start , cur.pos - 1));
			if(cur.pos + 1 <= finish)	ss.insert(seg(cur.pos + 1 , finish));	
		}
	}	
}

int main(){
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int Tc;
	scanf("%d",&Tc);
	for(int i = 1 ; i <= Tc ; i++)	solve(i);
}

