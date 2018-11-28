#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;
typedef long long ll;
typedef vector<ll> vi;
typedef pair<ll, ll> ii;
typedef vector<ii> vii;
#define pb push_back
#define mp make_pair
#define INF LLONG_MAX
char grid[30][30];
int main() {

    freopen("cjinput.txt", "r", stdin);
    freopen("cjoutput.txt", "w", stdout);

    int t;
    cin>>t;
    int r,c,f;
    char s;
    int tot=t;
    while(t--) {
        cin>>r>>c;
        f=-1;
        //s='.';
        vector<int> row(r,-1);
        for(int i=0;i<r;i++) {
            for(int j=0;j<c;j++) {
                cin>>s;
                if(row[i]==-1&&s!='?') {
                    row[i]=j;
                }
                grid[i][j]=s;
            }
            if(f==-1&&row[i]!=-1) {
                f=i;
            }
        }

        for(int i=0;i<r;i++) {
            if(row[i]!=-1) {
                //cout<<row[i]<<endl;
                int tmp=row[i];
                for(int j=row[i];j>=0;j--) {
                    if(grid[i][j]=='?') {
                        grid[i][j]=row[i];
                    }else {
                        row[i]=grid[i][j];
                    }
                }
                row[i]=tmp;
                for(int j=row[i];j<c;j++) {
                    //cout<<i<<" "<<j<<endl;
                    if(grid[i][j]=='?') {
                        grid[i][j]=row[i];
                    }else {
                        row[i]=grid[i][j];
                    }
                }
            }
        }


        if(f!=-1) {
            for(int i=f;i>=0;i--) {
            if(row[i]==-1) {
                for(int j=0;j<c;j++) {
                    grid[i][j]=grid[f][j];
                }
            }
            }

            for(int i=f;i<r;i++) {
            if(row[i]==-1) {
                for(int j=0;j<c;j++) {
                    grid[i][j]=grid[f][j];
                }
            }else {
                f=i;
            }
            }
        }
        
        cout<<"Case #"<<tot-t<<":"<<endl;
        for(int i=0;i<r;i++) {
            for(int j=0;j<c;j++) {
                cout<<grid[i][j];
            }
            cout<<endl;
        }

    }

    return 0;
}