#include <bits\stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
int T;

map<char, int> imap;
char str1[8] = "ROYGBV";
char str[8] = "0BYGRVO";
int A[10][10];

void solve(int testi){
    int N = 0;
    char sol[1007];
    int a[8]{};
    scanf("%d",&N);
    for(int i=0; i<6; i++){
        scanf("%d",a+imap[str1[i]]);
    }
    sol[N] = 0;

    int j0 = -1;
    for(int j=1; j<7; j++){
        if (a[j]){
            sol[0] = str[j];
            a[j]--;
            j0 = j;
            break;
        }
    }
    bool good = 1;
    for(int i=1; i<N; i++){
        bool found = 0;
        for(int j=1; j<7; j++){
            if (a[j] && A[imap[sol[i-1]]][imap[str[j]]]){
                a[j]--;
                bool goodj = 1;
                for(int ii=1; ii<7 && goodj; ii++){
                    int others = 0;
                    for(int jj=1; jj<7 && goodj; jj++) if (A[ii][jj]){
                        others += a[jj];
                        if (jj==j0)
                            others++;
                    }
                    goodj &= others>=a[ii];
                }
                if (goodj){
                    sol[i]=str[j];
                    found = 1;
                    break;
                }
                else{
                    a[j]++;
                }
            }
        }
        if (!found){
            good = 0;
            break;
        }
    }
    good &= A[imap[sol[0]]][imap[sol[N-1]]];

    if (good){
        printf("Case #%d: %s\n",testi, sol);
    }
    else
        printf("Case #%d: IMPOSSIBLE\n",testi);
}

int main(){
    imap['B'] = 1;
    imap['Y'] = 2;
    imap['G'] = 3;
    imap['R'] = 4;
    imap['V'] = 5;
    imap['O'] = 6;
    for(int i=1; i<=6; i++){
        for(int j=1; j<=6; j++){
            if (!(i & j))
                A[i][j] = 1;
        }
    }
	#ifdef LOCAL_PROJECT
		freopen("d:\\src\\CppProjects\\stdin","r",stdin);
		freopen("d:\\src\\CppProjects\\stdout","w",stdout);
	#endif
	scanf("%d",&T);
	for(int testi = 1; testi<=T; testi++)
        solve(testi);
	return 0;
}
