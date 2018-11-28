#include<cstdio>
#include<queue>
using namespace std;

void stall(int n,int k){
    priority_queue<int> hip;
    hip.push(n);
    int temp;
    for(int i=0;i<k;i++){

        temp = hip.top();
        hip.pop();
        temp--;
        hip.push(temp/2);
        hip.push(temp-temp/2);

    }
    printf("%d %d\n",temp-temp/2,temp/2);
}
int main(){
    int x,n,k;
    scanf("%d",&x);
    for(int i=0;i<x;i++){
        scanf("%d %d",&n,&k);
        printf("Case #%d: ",i+1);
        stall(n,k);
    }
}
