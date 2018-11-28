#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <cstdlib>
#include <queue>
#include <map>
#include <stack>
#define maxn 109
#define maxm 100000
using namespace std;
const long long INF = 1e18;
int n, R, RY, Y, YB, B, RB;
int a[5];
string ans;
stack<string>G[10];
bool ban[500][500];

bool checkans(){
	ban['O']['R'] = ban['O']['Y'] = 1;
	ban['Y']['G'] = ban['B']['G'] = 1;
	ban['R']['V'] = ban['B']['V'] = 1;
	int sz = ans.size();
	if(sz != n)
		return 0;
	for(int i = 0; i < n; i++){
		int a = ans[i];
		int b = ans[(i + 1) % n];
		if(a == b)
		 	return 0;
		if(ban[a][b] || ban[b][a])
			return 0;
	}
	return 1;
}

int last;
void addans(int x){
	if(G[x].empty())
		return;
	a[x]--;
	ans += G[x].top();
	G[x].pop();
	last = x;
}
bool solve2(int cur){
	int n = a[0] + a[1] + a[2] - 1;
	if(n == 0)
	 	return 0;
	 addans(cur);
	 

	
	last = cur;
	for(int i = 0; i < n ; i++){
		if(last == 0){
			if(a[1] > a[2]){
				addans(1);
			}
			else if(a[1] < a[2]){
				addans(2);
			}
			else if(a[1] == cur){
				addans(1);
			}
			else
				addans(2);
		}
		else if(last == 1){
			if(a[0] > a[2]){
				addans(0);
			}
			else if(a[0] < a[2]){
				addans(2);
			}
			else if(a[0] == cur){
				addans(0);
			}
			else
				addans(2);
		}
		else{
			if(a[1] > a[0]){
				addans(1);
			}
			else if(a[1] < a[0]){
				addans(0);
			}
			else if(a[1] == cur){
				addans(1);
			}
			else
				addans(0);
		}
		//cout << ans << endl;
	}
	if(checkans())
		return 1;
	else
		return 0;
	
}

void getans1(char a, char b){
	for(int i = 1;i <= n; i++){
		if(i & 1)
			ans.push_back(a);
		else
			ans.push_back(b);
	}
}

void getstring(int cnt, char a, char b, int pos){
	string S = "";
	S.push_back(b);
	for(int i = 0; i < cnt; i++){
		S.push_back(a);
		S.push_back(b);
	}
	G[pos].push(S);
}

bool solve(){
	ans = "";
	for(int i = 0; i < 3; i++)
	while(!G[i].empty())
		G[i].pop();
	
	if(RY){
	if(RY == B){
		if(RY + B == n){
			getans1('B', 'O');
			return 1;
		}
		else{
			return 0;
		}
	}
	if(B < RY + 1){
		return 0;
	}
	}
	
	if(YB){
	if(YB == R){
		if(YB + R == n){
			getans1('R', 'G');
			return 1;
		}
		return 0;
	}
	if(R < YB + 1){
		return 0;
	}
	}
	
	if(RB){
	if(RB == Y){
		if(RB + Y == n){
			getans1('Y', 'V');
			return 1;
		}
		else{
			return 0;
		}
	}
	if(Y < RB + 1)
		return 0;
	}
	
	a[0] = a[1] = a[2] = 0;
	a[0] = R - YB;
	a[1] = Y - RB;
	a[2] = B - RY;
	
	//cout << a[0] << " " << a[1] << " " << a[2] << endl;

	
	if(YB) getstring(YB, 'G', 'R', 0);
	if(RB) getstring(RB, 'V', 'Y', 1);
	if(RY) getstring(RY, 'O', 'B', 2);
	
	//cout << YB << endl;
	for(int i = 0; i < R - (YB > 0) * (YB + 1); i++)
		G[0].push(string("R"));
		
	for(int i = 0; i < Y - (RB > 0) * (RB + 1); i++)
		G[1].push(string("Y"));
		
	for(int i = 0; i < B - (RY > 0) * (RY + 1); i++)
		G[2].push(string("B"));
	
	//cout << G[0].size() << " " << G[1].size() << " " << G[2].size() << endl;
	
	if(a[0]){
		if(solve2(0))
			return 1;
		else 
			return 0;
	}
	else if(a[1]){
		if(solve2(1))
			return 1;
		else 
			return 0;
	}
	else{
		if(solve2(2))
			return 1;
		else 
			return 0;
	}
}

int main(){
	int cot = 1;
	freopen("/Users/fengweiming/ProgramContest/GoogleCodeJam2017/Round1B/A.in", "r", stdin);
	freopen("/Users/fengweiming/ProgramContest/GoogleCodeJam2017/Round1B/A.out", "w", stdout);
	int tt;
	scanf("%d", &tt);
	while(tt--){
		cin >> n >> R >> RY >> Y >> YB >> B >> RB;
		if(!solve())
			printf("Case #%d: IMPOSSIBLE\n", cot++);
		else{
			printf("Case #%d: ", cot++);
			cout << ans << endl;
		}
	}
	return 0;
}
