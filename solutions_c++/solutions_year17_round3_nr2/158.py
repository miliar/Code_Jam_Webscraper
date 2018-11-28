#include <cstdio>
#include <vector>
#include <set>
#include <unordered_map>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

#define DAY (24*60)

struct task{
	int start;
	int end;
	int who;
	bool operator<(task other){
		return start<other.start;
	}
	int duration(){
		if(start==end){ return DAY; }
		return (end-start+DAY)%DAY;
	}
};

#define MAKE_INT(time0, time1, who) ((time0)+(time1)*(DAY+1)+(who)*(DAY+1)*(DAY+1))
#define GET_TIME0(i) ((i)%(DAY+1))
#define GET_TIME1(i) ( ((i)/(DAY+1))%(DAY+1) )
#define GET_WHO(i)   ((i)/(DAY+1)/(DAY+1))

void solve(){
	vector<task> tasks;
	int num[2];
	scanf("%d %d", &num[0], &num[1]);
	if(num[0]+num[1]==0){
		printf("2\n"); // No tasks.
		return;
	}
	for(int k=0;k<2;k++){
		for(int i=0; i<num[k]; i++){
			task p;
			scanf("%d %d",&p.start, &p.end);
			p.who=k;
			tasks.push_back(p);
		}
	}
	sort(tasks.begin(), tasks.end());
	int who_works[DAY];
	for(int i=0; i<DAY;i++){
		who_works[i]=-1;
	}
	for(auto t: tasks){
		for(int time=t.start; time<t.end; time++){
			who_works[time]=t.who;
		}
	}
	int best=1e9;
	for(int who_started=0; who_started<2; who_started++){
		unordered_map< int, int > mp;
		mp[MAKE_INT(0, 0, who_started)]=0;
		for(int t=0; t<DAY; t++){
			unordered_map< int, int > next;
			for(auto p: mp){
				int tm[2]={GET_TIME0(p.first), GET_TIME1(p.first)};
				int who=GET_WHO(p.first);
				for(int who_now=0; who_now<2; who_now++){
					if(who_works[t]==!who_now){ continue; }
					tm[who_now]++;
					if(tm[who_now]>DAY/2){ tm[who_now]--; continue; }
					int nextstate=MAKE_INT(tm[0], tm[1], who_now);
					tm[who_now]--;
					int switches=p.second;
					if(who_now!=who){
						switches++;
					}
					if(next.count(nextstate)==0 || next[nextstate]>switches){
						next[nextstate]=switches;
					}
				}
			}
			swap(next, mp);
		}
		int oc=mp[MAKE_INT(DAY/2, DAY/2, who_started)];
		if(oc){
			if(oc<best){ best=oc; }
		}
		//printf("If %d starts, best outcome is %d\n", who_started, oc);
	}
	printf("%d\n", best);
}

int main(){
	int t;
	scanf("%d", &t);
	for(int tc=0; tc<t; tc++){
		fprintf(stderr, "%d/%d\n", tc, t);
		printf("Case #%d: ", tc+1);
		solve();
	}
}
