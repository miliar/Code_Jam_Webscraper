/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
 * Created By : Aditya Agarwal
 * IT, MNNIT-ALLAHABAD 
 * aditya.mnnit15@gmail.com
 _._._._._._._._._._._._._._._._._._._._._.*/


#include<bits/stdc++.h>
using namespace std;

#define MP make_pair
#define pb push_back
#define rep(i,n) for(int i=0;i<n;i++)
#define REP(i,a,b) for(int i=a;i<=b;i++)
#define PER(i,a,b) for(int i=b;i>=a;i--)
#define X first
#define Y second

 //i/o
#define inp(n) scanf("%d",&n)
#define inpl(n) scanf("%lld",&n)
#define inp2(n,m) inp(n), inp(m)
#define inp2l(n,m) inpl(n), inpl(m)


//cost
#define MOD 1000000007
#define MOD_INV 1000000006
#define MAX 100009
#define INF 999999999
#define mp make_pair
typedef long long ll;
typedef pair< pair<ll,ll>,ll > pairs;

int main(){
    int t,p=1;
    inp(t);
    while(t--){
        int r,c;
        inp2(r,c);
        char a[r+1][c+1];
        rep(i,r)
            scanf("%s",a[i]);
        char last;
        set<char> s;
        rep(i,26)
            s.insert('A'+i);
        rep(i,r){
            rep(j,c){
                if(a[i][j]!='?' && s.find(a[i][j])!=s.end())
                    s.erase(a[i][j]);
            }
        }
        rep(i,r){
            for(int j=1;j<c;j++){
                if(a[i][j]=='?')
                    a[i][j]=a[i][j-1];
            }
        }

        rep(i,r){
            for(int j=c-2;j>=0;j--){
                if(a[i][j]=='?')
                    a[i][j]=a[i][j+1];
            }
        }

        rep(j,c){
            for(int i=1;i<r;i++){
                if(a[i][j]=='?')
                    a[i][j]=a[i-1][j];
            }
        }

        rep(j,c){
            for(int i=r-2;i>=0;i--){
                if(a[i][j]=='?')
                    a[i][j]=a[i+1][j];
            }
        }
        char lol;
        set<char>::iterator it;
        int f=0;
        rep(i,r){
            rep(j,c){
                if(a[i][j]=='?'){
                    it=s.begin();
                    lol=*it;
                    s.erase(it);
                    f=1;
                    break;
            }
        }
    }
        if(f==1){
            rep(i,r){
            rep(j,c){
                a[i][j]=lol;
        }
        }
    }
        printf("Case #%d:\n",p++);
        rep(i,r){
            rep(j,c)
                cout<<a[i][j];
            cout<<endl;
        }

    }

    return 0;
}
