#include<fstream>
#include<math.h>
#include<algorithm>
#include<memory.h>
#include<string>
#include<vector>
#include<stdio.h>
#include<map>
#include<set>
#include<bitset>
#include<sstream>
#define rep(i,n) for(i=1;i<=n;i++)
#define repm(i,b,n) for(i=b;i<=n;i++)
#define repr(i,n) for(i=n;i>=1;i--)
#define repmr(i,n,b) for(i=n;i>=b;i--)
#define pr pair<LL,LL>
#define CL(a) memset(a,0,sizeof(a))
#define MAX_INT 2147483647
#define MOD 1000002013
using namespace std;
ifstream cin("A.in");
ofstream cout("A.out");
typedef long long LL;
int n,m;
int a[200];
int main(){

    int i,j,k,l,_;
    int test;
    cin>>test;
    //FILE * fp;
    //fp = fopen("A.out","w");
    rep(_,test){
        int ans = 0;
        cin>>n;
        cin>>m;
        rep(i,n){
            cin>>a[i];
        }
        if(m == 2){
            int cji = 0,cou = 0;
            rep(i,n){
                if(a[i] % 2){
                    cji++;
                }
                else cou++;
            }
            ans = cou + (cji + 1) / 2;
        }
        else if(m == 3){
            int c0 = 0, c1 = 0,c2 = 0;
            rep(i,n){
                if(a[i] % 3 == 0){
                    c0++;
                }
                else if(a[i] % 3 == 1) c1++;
                else c2++;
            }
            ans = c0;
            if(c2 > c1){
                ans+=c1;
                ans+= ceil((c2-c1) / 3.0);
            }
            else{
                ans+=c2;
                ans+= ceil((c1-c2) / 3.0);
            }
        }
        else{
            int c0 = 0, c1 = 0, c2 = 0, c3 = 0;
            rep(i,n){
                if(a[i] % 4 == 0){
                    c0++;
                }
                else if(a[i] % 4 == 1) c1++;
                else if(a[i] % 4 == 2) c2++;
                else{
                    c3++;
                }
            }
            ans = c0;
            ans += c2/2;
            c2 = c2 % 2;
            int minn = min(c1,c3);
            ans += minn;
            c1 -= minn;
            c3 -= minn;
            if(c2 == 0){
                if(c1 == 0){
                    ans += ceil((c3) / 4.0);
                }
                else{
                    ans += ceil((c1) / 4.0);
                }
            }
            else{
                if(c1 == 0){
                    if(c3 >= 2){
                        ans += 1;
                        c3 -= 2;
                        ans += ceil((c3) / 4.0);
                    }
                    else if(c3 == 0){
                        ans++;
                    }
                    else{
                        ans += ceil((c3) / 4.0);
                    }

                }
                else{
                    if(c1 >= 2){
                        ans += 1;
                        c1 -= 2;
                        ans += ceil((c1) / 4.0);
                    }
                    else if(c1 == 0){
                        ans++;
                    }
                    else{
                        ans += ceil((c1) / 4.0);
                    }
                }
            }

        }
        cout<<"Case #"<<_<<": "<<ans<<endl;
    }
    return 0;
}

