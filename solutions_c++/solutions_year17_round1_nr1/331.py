#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int maxn = 30;

char s[maxn][maxn];

int n,m;

int T;
int pos[30];

void solve(){
	int st = 0;
	for(int i = 1;i <= n;i++){
		bool flag = false;
		for(int j = 1;j <= m;j++){
			if(s[i][j] != '?') flag = true;
		}
		if(flag){
			st = i;
			break;
		}
	}
	//cout << st << endl;
	int cnt = 0;
	for(int j = 1;j <= m;j++){
		if(s[st][j] != '?'){
			pos[++cnt] = j;
		}
	}
	int l = 1;
	for(int i = 1;i <= cnt;i++){
		for(int j = l;j <= pos[i];j++){
			s[st][j] = s[st][pos[i]];
		}
		l = pos[i] + 1;
		if(i == cnt){
			for(int j = l;j <= m;j++){
				s[st][j] = s[st][pos[cnt]];
			}
		}
	}
	for(int x = st - 1;x >= 1;x--){
		bool flag = false;
		for(int j = 1;j <= m;j++){
			if(s[x][j] != '?') flag = true;
		}
		if(flag){
			cnt = 0;
			for(int j = 1;j <= m;j++){
				if(s[x][j] != '?'){
					pos[++cnt] = j;
				}
			}
			//cout << cnt << endl;
			int l = 1;
			for(int i = 1;i <= cnt;i++){
				for(int j = l;j <= pos[i];j++){
					s[x][j] = s[x][pos[i]];
				}
				l = pos[i] + 1;
				if(i == cnt){
					for(int j = l;j <= m;j++){
						s[x][j] = s[x][pos[cnt]];
					}
				}
			}
		}else{
			for(int j = 1;j <= m;j++){
				s[x][j] = s[x + 1][j];
			}
		}
	}
	for(int x = st + 1;x <= n;x++){
		bool flag = false;
		for(int j = 1;j <= m;j++){
			if(s[x][j] != '?') flag = true;
		}
		if(flag){
			cnt = 0;
			for(int j = 1;j <= m;j++){
				if(s[x][j] != '?'){
					pos[++cnt] = j;
				}
			}
			//cout << cnt << endl;
			//cout << i << "!" << endl;
			int l = 1;
			for(int i = 1;i <= cnt;i++){
			//	cout << "!!" << pos[i] << endl;
				for(int j = l;j <= pos[i];j++){
				//	cout << "!!!" << j << endl;
					s[x][j] = s[x][pos[i]];
				}
				l = pos[i] + 1;
				if(i == cnt){
					for(int j = l;j <= m;j++){
						s[x][j] = s[x][pos[cnt]];
					}
				}
			}
		}else{
			for(int j = 1;j <= m;j++){
				s[x][j] = s[x - 1][j];
			}
		}
	}
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.txt","w",stdout);
	cin >> T;
	int cas = 0;
	while(T--){
		cin >> n >> m;
		cas++;
		for(int i = 1;i <= n;i++){
			scanf("%s",s[i] + 1);
		}
		solve();
		printf("Case #%d:\n",cas);
		for(int i = 1;i <= n;i++){
			printf("%s",s[i] + 1);
			puts("");
		}
	}
	return 0;
}
