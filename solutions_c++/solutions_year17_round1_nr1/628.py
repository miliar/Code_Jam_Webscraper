/* Bismillahir Rahmanir Rahim */

#include <bits/stdc++.h>

#define rep(i, n)	for(int i=0;i<n;i++)
#define repn(i, n)	for(int i=1;i<=n;i++)
#define set(i, n)	memset(i, n, sizeof(i))

#define pb	push_back

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

const int N = 30;

string mat[N];
int n, m;

int main(){
    int tc, cas=1;
    scanf("%d", &tc);
    while(tc--){
        scanf("%d %d", &n, &m);
        rep(i, n) cin >> mat[i];
        map<char, int>used;
        rep(i, n){
            rep(j, m){
                if(mat[i][j] == '?' || used[mat[i][j]]) continue;
                used[mat[i][j]] = 1;
                int s = j, e = j;
                for(int k=j-1;k>=0;k--){
                    if(mat[i][k] != '?') break;
                    s = k;
                }
                for(int k=j+1;k<m;k++){
                    if(mat[i][k] != '?') break;
                    e = k;
                }
                for(int k=s;k<=e;k++) mat[i][k] = mat[i][j];
                for(int k=i-1;k>=0;k--){
                    bool flag = true;
                    for(int f=s;f<=e;f++) if(mat[k][f] != '?') flag = false;
                    if(!flag) break;
                    for(int f=s;f<=e;f++) mat[k][f] = mat[i][j];
                }
                for(int k=i+1;k<n;k++){
                    bool flag = true;
                    for(int f=s;f<=e;f++) if(mat[k][f] != '?') flag = false;
                    if(!flag) break;
                    for(int f=s;f<=e;f++) mat[k][f] = mat[i][j];
                }
            }
        }
        printf("Case #%d:\n", cas++);
        rep(i, n) cout << mat[i] << endl;
    }
	return 0;
}

