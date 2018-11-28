#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long long LL;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

#ifdef DEBUG
    #define cek(x) cout<<x
#else
    #define cek(x) if(false){}
#endif // DEBUG

#define fi first
#define se second
#define INF 1000000000
#define INFLL 1000000000000000000LL
#define EPS 1e-9
#define PI acos(-1.0)
#define pb push_back
#define TC() while(tc--)
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORN(i,n) for(int i=0;i<=n;i++)
#define REP(i,a,b) for(int i=a;i<b;i++)
#define REPN(i,a,b) for(int i=a;i<=b;i++)
#define reset(a,b) memset(a,b,sizeof(a))
#define sci(x) scanf("%d",&x)
#define scs(x) scanf("%s",&x)

int main(void){
    freopen("C:/Users/Rideasnail/Downloads/A-large.in","r",stdin);
    freopen("C:/Users/Rideasnail/Downloads/out.txt","w",stdout);

    int tc;
    sci(tc);

    FOR(x,tc)
    {
        int r, c;
        cin >> r;
        cin >> c;
        string done = "";

        char dat[r][c];
        for(int i=0;i<r;i++)
        for(int ii=0;ii<c;ii++){
            cin >> dat[i][ii];
        }

        for(int i=0;i<r;i++){
            for(int ii=0;ii<c;ii++){
                if(dat[i][ii]!='?' && done.find(dat[i][ii])==string::npos){
                    char myChar = dat[i][ii];

                    int colStart = ii;
                    int colEnd = ii;
                    while(colStart>0 && dat[i][colStart-1]=='?') colStart--;
                    while(colEnd<c-1 && dat[i][colEnd+1]=='?') colEnd++;

                    int rowStart = i;
                    int rowEnd = i;
                    bool rowValid = true;
                    while(rowStart>0 && rowValid){
                        for(int iii=colStart;iii<=colEnd;iii++){
                            if(dat[rowStart-1][iii]!='?'){
                                rowValid = false;
                                break;
                            }
                        }
                        if(rowValid){
                            rowStart--;
                        }
                    }

                    rowValid = true;
                    while(rowEnd<r-1 && rowValid){
                        for(int iii=colStart;iii<=colEnd;iii++){
                            if(dat[rowEnd+1][iii]!='?'){
                                rowValid = false;
                                break;
                            }
                        }
                        if(rowValid){
                            rowEnd++;
                        }
                    }


                    for(int iii=rowStart;iii<=rowEnd;iii++){
                        for(int iv=colStart;iv<=colEnd;iv++) {
                            dat[iii][iv] = myChar;
                        }
                    }

                    done = done + dat[i][ii];
                }
            }
        }



        cout << "Case #" << x+1 << ": " << endl;
        for(int i=0;i<r;i++){
            for(int ii=0;ii<c;ii++){
                    cout << dat[i][ii];
            }
            cout << endl;
        }
    }


    return 0;
}
