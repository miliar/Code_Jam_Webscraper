#include <cstdio>  
#include <algorithm>  
#include <cstring>  
using namespace std;  
const int M =5100;  
int dir[M];//  dir[i] 0:F 1;B  
int n;   
int f[M];
char s[1005];  
   
int calc(int k) {  
    memset(f,0,sizeof(f));  
    int res=0;  
    int sum=0;  
    for (int i=0;i+k-1<=n-1;i++) {  
        if((dir[i]+sum)%2!=0) {  
            res++;  
            f[i]=1;  
        }  
        sum+=f[i];  
        if(i-k+1>=0) {  
        	sum-=f[i-k+1];    
        }  
    }  
    for (int i=n-k+1;i<n;i++) {  
        if((dir[i]+sum)%2!=0) {  
            return -1;  
        }  
        if(i-k+1>=0)  
        sum-=f[i-k+1];  
    }  
    return res;  
}  
  
  
  
  
/*void solve() {  
    int K=1,M=n;  
    for(int k=1;k<=n;k++) {  
        int m=calc(k); 
		if(m>0&&m<M) {  
            M=m;  
            K=k;   
        }  
          
    }   
     //cout<<K<<" "<<M;
     printf("%d %d", K, M);
}*/
int main() {
	int t;
	freopen("A-large.in", "r", stdin);
 	freopen("largeoutputA.out", "w", stdout);  
	scanf("%d", &t);
	for (int j = 1; j <=t; j++) {
		int k;
		scanf("%s %d", &s, &k);
		n = strlen(s);  
	    for(int i = 0; i < n; i++) {  
	        if(s[i] == '-') {  
	            dir[i] = 1;     
	        } else { 
	            dir[i] = 0;  
	        }  
	    }
	    int ans =calc(k);
	    if (ans == -1) {
			printf("Case #%d: IMPOSSIBLE\n", j);
    	} else {
	    	printf("Case #%d: %d\n", j, ans);	
	    }
	}
    return 0;     
}   