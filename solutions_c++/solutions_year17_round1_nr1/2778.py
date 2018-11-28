#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<stack>
#include<set>
#include<string>
using namespace std;
char m[30][30];
int rflag[30];
int t,r,c;
struct Node{
    char c;
    int x,y;
};
vector<Node> s;
queue<Node> q;
queue<int> qr;
int main(){
    cin>>t;
    for(int cas=1;cas<=t;cas++){
        memset(rflag,0,sizeof(rflag));
        while(!q.empty())q.pop();
        while(!qr.empty())qr.pop();
        printf("Case #%d:\n",cas);
        cin>>r>>c;
        for(int i=1;i<=r;i++){
            for(int j=1;j<=c;j++){
                cin>>m[i][j];
                if(m[i][j]!='?'){
                    rflag[j]=1;
                    Node nd={m[i][j],i,j};
                    q.push(nd);
                }
            }
        }
        while(!q.empty()){
            Node nd=q.front();
            q.pop();
            if(nd.x-1>0){
                if(m[nd.x-1][nd.y]=='?'){
                    m[nd.x-1][nd.y]=nd.c;
                    Node tmp={nd.c,nd.x-1,nd.y};
                    q.push(tmp);
                }
            }
            if(nd.x+1<=r){
                if(m[nd.x+1][nd.y]=='?'){
                    m[nd.x+1][nd.y]=nd.c;
                    Node tmp={nd.c,nd.x+1,nd.y};
                    q.push(tmp);
                }
            }
        }
        for(int i=1;i<=c;i++){
            if(rflag[i]){
                qr.push(i);
            }
        }
        while(!qr.empty()){
            int r1=qr.front();
            qr.pop();
            if(r1-1>=1&&rflag[r1-1]==0){
                for(int j=1;j<=r;j++){
                    m[j][r1-1]=m[j][r1];
                }
                rflag[r1-1]=1;
                qr.push(r1-1);
            }
            if(r1+1<=c&&rflag[r1+1]==0){
                for(int j=1;j<=c;j++){
                    m[j][r1+1]=m[j][r1];
                }
                rflag[r1+1]=1;
                qr.push(r1+1);
            }
        }
        for(int i=1;i<=r;i++){
            for(int j=1;j<=c;j++){
                cout<<m[i][j];
            }
            printf("\n");
        }
    }
    return 0;
}
