//
// Created by Kapil Dolas on 15-04-2017.
//

#include<stdio.h>
#include<iostream>
#include<math.h>
#include<vector>
#include<map>
#include<string>
#include<string.h>
#include<algorithm>
#include<set>
#define PI acos(-1.0)
#define SZ 26LL
#define Fi(a,n) for(int i=a;i<n;i++)
#define Fj(a,n) for(int j=a;j<n;j++)
#define Fk(a,n) for(int k=a;k<n;k++)
#define ri(a) scanf("%d",&a)
#define c(a) (a-'A')
#define rc(a) (char)('A'+a)
#define pb push_back
#define mp make_pair
using namespace std;
typedef vector<int> vi;
typedef vector<vi > vii;
typedef long long ll;
typedef vector<ll> vll;
char glob;
bool check(int ri, int ci, int rj, int cj, char str[26][26]) {
    char c='?';
    glob='?';
    Fi(ri, rj+1) Fj(ci, cj+1) {
            if(c=='?' && c!=str[i][j]) {
                c = str[i][j];
                glob = c;
                continue;
            }
            if(c!='?' && str[i][j]!='?' && str[i][j]!=c) {
                return false;
            }
        }
    return c!='?';
}
int xmax[26], ymax[26], xmin[26], ymin[26], cnt[26];
void grow(int ch, int ri, int ci, int rj, int cj, char str[26][26], int r, int c, int op) {
    glob = rc(ch);
    switch (op) {
        case 1:
            //above
            if (ri > 0 && check(ri - 1, ci, ri, cj, str)) {
                Fj(ci, cj + 1) str[ri - 1][j] = glob;
                ri--;
            }
            break;
        case 2:
        //below
        if (rj < r - 1 && check(rj, ci, rj + 1, cj, str)) {
            Fj(ci, cj + 1) str[rj + 1][j] = glob;
            rj++;
        }
            break;
        case 3:
        //left
        if (ci > 0 && check(ri, ci - 1, rj, ci, str)) {
            Fi(ri, rj + 1) str[i][ci - 1] = glob;
            ci--;
        }
            break;
        case 4:
        //right
        if (cj < c - 1 && check(ri, cj, rj, cj + 1, str)) {
            Fi(ri, rj + 1) str[i][cj + 1] = glob;
            cj++;
        }
    }
    xmin[ch]=ri;
    xmax[ch]=rj;
    ymin[ch]=ci;
    ymax[ch]=cj;
}
int main() {
    int t;
    int r, c;
    ri(t);
    char str[SZ][SZ];
    for(int T=1; T<=t; T++) {
        ri(r); ri(c);
        Fi(0, 26) {
            xmax[i] = ymax[i] = -1;
            xmin[i] = ymin[i] = 26;
            cnt[i] = 0;
        }
        Fi(0, r)
            scanf("%s", str[i]);
        Fi(0, r)
            Fj(0, c) {
                if(str[i][j]!='?') {
                    xmax[c(str[i][j])]=i;
                    xmin[c(str[i][j])]=min(i, xmin[c(str[i][j])]);
                    ymax[c(str[i][j])]=max(j, ymax[c(str[i][j])]);
                    ymin[c(str[i][j])]=min(j, ymin[c(str[i][j])]);
                    cnt[c(str[i][j])]++;
                }
            }
        int q_cnt = 0;
        Fi(0, r) Fj(0, c) {
                if(str[i][j]=='?') {
                    Fk(0, 26) {
                        if (cnt[k] > 1 && xmin[k] <= i && xmax[k] >= i && ymin[k] <= j && ymax[k] >= j) {
                            str[i][j] = rc(k);
                        }
                    }
                    if(str[i][j]=='?') q_cnt++;
                }
            }
        while (q_cnt) {
            Fi(0, 26)
                Fj(0, 25)
                   grow(i, xmin[i], ymin[i], xmax[i], ymax[i], str, r, c, 1);
            Fi(0, 26)
                Fj(0, 25)
                    grow(i, xmin[i], ymin[i], xmax[i], ymax[i], str, r, c, 2);
            Fi(0, 26)
                Fj(0, 25)
                    grow(i, xmin[i], ymin[i], xmax[i], ymax[i], str, r, c, 3);
            Fi(0, 26)
                Fj(0, 25)
                    grow(i, xmin[i], ymin[i], xmax[i], ymax[i], str, r, c, 4);
            q_cnt=0;
            Fi(0, r) Fj(0, c) {
                    if (str[i][j] == '?') q_cnt++;
                }
        }
        printf("Case #%d:\n", T);
        Fi(0, r)
            printf("%s\n", str[i]);
        fflush(stdout);
    }
    return 0;
}