#include <bits/stdc++.h>
#define endl '\n'

using namespace std;

const int TIME = 1464;
const int INF = (1e9) + 7;

int tests,current_case;
int n,m;
bool busy1[TIME],busy2[TIME];
bool used[TIME][TIME/2][4][4];
int state[TIME][TIME/2][4][4];

void message(int current_case) {
    //cerr<<"Case "<<current_case<<" solved!"<<endl;
    fprintf(stderr, "Case %d solved!\n", current_case);
}

/*int recurse(int moment, int time1, int time2, int who) {
    if(time1>720 || time2>720) return INF;
    if(moment>1440) return ((time1==720 && time2==720) ? 0 : INF);
    if(used[moment][time1][who]) return state[moment][time1][who];
    int ans=INF;
    
    //Give it to the first one
    if(!busy1[moment]) {
        ans=min(ans,recurse(moment+1,time1+1,time2,1)+(who!=1));
    }

    //Give it to the second one
    if(!busy2[moment]) {
        ans=min(ans,recurse(moment+1,time1,time2+1,2)+(who!=2));
    }

    used[moment][time1][who]=true;
    state[moment][time1][who]=ans;
    return ans;
}*/

int recurse(int pos, int time1, int time2, int who, int first) {
    if(time1>720 || time2>720) return INF;
    if(pos==1441) {
        if(time1==720 && time2==720) {
            if(who==first) return 0;
            else return 1;
        }
        else return INF;
    }
    if(used[pos][time2][who][first]) return state[pos][time2][who][first];
    int curr,ans=INF;

    if(!busy1[pos] && time1<720) {
        curr=recurse(pos+1,time1+1,time2,1,first);
        if(who==2) ++curr;
        ans=min(ans,curr);
    }

    if(!busy2[pos] && time2<720) {
        curr=recurse(pos+1,time1,time2+1,2,first);
        if(who==1) ++curr;
        ans=min(ans,curr);
    }

    used[pos][time2][who][first]=true;
    state[pos][time2][who][first]=ans;

    return ans;
}

int main() {
    //ios_base::sync_with_stdio(false);
    //cin.tie(NULL);
    int i,j,x,y;

    tests=1;
    scanf("%d", &tests);
    //cin>>tests;
    for(current_case=1;current_case<=tests;current_case++) {
        scanf("%d %d", &n, &m);
        memset(busy1,0,sizeof(busy1));
        memset(busy2,0,sizeof(busy2));
        for(i=1;i<=n;i++) {
            scanf("%d %d", &x, &y);
            for(j=x+1;j<=y;j++) busy1[j]=true;
        }
        for(i=1;i<=m;i++) {
            scanf("%d %d", &x, &y);
            for(j=x+1;j<=y;j++) busy2[j]=true;
        }
        memset(used,0,sizeof(used));
        int ans=INF;
        if(!busy1[1]) ans=min(ans,recurse(2,1,0,1,1));
        if(!busy2[1]) ans=min(ans,recurse(2,0,1,2,2));
        printf("Case #%d: %d\n", current_case, ans);

        MESSAGE:
        message(current_case);
    }

    return 0;
}
