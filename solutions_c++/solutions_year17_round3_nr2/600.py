#include<cstdio>
#include<cstdlib>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<algorithm>
#include<iostream>
#include<cmath>

using namespace std;

#define pb push_back
#define mp make_pair

int T,carol,james;
pair< pair<int,int>,int > e[205];

const int inf= 1e9;
int dp[2][2][750][750];

int solve(int st,int who,int ca,int ja,int w){
    if(dp[st][who][ca][ja])
	return dp[st][who][ca][ja];

    if(ca > 720 || ja > 720)
	return inf;

    if(ca == 720 && ja == 720)
	return who != st;

    if(w < carol+james && ca+ja == e[w].first.first){
	int res;
	if(e[w].second == 0)
	    res = solve(st,0,ca+e[w].first.second-e[w].first.first,ja,w+1);
	else
	    res = solve(st,1,ca,ja+e[w].first.second-e[w].first.first,w+1);

	if(who != e[w].second)
	    res++;

	return dp[st][who][ca][ja] = res;
    }

    if(who == 0)
	return dp[st][who][ca][ja] = min(solve(st,who,ca+1,ja,w),solve(st,1-who,ca,ja+1,w)+1);
    else
	return dp[st][who][ca][ja] = min(solve(st,1-who,ca+1,ja,w)+1,solve(st,who,ca,ja+1,w));
}

void read_input(){
    cin >> T;
    for(int t = 0 ; t < T ; ++t){
	cin >> carol >> james;

	for(int i = 0 ; i < carol + james ; ++i){
	    cin >> e[i].first.first >> e[i].first.second;
	    e[i].second = (i >= carol);
	}

	sort(e,e+carol+james);

	cout << "Case #" << t+1 << ": " << min(solve(0,0,0,0,0),solve(1,1,0,0,0)) << endl;

	memset(dp,0,sizeof dp);
    }
}

int main(){
    read_input();
    return 0;
}
