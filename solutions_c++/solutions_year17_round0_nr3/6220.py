#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair

typedef long long int ll;
typedef vector< pair<int,int> > vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<long long int> vll;
typedef pair<int,int> pii;

const ll INF= ll (1e18);
const int MOD= 1e9+7;


int Max(int a,int b){
    if(a<b)return b;return a;
}

int Min(int a,int b){
    if(a<b)return a;return b;
}

int arr[10000001];

int left(int n){
    int i;
    for(i=n-1;;i--)
        if(arr[i]==1)
            break;
    return n-i-1;
}

int right(int n){
    int i;
    for(i=n+1;;i++)
        if(arr[i]==1)
            break;
    return i-n-1;
}

int main(void){
    int t;scanf("%d",&t);
    for(int T=1;T<=t;T++){
        int n,k;
        scanf("%d %d",&n,&k);
        for(int i=1;i<=n;i++)arr[i]=0;
        arr[0]=1;arr[n+1]=1;

        int LL,RR;
        for(int N=1;N<=k;N++){
            int max=-1,M,mmax=-1;
        for(int i=1;i<=n;i++)
            if(arr[i]==0){
                int L=left(i);
                int R=right(i);
                if(max<=Min(L,R)){
                    if(max<Min(L,R)){
                        max=Min(L,R);
                        LL=L;RR=R;
                        M=i;
                    }
                    else{
                        if(mmax<Max(L,R)){
                            mmax=Max(L,R);
                            max=Min(L,R);
                            LL=L;RR=R;
                            M=i;
                    }

                }
            }
            }
        arr[M]=1;
    }
    printf("Case #%d: %d %d\n",T,Max(LL,RR),Min(LL,RR));
}return 0;
}
