#include<iostream>
#include<vector>
#include<stack>
#include<string>
#include<queue>
#include<map>
#include<algorithm>
#include<sstream>
#include<set>
using namespace std;
#include<stdio.h>
#include<time.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#define MAX 100
#define INF 1<<23

#define I1(a) scanf("%d",&a)
#define I2(a,b) scanf("%d %d",&a,&b)
#define I3(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define rep(i,s,e) for(i=s;i<e;i++)
#define repr(i,s,e) for(i=s;i>e;i--)


#define in(a) freopen(a,"r",stdin)
#define out(a) freopen(a,"w",stdout)
#define ll long long
ll BigMod(ll B,ll P,ll M){  ll R=1; while(P>0)  {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return R%M;}
#define ull long double
#define M 1000000000
vector<int>digits;
int total_digits = 0;
ll global_mx = 1;
bool done = 0;
void last_seen(int position, int overall_max, bool highest_streak, ll num){
    //cout<<position<<" "<<total_digits<<endl;
    if(done)return;
    if(position==total_digits){
        global_mx = max(global_mx,num);
        done = 1;
        return;
    }

    if(position==0){
        for(int i=digits[position];i>=0;i--){
            last_seen(position+1, i, i==digits[position], i);
        }
    }else if(highest_streak==0){
        for(int i=9;i>=overall_max;i--){
            last_seen(position+1, max(overall_max,i), 0, num*10+i);
        }
    }else{
        if(digits[position]<overall_max){
            return;
        }
        for(int i=digits[position];i>=overall_max;i--){
            last_seen(position+1, i, i==digits[position], num*10+i);
        }
    }
}
int main()
{
    in("/Users/kishwar/Kishwar/C++/google/codejam/codejam/in");
    out("/Users/kishwar/Kishwar/C++/google/codejam/codejam/out");
    int T,caseno=1;
    cin>>T;
    while(T--){
        ll N;
        total_digits = 0;
        cin>>N;
        digits.clear();
        global_mx = 1;
        while(N){
            int x = N%10;
            digits.push_back(x);
            N/=10;
            total_digits++;
        }
        reverse(digits.begin(),digits.end());
        printf("Case #%d: ",caseno);
        done = 0 ;
        last_seen(0, 0, 0, 0);
        cout<<global_mx<<endl;
        caseno++;
    }
    return 0;
}
