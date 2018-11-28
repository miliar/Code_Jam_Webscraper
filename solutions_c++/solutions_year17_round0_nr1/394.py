#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> PII;

const int MM = 1e9 + 7;
const double eps = 1e-8;
const int MAXN = 2e6 + 10;

int n, m;

void prework(){

}

void read(){

}

char s[MAXN];
int a[MAXN];

void solve(int casi){
	cout << "Case #" << casi << ": ";
	int n, k;
	scanf("%s%d", s, &k);
	n = strlen(s);
	for(int i = 0; i < n; i++)
		a[i] = (s[i] == '-') ? 0 : 1;
	int cnt = 0;
	for(int i = 0; i <= n - k; i++)
		if (a[i] == 0){
			cnt++;
			for(int j = 0; j < k; j++)
				a[i + j] = 1 - a[i + j];
		}
	int flag = 1;
	for(int i = 0; i < n; i++)
		if (a[i] != 1)
			flag = 0;
	if (flag)
		cout<<cnt<<endl;
	else
		puts("IMPOSSIBLE");
}

void printans(){

}


int main(){
//	std::ios::sync_with_stdio(false);
	prework();
	int T = 1;
	cin>>T;
	for(int i = 1; i <= T; i++){
		read();
		solve(i);
		printans();
	}
	return 0;
}


