#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;

typedef long long ll;


struct AugPath {
    int A, B;   //size of left, right groups
    vector<vector<int> > G; //size A
    vector<bool> visited;   //size A
    vector<int> P;          //size B

    AugPath(int _A, int _B): A(_A), B(_B), G(_A), P(_B, -1) {}

    void AddEdge(int a, int b) {    //a from left, b from right
        G[a].push_back(b);
    }
    bool Aug(int x) {
        if (visited[x]) return 0;
        visited[x] = 1;
        /* Greedy heuristic */
        for (auto it:G[x]) {
            if (P[it] == -1) {
                P[it] = x;
                return 1;
            }
        }
        for (auto it:G[x]) {
            if (Aug(P[it])) {
                P[it] = x;
                return 1;
            }
        }
        return 0;
    }
    int MCBM() {
        int matchings = 0;
        for (int i = 0; i < A; ++i) {
            visited.resize(A, 0);
            matchings += Aug(i);
            visited.clear();
        }
        return matchings;
    }
    vector<pair<int, int> > GetMatchings() {
        vector<pair<int, int> > matchings;
        for (int i = 0; i < B; ++i) {
            if (P[i] != -1) matchings.emplace_back(P[i], i);
        }
        return matchings;
    }
};

AugPath *aug;
bool cross[110][110];
bool pluss[110][110];
bool coltake[110];
bool rowtake[110];
bool di1[210],di2[210];
int n;
char original[110][110];

void addcross(){
    int c=0;
    for(int i=0;i<n;i++){
        if(rowtake[i])continue;
        while(coltake[c]){
            c++;
        }
        rowtake[i]=true;
        coltake[c]=true;
        cross[i][c]=true;
        //printf("addcross %d %d\n",i,c);
    }
}

pair<int,int> getxy(int d1,int d2){
    //d1=a+b
    //d2=n-1-a+b
    int b=d1+d2-n+1;
    if(b%2!=0)return make_pair(-1,-1);
    b=b/2;
    int a=d1-b;
    if(a<0 || a>=n || b<0 || b>=n)return make_pair(-1,-1);
    return make_pair(a,b);
}

int main(){
    freopen("hi.txt","r",stdin);
    freopen("hi2.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    char str[1010];
    for(int t=1;t<=tc;t++){
        int m;
        scanf("%d%d",&n,&m);
        aug=new AugPath(2*n,2*n);
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                cross[i][j]=false;
                pluss[i][j]=false;
                original[i][j]='.';
            }
            coltake[i]=false;
            rowtake[i]=false;
        }
        for(int i=0;i<2*n;i++){
            di1[i]=false;
            di2[i]=false;
        }
        int a,b;
        char str[10];
        while(m--){
            scanf("%s%d%d",str,&a,&b);
            a--;b--;
            if(str[0]=='+'){pluss[a][b]=true;original[a][b]='+';}
            if(str[0]=='x'){cross[a][b]=true;original[a][b]='x';}
            if(str[0]=='o'){
                pluss[a][b]=true;
                cross[a][b]=true;
                original[a][b]='o';
            }

            if(pluss[a][b]){
                di1[a+b]=true;
                di2[(n-1-a)+b]=true;
            }
            if(cross[a][b]){
                coltake[b]=true;
                rowtake[a]=true;
            }
        }
        addcross();
        for(int i=0;i<2*n-1;i++){
            if(di1[i])continue;
            int counter=0;
            for(int j=0;j<2*n-1;j++){
                if(di2[j])continue;
                if(getxy(i,j).first==-1)continue;
                aug->AddEdge(i,j);
            }
            //printf("%d:%d\n",i,counter);
        }
        aug->MCBM();
        vector<pair<int, int> > v=aug->GetMatchings();
        for(int i=0;i<v.size();i++){
            pair<int,int> p=getxy(v[i].first,v[i].second);
            //printf("x %d %d\n",p.first,p.second);
            pluss[p.first][p.second]=true;
        }
/*
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(cross[i][j] && pluss[i][j])printf("o");
                else if(cross[i][j])printf("x");
                else if(pluss[i][j])printf("+");
                else printf(".");
            }
            printf("\n");
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                printf("%c",original[i][j]);
            }
            printf("\n");
        }*/
        int ans=0;
        vector<pair<char,pair<int,int> > >vans;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(cross[i][j])ans++;
                if(pluss[i][j])ans++;
                //printf("%d %d:%d %d\n",i,j,cross[i][j],pluss[i][j]);
                if(cross[i][j] && pluss[i][j] && original[i][j]!='o'){
                    vans.push_back(make_pair('o',make_pair(i+1,j+1)));
                }
                if(cross[i][j] && !pluss[i][j] && original[i][j]!='x'){
                    vans.push_back(make_pair('x',make_pair(i+1,j+1)));
                }
                if(!cross[i][j] && pluss[i][j] && original[i][j]!='+'){
                    vans.push_back(make_pair('+',make_pair(i+1,j+1)));
                }
            }
        }
        printf("Case #%d: %d %d\n",t,ans,vans.size());
        for(int i=0;i<vans.size();i++){
            printf("%c %d %d\n",vans[i].first,vans[i].second.first,vans[i].second.second);
        }
    }
    return 0;
}
