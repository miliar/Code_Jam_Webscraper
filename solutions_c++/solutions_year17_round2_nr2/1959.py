#include <bits/stdc++.h>
#define pii pair<int,int>

using namespace std;

int N;

string ch[6] = {"R","O","Y","G","B","V"};

map<int,map<int,map<int,map<int,bool> > > > vis;

bool notsame(int a,int b){
    if(a==b)return false;
    if(a==-1 || b==-1)return true;

    /// orange
    if(a==1){
        if(b==0 || b==2)return false;
        return true;
    }
    if(b==1){
        if(a==0 || a==2)return false;
        return true;
    }

    /// green

    if(a==3){
        if(b==2 || b == 4)return false;
        return true;
    }

    if(b==3){
        if(a==2 || a == 4)return false;
        return true;
    }

    /// violet

    if(a==5){
        if(b==0 || b==4)return false;
        return true;
    }

    if(b==5){
        if(a==0 || a==4)return false;
        return true;
    }

    return true;
}

string dfs(int tot,int R,int O,int Y,int G,int B,int V,int last,int first){

    string ret = "";
    if(tot==N ){
        if(notsame(last,first)){
            ret = ch[last] + ret;
        }
        return ret;
    }

    int col[6] = {R,O,Y,G,B,V};
    int tmp[6] = {R,O,Y,G,B,V};
    pii tosrt[6] = {{-R,0},{-O,1},{-Y,2},{-G,3},{-B,4},{-V,5}};
    if(vis[-tosrt[0].first][-tosrt[1].first][-tosrt[2].first][last])return "";
    vis[-tosrt[0].first][-tosrt[1].first][-tosrt[2].first][last] = 1;
    sort(tosrt,tosrt+6);
    for(int i=0;i<6;++i){
        int idx = tosrt[i].second;
        if(!col[idx])continue;
        tmp[idx]--;
        int fr(first);
        if(!tot)fr = idx;
        if(notsame(idx,last)){
            ret = dfs(tot+1,tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5],idx,fr);
            if(ret.size()){
                ret = ch[idx] + ret;
                return ret;
            }
        }
        tmp[idx]++;
    }
    return ret;
}

int main()
{
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cs(0);
    cin>>t;
    while(t--){
        vis.clear();
        int R,O,Y,G,B,V;
        cin>>N>>R>>O>>Y>>G>>B>>V;
        string ans = dfs(0,R,O,Y,G,B,V,-1,-1);
        if(!ans.size())ans = "IMPOSSIBLE";
        else ans.erase(ans.end()-1);
        ++cs;
        cout<<"Case #"<<cs<<": "<<ans<<"\n";
    }
    return 0;
}
