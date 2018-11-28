#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<climits>
#include<cmath>
#include<utility>
#include<set>
#include <queue>
#define ull unsigned long long
#define ll long long
#define pii pair<int,int>
#define pb(x) push_back(x)
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%lld",&x)
#define M(x,i) memset(x,i,sizeof(x))
#define F(i,a,n) for(int i=(a);i<(n);++i)
#define FD(i,a,n) for(int i=(a);i>=(n);--i)
using namespace std;
vector<string> a(30);
int main()
{
    freopen("inp.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t;
    cin>>t;
    F(k,1,t+1){
        int r,c;

        cin>>r>>c;
        F(i,0,r){
            cin>>a[i];
        }

        F(i,0,r){

            char ch = 'x';
            F(j,0,c){
                if(a[i][j]!='?'){
                    ch = a[i][j];
                } else if(a[i][j] == '?' && ch !='x'){
                    a[i][j] = ch;
                }
            }

            ch = 'x';
            FD(j,c-1,0){
                if(a[i][j]!='?'){
                    ch = a[i][j];
                } else if(a[i][j] == '?' && ch !='x'){
                    a[i][j] = ch;
                }
            }
        }

        /*cout<<endl;
        F(i,0,r)cout<<a[i]<<endl;
        cout<<endl;*/

        F(p,0,r){

            F(i,0,r-1){
                if(a[i][0] != '?')continue;
                F(j,0,c){
                    if(a[i+1][j] != '?'){
                        a[i][j] = a[i+1][j];
                    }
                }
            }

            
            F(i,1,r){
                if(a[i][0] != '?')continue;
                F(j,0,c){
                    if(a[i-1][j] != '?'){
                        a[i][j] = a[i-1][j];
                    }
                }
            }
        }

        cout<<"Case #"<<k<<": "<<endl;
        F(i,0,r)cout<<a[i]<<endl;
    }
}
            
