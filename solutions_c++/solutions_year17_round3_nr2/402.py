#include <bits/stdc++.h>

using namespace std;
int ac,aj;
vector<pair<int,int> > aces;
vector<pair<int,int> > ajes;
int DP[1445][740][2];
int curstart=0;
int solve(int CurMin,int LeftForZero,int LeftForOne,int turn)
{
    if(CurMin==1439){
        if(turn==curstart)
            return 0;
        return 1;
    }
    int &ret=DP[CurMin][LeftForZero][turn];
    if(ret!=-1)
        return ret;
    ret=1e9;
    if(turn == 0)
    {
        for(int i=0;i<aces.size();i++){
            if(CurMin>=aces[i].first&&CurMin<aces[i].second)
                return ret;}
        if(LeftForZero>0)
            ret=min(ret,solve(CurMin+1,LeftForZero-1,LeftForOne,turn));
        if(LeftForOne>0)
            ret=min(ret,solve(CurMin+1,LeftForZero,LeftForOne-1,1-turn)+1);
    }
    else{
        for(int i=0;i<ajes.size();i++){
            if(CurMin>=ajes[i].first&&CurMin<ajes[i].second)
                return ret;}

        if(LeftForOne>0)
            ret=min(ret,solve(CurMin+1,LeftForZero,LeftForOne-1,turn));
        if(LeftForZero>0)
            ret=min(ret,solve(CurMin+1,LeftForZero-1,LeftForOne,1-turn)+1);
    }
    return ret;
}
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    int cases=0;
    cin>>T;
    while(T--){
        curstart=0;
        cases++;
        aces.clear();
        ajes.clear();
        memset(DP,-1,sizeof DP);
        cin>>ac>>aj;
        for(int i=0;i<ac;i++){
            int a,b;
            cin>>a>>b;
            aces.push_back(make_pair(a,b));
        }
        for(int i=0;i<aj;i++){
            int a,b;
            cin>>a>>b;
            ajes.push_back(make_pair(a,b));
        }
        int ans=solve(0,719,720,0);
        memset(DP,-1,sizeof DP);
        curstart=1;
        ans=min(ans,solve(0,720,719,1));
        cout<<"Case #"<<cases<<": "<<ans<<endl;
    }
    return 0;
}
