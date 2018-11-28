#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <algorithm>
#include <sstream>
#include <queue>
#include <math.h>
#include <set>
#include <map>
#include <climits>
#define INF 0x3f3f3f3f
using namespace std;
typedef long long ll;
int t;
int main()
{
    
    scanf("%d",&t);
    for(int test= 0;test<t;test++){
        char seq[1050];
        scanf("%s",seq);
        int len = strlen(seq);
        int k;
        scanf("%d",&k);
        int cnt = 0;
        bool found = false;
        for(int s = 0;s+k<=len;s++){
            if(seq[s]=='-'){
                cnt++;
                for(int i = 0;i<k;i++){
                    if(seq[s+i]=='+'){
                        seq[s+i]='-';
                    }else{
                        seq[s+i]='+';
                    }
                }
            }
            bool ok = true;
            for(int pos = 0;pos<len;pos++){
                if(seq[pos]=='-'){
                    ok=false;
                    break;
                }
            }
            if(ok){
                printf("Case #%d: %d\n",test+1,cnt);
                found=true;
                break;
            }
        }
        if(!found){
            printf("Case #%d: IMPOSSIBLE\n",test+1);
        }
        
    }
    
    return 0;
}
