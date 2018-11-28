#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
using namespace std;
#define INF 10000
int timeline[1441];

int f[721][721][2][2];
int recur(int re1,int re2,int who,int start){
    if(re1 < 0 || re2 < 0 )return INF;
    if(f[re1][re2][who][start]!=-1)return f[re1][re2][who][start];

    int tmp = 1440 - re1 - re2;
    if(tmp == 1440){
        return f[re1][re2][who][start] = (who != start);
    }
    if(timeline[tmp]==0){
        if(who==0){
            return f[re1][re2][who][start] = min(recur(re1-1,re2,who,start),recur(re1,re2-1,1,start)+1);
        }
        else{
            return f[re1][re2][who][start] = min(recur(re1,re2-1,who,start),recur(re1-1,re2,0,start)+1);
        }
    }
    else if(timeline[tmp]==1){
        if(who==0){
            return f[re1][re2][who][start] = recur(re1,re2-1,1,start)+1;
        }
        else{
            return f[re1][re2][who][start] = recur(re1,re2-1,1,start);
        }
    }
    else{
        if(who==0){
            return f[re1][re2][who][start] = recur(re1-1,re2,0,start);
        }
        else{
            return f[re1][re2][who][start] = recur(re1-1,re2,0,start)+1;
        }
    }

}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("Bout.txt","w",stdout);
    int cas,q;
    cin>>cas;
    for(q=1;q<=cas;q++){
        int A,B;
        cin>>A>>B;
        memset(f,-1,sizeof(f));
        memset(timeline,0,sizeof(timeline));
        for(int i=0; i < A; i++){
                int t1,t2;
                cin>>t1>>t2;
                for(int j =t1;j < t2;j++)timeline[j]=1;
        }
        for(int i=0; i < B; i++){
                int t1,t2;
                cin>>t1>>t2;
                for(int j =t1;j < t2;j++)timeline[j]=2;
        }
        cout<<"Case #"<<q<<": "<<min(recur(720,720,0,0),recur(720,720,1,1) )<<endl;
    }
    return 0;
}
