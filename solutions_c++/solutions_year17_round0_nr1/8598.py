#include <iostream>
#include <string.h>
using namespace std;
const int INF = 20000;
int h;

int flips(int a[], int M, int N, int want) {
    int s[M];
    for(int i=0; i<M; ++i)
        s[i] = 0;
    int sum=0, ans=0;
    for(int i=0; i<M; ++i)
    {
        s[i] = (a[i]+sum)%2 != want;
        sum += s[i] - (i>=N-1?s[i-N+1]:0);
        ans += s[i];
        if(i>M-N and s[i]!=0) return INF;
    }
    return ans;
}


int main() {
    int t;
    char s[1000];
    int a[1000];
    int M, N;
    freopen("A-large.in","r",stdin);
    
       cin>>t;
    for(int l=0;l<t;l++)
    {
        
        
        //cout<<t;
        scanf("%s", s);
        scanf("%d", &N);
        
        M = strlen(s);
        //  cout<<M<<endl;
        
        for(int i = 0 ; i < M ; i++)
        {
            if(s[i]=='-')
                a[i]=0;
            else if(s[i]=='+')
                a[i]=1;
        }
        //  printf("%d flips to 1\n",flips(a, M, N, 1));
        h = flips(a,M,N,1);
        if(h==INF)
            printf("Case #%d: IMPOSSIBLE\n",l+1);
        
        else  printf("Case #%d: %d\n",l+1,flips(a, M, N, 1));
        
        
               // memset(s, 0, sizeof(s));
    }
    freopen("output_file_name.out","w",stdout);
    

}
