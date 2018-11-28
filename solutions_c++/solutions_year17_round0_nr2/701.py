#include<bits/stdc++.h>
using namespace std;

typedef long long LL;
const int N = 20;
char s[N];

int T, n, top, a[N], b[N];

bool ok(){
	for(int i=1; i<n; i++){
		if(a[i] < a[i-1]){
			return 0;
		}
	}
	return 1;
}

LL getnum(int m){
	LL x = 0;
	for(int i=0; i<m; i++){
		x = x * 10 + b[i];
	}
	return x;
}

LL solve1(){
    for(int i=0; i<n; i++){
		b[i] = a[i];
    }
    for(int i=0; i<n; i++){
        if(b[i] > b[i+1]){
			for(int j=i+1; j<n; j++){
				b[j] = 9;
			}
			b[i]--;
            for(int j=i; j>0; j--){
				if(b[j] < b[j-1]){
					b[j-1]--;
					b[j] = 9;
				}
            }
            break;
        }
    }
    if(b[0] == 0){
		return 0;
    }
    return getnum(n);
}

LL solve(){
	for(int i=0; i<n; i++){
		a[i] = s[i] - '0';
	}
	LL ret = 0;
	if(ok()){
		ret = 0;
		for(int i=0; i<n; i++){
			ret = ret * 10 + a[i];
		}
		return ret;
	}
	top = 0;
	for(int i=0; i<n; i++){
		top = top * 10 + a[i];
	}

    for(int i=0; i<n-1; i++){
		b[i] = 9;
    }
    ret = max(solve1(), getnum(n - 1));

    return ret;
}

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
	for(int t=1; t<=T; t++){
		scanf("%s", s);
		n = strlen(s);
		printf("Case #%d: %I64d\n", t, solve());
	}
	return 0;
}
