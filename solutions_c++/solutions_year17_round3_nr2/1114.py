#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <iostream>
#include <vector>
#include <set>
#define rep(i,a,b) for (int i = (a); i <= (b); ++i)
#define rep(i,a,b) for (int i = (a); i <= (b); ++i)
typedef long long ll;
using namespace std;
const int N = 2010;
const int L = 1440;
struct node{
    int x,y;
}a[N],b[N];
int k, n, m, ans, sum[3];
int c[N];
string s;
int check(){
    return 0;
}
void dfs(int k){
    int h, lak;
    if (k > 1400){
        h = check();
        ans = min(ans, h);
        return ;
    }
    lak = k;
    if (c[k] != 0){
        k++;
        while (k <= L && c[k]<=0)
            k++;
        dfs(k+1);
        return ;
    }
    while (k <= L && c[k] == 0)
        k++;
    int temp1,temp2;
    if (k - lak <= 720-sum[c[k]]){
        temp1 = c[k];
        c[lak] = c[k];
        c[k] = 0;
        sum[c[k]]+=k-lak;
        k++;
        
        while (k <= L && c[k] ==0)
            k++;
        dfs(k+1);
        sum[c[k]]-=k-lak;
        
    }else{
        c[lak] = 3-c[k];
        c[k-(720-sum[c[k]])] = c[k];
        sum[3-c[k]] += k-lak-(720-sum[c[k]]);
        sum[c[k]] = 720;
        
        k++;
        while (k <= L && c[k] ==0)
            k++;
        dfs(k+1);
    }
}
int main() {
    freopen("/users/Mr.ZY/Documents/Program/GCJ2017-1C-B/1.txt","r",stdin);
    freopen("/users/Mr.ZY/Documents/Program/GCJ2017-1C-B/B.txt","w",stdout);
    int ttt;
    cin >> ttt;
    rep (sss,1,ttt){
        memset(a,0,sizeof(a));
        memset(c,0,sizeof(c));
        cin >> n >> m;
        sum[1] = sum[2] = 0;
        rep (i,1,n){
            cin >> a[i].x >> a[i].y;
            sum[1] += a[i].y-a[i].x;
            c[a[i].x] = 1;//C start
            c[a[i].y] = -1;//C end
        }
        if (n==2 && a[1].x >= a[2].y)
            swap(a[1],a[2]);
        
        rep (i,1,m){
            cin >> b[i].x >> b[i].y;
            sum[2] += b[i].y-b[i].x;
            c[b[i].x] = 2;//C start
            c[b[i].y] = -2;//C end
        }
        if (m==2 && b[1].x >= b[2].y)
            swap(b[1],b[2]);
        ans = 2;
        if (n > 1 || m > 1){
            if (n==0){
                if (b[2].y-b[1].x > 720 && b[1].y+1440-b[2].x > 720){
                    printf("Case #%d: 4\n",sss);
                    continue;
                }
                printf("Case #%d: 2\n",sss);
                continue;
            }else if (m==0){
                if (a[2].y-a[1].x > 720 && a[1].y+1440-a[2].x > 720){
                    printf("Case #%d: 4\n",sss);
                    continue;
                }
                printf("Case #%d: 2\n",sss);
                continue;
            }else   if (n==2&&m==1){
                if (b[1].x>=a[1].y && b[1].y<=a[2].x && (a[1].y+1440-a[2].x) > 720){
                    printf("Case #%d: 4\n",sss);
                    continue;
                }
                if (a[2].y-a[1].x>720 && a[2].x-a[1].y<720 ){
                    printf("Case #%d: 4\n",sss);
                    continue;
                }
                printf("Case #%d: 2\n",sss);
                continue;
            }else if (n==1&&m==2){
                if (a[1].x>=b[1].y && a[1].y<=b[2].x && (b[1].y+1440-b[2].x)<=720){
                    printf("Case #%d: 4\n",sss);
                    continue;
                }
                if (b[2].y-b[1].x>720 && b[2].x-b[1].y<720){
                    printf("Case #%d: 4\n",sss);
                    continue;
                }
                printf("Case #%d: 2\n",sss);
                continue;
            }else{
                if (a[2].y <= b[1].x || b[2].y<=a[1].x){
                    if (a[2].y-a[1].x<=720 && b[2].y-b[1].x<=720){
                        printf("Case #%d: 2\n",sss);
                        continue;
                    }
                }
                if (b[1].x>=a[1].y && a[2].x>=b[2].y){
                    if (b[2].y-b[1].x<=720 && (a[1].y+1440-a[2].x)<=720){
                        printf("Case #%d: 2\n",sss);
                        continue;
                    }
                }
                if (a[1].x>=b[1].y && b[2].x>=a[2].y){
                    if (a[2].y-a[1].x<=720 && (b[1].y+1440-b[2].x)<=720){
                        printf("Case #%d: 2\n",sss);
                        continue;
                    }
                }
                printf("Case #%d: 4\n",sss);
                continue;
            }
        }
        
        
        printf("Case #%d: 2\n",sss);
        //dfs(0);
        //cout << ans << endl;
        
    }
    return 0;
}
