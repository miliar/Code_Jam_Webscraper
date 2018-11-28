#include <stdio.h>
#include <iostream>
#include <vector>
#include <math.h>
#include <queue>
#include <utility>

using namespace std;

struct CompareByFirst {
    bool operator()(pair<int, int> const & a,pair<int, int> const & b)
    { return a.first < b.first||(!(b.first < a.first) && a.second > b.second); }
};

void cal(){
    int n,k;
    scanf("%d %d",&n,&k);
    pair <int,int> temp;
    priority_queue<pair<int, int>,
                   std::vector<pair<int, int> >,
                   CompareByFirst> mypq;
    mypq.push(make_pair(n,(int)ceil(n/2.0)));
    for(int i=1;i<=k;i++){
        temp = mypq.top();
        mypq.pop();
        if(i==k){
            if(temp.first%2==0)
                printf("%d %d",temp.first/2,temp.first/2-1);
            else
                printf("%d %d",temp.first/2,temp.first/2);
        }
        else{
            if(temp.first%2==0){
                mypq.push(make_pair(temp.first/2,temp.second/2+temp.second+1));
                mypq.push(make_pair(temp.first/2-1,temp.second/2));
            }
            else{
                mypq.push(make_pair(temp.first/2,temp.second/2));
                mypq.push(make_pair(temp.first/2,temp.second/2+temp.second));
            }
        }
    }
    /*
    mypq.push(make_pair(10,10));
    mypq.push(make_pair(20,10));
    mypq.push(make_pair(10,20));

    temp = mypq.top();
    cout<<temp.first<<" "<<temp.second;
    mypq.pop();
    */

}
int main() {
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        printf("Case #%d: ",i);
        //printf("%d",(int)ceil(i/2.0));
        cal();
        printf("\n");
    }
    return 0;
}
