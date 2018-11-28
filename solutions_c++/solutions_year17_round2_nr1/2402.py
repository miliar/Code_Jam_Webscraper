#include <algorithm>
#include <iostream>
#include <string>
#include <math.h>
#include <vector>
#include <stdio.h>
#include <sstream>
#include <queue>
#include <unordered_set>
#include <map>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <bitset>

using namespace std;

#define REP(i,a,b) for(int i = int(a); i<=int(b);i++)

typedef long long ll;
typedef vector<int> vi;
int dp[30][160] = {0};//first parameter is dice left, second parameter is sum

double maxx = 0;
double time_e;

int main(int argc, const char * argv[]) {  
    int TC;
    scanf("%d",&TC);
    REP(i,1,TC){
        int total_len, num_horse;
        scanf("%d%d",&total_len,&num_horse);
        maxx = 0;
        REP(j,0,num_horse-1){
            int pos, speed;
            scanf("%d%d",&pos,&speed);
            time_e = (double)(total_len - pos)/speed;
            
            if(time_e > maxx) maxx = time_e;
            // cout<<maxx<<endl;

        }
        printf("Case #%d: %.6lf\n",i,(double)total_len/maxx);
    }
}