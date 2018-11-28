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
int seats[10000];
int find_right(int indx){
    int s = indx;
    indx += 1;
    while(1){
        if(seats[indx]==1){
            return indx-s-1;
        }
        indx++;
    }
}
int find_left(int indx){
    int s = indx;
    indx -= 1;
    while(1){
        if(seats[indx]==1){
            return s-indx-1;
        }
        indx--;
    }
}
int main()
{
    in("/Users/kishwar/Kishwar/C++/google/codejam/problemC/in");
    //out("/Users/kishwar/Kishwar/C++/google/codejam/problemC/out");
    int T,caseno=1;
    cin>>T;
    while(T--){
        int N,K;
        cin>>N>>K;
        printf("Case #%d: ",caseno);
        caseno++;
        memset(seats,0,sizeof(seats));
        N+=2;
        seats[1] = 1;
        seats[N] = 1;
        int last_position_taken = 0;
        for(int i=0;i<K;i++){
            //cout<<last_position_taken<<endl;
            int minLR = 0;
            vector<int>bests;
            for(int j=2;j<N;j++){
                if(seats[j])
                    continue;
                int l = find_left(j);
                int r = find_right(j);
                if(min(l,r)>minLR){
                    bests.clear();
                    bests.push_back(j);
                    minLR = min(l,r);
                }else if(min(l,r)==minLR){
                    bests.push_back(j);
                }
            }
            /*cout<<"MAX MINLRs"<<endl;
            for(int i=0;i<bests.size();i++){
                cout<<bests[i]<<endl;
            }
            cout<<"----"<<endl;*/
            if(bests.size()==1){
                seats[bests[0]] = 1;
                last_position_taken = bests[0];
                continue;
            }
            int maxLR = 0;
            vector<int>bests2;
            for(int j=0;j<bests.size();j++){
                int l = find_left(bests[j]);
                int r = find_right(bests[j]);
                if(max(l,r)>maxLR){
                    bests2.clear();
                    bests2.push_back(bests[j]);
                    maxLR = max(l,r);
                }else if(max(l,r)==maxLR){
                    bests2.push_back(bests[j]);
                }
            }
            /*cout<<"MAX MAXLRs"<<endl;
            for(int i=0;i<bests2.size();i++){
                cout<<bests2[i]<<endl;
            }
            cout<<"----"<<endl;*/
            if(bests2.size()==1){
                seats[bests2[0]] = 1;
                last_position_taken = bests2[0];
                continue;
            }
            int mx = bests2[0];
            for(int j=0;j<bests2.size();j++){
                mx = min(mx,bests2[j]);
            }
            seats[mx] = 1;
            last_position_taken = mx;

        }
        //cout<<last_position_taken<<endl;
        int r=find_right(last_position_taken),l=find_left(last_position_taken);
        cout<<max(l,r)<<" "<<min(l,r)<<endl;
    }
    return 0;
}
