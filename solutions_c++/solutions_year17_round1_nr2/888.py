#include<bits/stdc++.h>
#define LIMIT1 55
#define LIMIT2 1000000
#define fi first
#define se second

using namespace std;
typedef pair < int , int > ii;
typedef pair < int ,  ii > II;
long long R[LIMIT1] , Q[LIMIT1][LIMIT1];
int start[LIMIT1][LIMIT1] , finish[LIMIT1][LIMIT1];
int cur[LIMIT1] , n , p;
set < ii > ss[LIMIT1];
vector < II > event;

int findLeast(int ingredient, int index){
	int l = 0 , r = LIMIT2;
	while(l < r){
		int mid = (l + r + 2)/2;
		long long need = R[ingredient]*mid;
		need = (9*need) / 10 + ( (9*need) % 10 != 0 );
		if(Q[ingredient][index] >= need)	l = mid;
		else r = mid - 1;
	}
	return l;
}

int findMost(int ingredient, int index){
	int l = 0 , r = LIMIT2;
	while(l < r){
		int mid = (l + r)/2;
		long long need = R[ingredient]*mid;
		need = (11*need) / 10;
		if(Q[ingredient][index] <= need)	r = mid;
		else l = mid + 1;
	} 
	return l;
}

void solve(int Test){
	int ans = 0;
	event.clear();
	cin>>n>>p;
	for(int i = 1 ; i <= n ; i++)	ss[i].clear();
	for(int i = 1 ; i <= n ; i++)	cin>>R[i];
	for(int i = 1 ; i <= n ; i++)
		for(int j = 1 ; j <= p ; j++){
			cin>>Q[i][j];
			start[i][j] = findMost(i , j);
			finish[i][j] = findLeast(i , j);
			if(start[i][j] == 0)	start[i][j]++;
			if(finish[i][j] == 0)	continue;
			if(start[i][j] > finish[i][j])	continue;
			event.push_back(II(start[i][j] , ii(i , j)));
			event.push_back(II(finish[i][j] + 1, ii(-i , -j)));
		}
	sort(event.begin() , event.end());
	for(int i = 0 ; i < event.size() ; i++){
		int cur = event[i].fi;
		int ingredient = event[i].se.fi;
		int index = event[i].se.se;
		if(index > 0)	ss[ingredient].insert(ii(finish[ingredient][index] + 1 , index));
		else{
			ss[-ingredient].erase(ii(finish[-ingredient][-index] + 1 , -index));
		}
		if(i == event.size() - 1 || cur != event[i + 1].fi){
			while(true){
				int c = 0;
				for(int j = 1 ; j <= n ; j++) if(ss[j].size() > 0)	c++;
				if(c == n){
					ans++;
					for(int j = 1 ; j <= n ; j++)	ss[j].erase(ss[j].begin());
				}
				if(c < n) break;
			}
		}	
	}
	printf("Case #%d: %d\n",Test,ans);
}

int main(){
	freopen("test.inp","r",stdin);
	freopen("test.out","w",stdout);
	int Tc;
	cin>>Tc;
	for(int i = 1 ; i <= Tc ; i++)	solve(i);
}





