/*@author:abhi2110*/
#include <cstdio>
#include <queue>
using namespace std;
#define TC int tc; scanf("%d",&tc); while(tc--)
#define sii(i,j) scanf("%d%d",&i,&j)
#define si(i) scanf("%d",&i)
#define sl(i) scanf("%lld",&i)
#define ss(i) scanf("%s",i)
#define m0(a) memset(a,0,sizeof(a))
#define m1(a) memset(a,-1,sizeof(a))
#define pb push_back
#define mp make_pair
#define clk 1.0*clock()/CLOCKS_PER_SEC
#define FILEIO(x) freopen(#x ".in","r",stdin);freopen(#x ".out","w",stdout);
#define FILEIOS freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long int ll;
char A[27][27];
int main(){
    FILEIOS
    int cas=1,r,c;
    TC{
        sii(r,c);
        int _cnt[r+1];
        for(int i=0;i<r;i++)
            ss(A[i]);
        for(int i=0;i<r;i++){
            int cnt=0;
            queue<char> see;
            for(int j=0;j<c;j++){
                if(A[i][j] == '?')  continue;
                else{
                        see.push(A[i][j]);
                        cnt++;
                    }
            }
            _cnt[i]=cnt;
            if(cnt == 0 && i >0 && _cnt[i-1]!=0){
                for(int k=0;k<c;k++)    A[i][k]=A[i-1][k];
                _cnt[i]=_cnt[i-1];
            }
            else{
                    char t=see.front();
                    see.pop();
                for(int k=0;k<c;k++){
                    if(A[i][k] == '?' ) A[i][k]=t;
                    else if(A[i][k] != '?' && A[i][k] != t){
                            t=see.front();
                            see.pop();
                    }
                }
            }
        }
        for(int i=r-2;i>=0;i--){
                if(_cnt[i]==0 && _cnt[i+1]!=0){
                for(int j=0;j<c;j++) A[i][j]=A[i+1][j];
                _cnt[i]=_cnt[i+1];
                }
        }
        printf("Case #%d:\n",cas++);
        for(int i=0;i<r;i++)
            printf("%s\n",A[i]);

    }
	return 0;
}
