#include <algorithm>
#include <assert.h>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <memory.h>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <utility>
#include <vector>
using namespace std;

typedef pair<int,int> PII;
typedef long long LL;

#define ALL(x) x.begin(),x.end()

#define DEB(args...) fprintf(stderr,args)

#define PB push_back
#define MP make_pair
#define ST first
#define ND second 

const int INF = 0x3f3f3f3f;

int rem[4];
int remat[4];

int main(){
    int t;
    scanf("%d", &t);
    for(int cas = 0; cas < t; cas++){
        int n, p;
        scanf("%d%d",&n,&p);
        long long ans;
        for(int i = 0; i < p; i++){
            rem[i]=0;
        }
        for(int i = 0; i < n; i++){
            int a;
            scanf("%d",&a);
            rem[a%p]++;
        }
        if(p==2){
            ans = rem[0] + (rem[1]+1)/2;
            printf("Case #%d: %lld\n", cas+1, ans);       
        }
        else if(p==3){
            ans = rem[0];
            
            while(rem[1]>0&&rem[2]>0){
                ans++;
                rem[1]--;
                rem[2]--;
            }
            while(rem[1]>2){
                ans++;
                rem[1]-=3;
            }
            while(rem[2]>2){
                ans++;
                rem[2]-=3;
            }
            ans+=(rem[1]+2)/3+(rem[2]+2)/3;
            printf("Case #%d: %lld\n", cas+1, ans);  
        }
        else{
            ans = 0;
            int p2[6]={0,1,2,3,4,5};
            long long aux = 0;
            do{
                aux = 0;
                for(int i = 0; i < p; i++){
                    remat[i] = rem[i];
                }
                for(int i = 0; i < 6; i++){
                    if(p2[i]==0){
                        while(rem[1]>0&&rem[3]>0){
                            rem[1]--;
                            rem[3]--;
                            aux++;
                        }
                    }
                    else if(p2[i]==1){
                        while(rem[2]>1){
                            rem[2]-=2;
                            aux++;
                        }                
                    }
                    else if(p2[i]==2){
                        while(rem[2]>0&&rem[1]>1){
                            rem[2]-=1;
                            rem[1]-=2;
                            aux++;
                        }    
                    }
                    else if(p2[i]==3){
                        while(rem[3]>3){
                            rem[3]-=4;
                            aux++;
                        }                            
                    }
                    else if(p2[i]==4){
                        while(rem[1]>3){
                            rem[1]-=4;
                            aux++;
                        }       
                    }
                    else if(p2[i]==5){
                        while(rem[2]>0&&rem[3]>1){
                            rem[2]-=1;
                            rem[3]-=2;
                            aux++;
                        }    
                    }
                }
                int ok = 0;
                for(int i = 1; i <= 3; i++){
                    if(rem[i]>0)ok=1;
                }
                ans = max(ans, aux+rem[0]+ok);
            }while(next_permutation(p2,p2+6));
            printf("Case #%d: %lld\n", cas+1, ans);              
        }
        
        

    }
    
}
