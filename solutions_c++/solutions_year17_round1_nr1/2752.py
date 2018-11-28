#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pb push_back
#define mp make_pair

int gcd(int a, int b){
	if(b == 0) return a;
	return gcd(b, a%b);
}

const int INFI = 1e9+1e9;
const ll INFLL = 1e18+100;

char s[105][105];

int xx[500], yy[500];

void solve(int t){
	memset(xx, 0, sizeof(xx));
	memset(yy, 0, sizeof(yy));
	memset(s, 0, sizeof(s));

	int R, C;
	cin >> R >> C;
	for(int i=1;i<=R;i++){
		cin >> s[i]+1;
	}

	for(int i=1;i<=R;i++){
		for(int j=1;j<=C;j++){
			if(s[i][j] != '?'){
				xx[s[i][j]] = 1;
				yy[s[i][j]] = 1;
			}
		}
	}

	for(int x=1;x<=R*C;x++){
		for(int i=1;i<=R;i++){
			for(int j=1;j<=C;j++){
				if(s[i][j] == '?'){
					if('A' <= s[i][j-1] && s[i][j-1] <= 'Z'){
						int yy1 = 0;
						int yy2 = 0;
						for(int l=i;l<=R;l++){
							if(s[l][j-1] == s[i][j-1]) yy2 = l;
							else break;
						}

						for(int l=i;l>=1;l--){
							if(s[l][j-1] == s[i][j-1]) yy1 = l;
							else break;
						}


						int num = 0;
						for(int l=yy1;l<=yy2;l++){
							if(s[l][j] == '?') num++;
						}

						if(num == yy[s[i][j-1]]){
							for(int l=yy1;l<=yy2;l++){
								s[l][j] = s[i][j-1];
							}
							xx[s[i][j-1]]++;
							continue;
						}
					}
					if('A' <= s[i][j+1] && s[i][j+1] <= 'Z'){
						int yy1 = 0;
						int yy2 = 0;
						for(int l=i;l<=R;l++){
							if(s[l][j+1] == s[i][j+1]) yy2 = l;
							else break;
						}

						for(int l=i;l>=1;l--){
							if(s[l][j+1] == s[i][j+1]) yy1 = l;
							else break;
						}


						int num = 0;
						for(int l=yy1;l<=yy2;l++){
							if(s[l][j] == '?') num++;
						}

						if(num == yy[s[i][j+1]]){
							for(int l=yy1;l<=yy2;l++){
								s[l][j] = s[i][j+1];
							}
							xx[s[i][j+1]]++;
							continue;
						}
					}
					if('A' <= s[i-1][j] && s[i-1][j] <= 'Z'){
						int xx1 = 0;
						int xx2 = 0;
						for(int l=j;l<=C;l++){
							if(s[i-1][l] == s[i-1][j]) xx2 = l;
							else break;
						}

						for(int l=j;l>=1;l--){
							if(s[i-1][l] == s[i-1][j]) xx1 = l;
							else break;
						}



						int num = 0;
						for(int l=xx1;l<=xx2;l++){
							if(s[i][l] == '?') num++;
						}

						if(num == xx[s[i-1][j]]){
							for(int l=xx1;l<=xx2;l++){
								s[i][l] = s[i-1][j];
							}
							yy[s[i-1][j]]++;
							continue;
						}
					}
					if('A' <= s[i+1][j] && s[i+1][j] <= 'Z'){
						int xx1 = 0;
						int xx2 = 0;
						for(int l=j;l<=C;l++){
							if(s[i+1][l] == s[i+1][j]) xx2 = l;
							else break;
						}

						for(int l=j;l>=1;l--){
							if(s[i+1][l] == s[i+1][j]) xx1 = l;
							else break;
						}

						int num = 0;
						for(int l=xx1;l<=xx2;l++){
							if(s[i][l] == '?') num++;
						}

						if(num == xx[s[i+1][j]]){
							for(int l=xx1;l<=xx2;l++){
								s[i][l] = s[i+1][j];
							}
							yy[s[i+1][j]]++;
							continue;
						}
					}
				}

			}
		}
	}

	printf("Case #%d:\n", t);

	for(int i=1;i<=R;i++){
		for(int j=1;j<=C;j++) cout << s[i][j];
		cout << endl;
	}
}

int main(){
	int T;
	cin >> T;
	for(int t=1;t<=T;t++) solve(t);
}