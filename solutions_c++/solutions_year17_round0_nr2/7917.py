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

const int ms = 111;

int T;

char s[ms];
char a[ms];
bool mark[ms];

int main(){
	sc(T);
	fr(t, 0, T){
		scs(s);
		int n = strlen(s);
		bool ok = false;
		memset(mark, false, sizeof mark);
		fr(i, 0, n){
			if(ok){
				a[i] = '9';
			}
			else if(mark[i]){
				a[i] = s[i] - 1;
				ok = true;
			}
			else{
				bool eq = true;
				fr(j, i + 1, n){
					if(s[j] < s[i]) eq = false;
				}
				if(eq){
					a[i] = s[i];
				}
				else{
					int p = 0;
					fr(j, i + 1, n){
						if(s[j] < s[i]){
							p = j;
							break;
						}
					}
					bool nz = false;
					fr(j, i + 1, p){
						if(s[j] > s[i])
							nz = true;
					}
					if(nz){
						for(int j = p - 1; j > i; --j){
							if(s[j] > s[i]){
								mark[j] = true;
								break;
							}
						}
						a[i] = s[i];
					}
					else{
						a[i] = s[i] - 1;
						ok = true;
					}
				}
			}
		}
		int i = 0;
		printf("Case #%d: ", t + 1);
		while(a[i] == '0') ++i;
		//printf("%s ", s);
		while(i < n) 
			printf("%c", a[i++]);
		puts("");
	}
	return 0;
}

