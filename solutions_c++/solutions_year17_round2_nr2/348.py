#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>
#include <cstring>
#include <set>
#include <map>
using namespace std;

int N,D;
int R,O,Y,G,B,V;
int c[33];
int x[33];
int res[1111];
char col[3];
char altC[3];
int alt[33];
void printres(){
	for (int i=0;i<N;i++){
		printf("%c",col[res[i]]);

		while (alt[res[i]]){
			alt[res[i]]--;
			printf("%c", altC[res[i]]);
			printf("%c", col[res[i]]);
		}
	}
	cout<<endl;
}

bool coba(int st){
	x[0] = c[0];
	x[1] = c[1];
	x[2] = c[2];

	if (x[st] == 0)
		return false;
	//cout<<"TES "<<N<<endl;
	int p = N;
	int now = st;
	for (int i=0;i<p;i++){
		res[i]=now;
		x[now]--;
		//cout<<now<<": "<<x[0]<<" "<<x[1]<<" "<<x[2]<<endl;
		int nx = 0;
		int next= -1;
		for (int j=0;j<3;j++)
			if (x[j] > 0 && j != now && nx < x[j]){
				nx = x[j];
				next = j;
			}
		
		if (x[st] > 0 && now != st && x[st] >= nx){
			next = st;
		}

		if (i == p-1)
			break;

		if (next == -1)
			return false;
		now = next;
	}
	//cout<<now<<endl;
	if (now == st)
		return false;
	printres();
	return true;
}

void solve(){
	scanf("%d", &N);
	scanf("%d%d%d%d%d%d",&c[0],&O,&c[1],&G,&c[2],&V);

	c[0] -= G;
	alt[0] = G;
	c[1] -= V;
	alt[1] = V;
	c[2] -= O;
	alt[2] = O;

	col[0] = 'R';
	col[1] = 'Y';
	col[2] = 'B';

	altC[0] = 'G';
	altC[1] = 'V';
	altC[2] = 'O';
	

	if (c[0] < 0 || c[1] < 0 || c[2] < 0){
		cout<<"IMPOSSIBLE"<<endl;
		return;
	}

	N = N - 2*(G + V + O);
	
	if (N == 0){
		int ct = 0;
		int x = 0;
		for (int i=0;i<3;i++)
			if (alt[i] > 0) {
				x = i;
				ct++;
			}
		if (ct > 1){
			cout<<"IMPOSSIBLE"<<endl;
			return;
		}
		while (alt[x]--){
			printf("%c%c", col[x], altC[x]);
		}
		cout<<endl;
		return;
	}

	if (coba(0)) return;
	if (coba(1)) return;
	if (coba(2)) return;
	cout<<"IMPOSSIBLE"<<endl;
}

int main(){
	int T;
	scanf("%d",&T);
	for (int tt=1;tt<=T;tt++){
		printf("Case #%d: ",tt);
		solve();
	}
}

