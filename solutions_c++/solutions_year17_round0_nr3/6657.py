/*
#include <iostream>
#include <queue>
using namespace std;

int T,n,k;

struct Data{
    int num,Ls,Rs;
    struct Data *left,*right,*now;
    Data(int a){
        num = a;
    }

    void push(Data* a,Data* b){
        now->left = a;
        now->right = b;
        a->right = now;
        b->left = now;
        now->Ls = now->num-a->num;
        now->Rs = b->num-now->num;
        a->Rs = now->Ls;
        a->Ls = now->Rs;
    }
    /*
    void pop(){
        now->left->
        now->left->right = now->right;
        now->right->left = now->left;
        now->left = NULL;
        now->right = NULL;
    }
    *//*
};

priority_queue<Data> q;

int main()
{
    cin>>T;
    for(int q = 1;q<=T;q++){
        cin>>n>>k;
    }
}

*/

#include <cstdio>
#include <iostream>
#include <queue>
#include <utility>
using namespace std;
int T,n,k;
int main(){
    freopen("input2.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    for(int p = 1;p<=T;p++){
        cin>>n>>k;
        priority_queue<pair<int,pair<int,int> > >q;
        q.push(make_pair(n+1,make_pair(0,n+1)));
        for(int i = 1;i<=k;i++){
            int left = q.top().second.first;
            int right = q.top().second.second;
            int dis = q.top().first;
            q.pop();
            int now = left+dis/2;
            //printf("push %d\n",now);
            q.push(make_pair(now-left,make_pair(left,now)));
            q.push(make_pair(right-now,make_pair(now,right)));
            if(i == k){
                printf("Case #%d: %d %d\n",p,max(now-left-1,right-now-1),min(now-left-1,right-now-1));
            }
        }
    }
}
