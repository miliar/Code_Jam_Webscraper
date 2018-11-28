#include<bits/stdc++.h>
#define fr(a, b, c) for(int a = (b); a < int(c); ++a)
#define fre(i, u) for(int i = adj[u]; i != -1; i = ant[i])
#define sc(a) scanf("%d", &a)
#define sc2(a, b) scanf("%d%d", &a, &b)
#define sc3(a, b, c) scanf("%d%d%d", &a, &b, &c)
#define scs(s) scanf("%s", s)
#define msb(x) (x & -x)
#define st first
#define nd second
#define pb push_back
#define mp make_pair

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int ms = 1111;

int k, T;
char s[ms];

int main(){
	sc(T);
	fr(t, 0, T){
		scs(s);
		sc(k);
		int a = 0;
		int n = strlen(s);
		bool ok = true;
		fr(i, 0, n){
			if(!ok) break;
			if(s[i] == '-'){
				//printf("i %d j %d\n", i, i + k - 1);
				if(i + k - 1 >= n) ok = false;
				else{
					++a;
					fr(j, 0, k){
						if(s[i + j] == '+') s[i + j] = '-';
						else s[i + j] = '+';
					}
				}
			}
		}
		printf("Case #%d: ", t + 1);
		if(ok){
			printf("%d\n", a);
		}
		else{
			puts("IMPOSSIBLE");
		}
	}
	return 0;
}

