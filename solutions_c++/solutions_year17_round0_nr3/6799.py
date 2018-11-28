//----------------------JUGNU:LET YOUR LIGHT SHINE---------------------------//
#include <bits/stdc++.h>
#define ll long long int
#define ld long double
#define pb push_back
#define pf push_front
#define sz size
#define mk make_pair
#define ln length
#define fr(i,a,b) for(i=a;i<b;i++)
#define fre(i,a,b) for(i=a;i<=b;i++)
#define frr(i,a,b) for(i=a;i>=b;i--)
#define sc(a) scanf("%d", &a)
#define sm(a, b) scanf("%d%d", &a, &b)
#define pr(a) printf("%d\n", a)
#define pm(a, b) printf("%d %d\n", a, b)
#define isset(x,i) ((x>>i)&1)
#define MAXN 1005
#define MOD 1000000007LL
#define fastScan ios_base::sync_with_stdio(0); cin.tie(NULL);

#define trace1(x)       cerr << #x << " : " << x << endl;
#define trace2(x, y)    cerr << #x << " : " << x << " | " << #y << " : " << y << endl;
#define trace3(x, y, z) cerr << #x << " : " << x << " | " << #y << " : " << y << " | " << #z << " : " << z << endl;
#define cline cout << "----------------------" << endl;
using namespace std;

bool ocupied[MAXN];
int ls[MAXN], rs[MAXN];
pair<int, int> result;

int main()
{
	int i, j, t, n, m, k, l, r, temp, mini, maxi, flag, cnt, test, prev, next, index;
	scanf("%d", &test);
	fre(t, 1, test){
		scanf("%d%d", &n, &k);
		ocupied[0] = ocupied[n + 1] = true;
		fre(i, 1, n) ocupied[i] = false;
		fre(i, 1, k){
			prev = 0;
			fre(j, 1, n){
				if(!ocupied[j]) ls[j] = j - prev - 1;
				else prev = j;
			}
			next = n + 1;
			frr(j, n, 1){
				if(!ocupied[j]) rs[j] = next - j - 1;
				else next = j;
			}
			result = mk(-MAXN, -MAXN);
			fre(j, 1, n){
				if(!ocupied[j]){
					mini = min(ls[j], rs[j]);
					maxi = max(ls[j], rs[j]);
					if(mini > result.first){
						result = mk(mini, maxi);
						index = j;
					}
					else if(mini == result.first){
						if(maxi > result.second){
							result = mk(mini, maxi);
							index = j;
						}
					}	
				}
			}
			// trace2(i, index);
			ocupied[index] = true;
		}
		printf("Case #%d: %d %d\n", t, max(ls[index], rs[index]), min(ls[index], rs[index])) ;
	}
return 0;
}