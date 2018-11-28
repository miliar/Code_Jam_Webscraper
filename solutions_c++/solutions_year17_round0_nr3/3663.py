#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <queue>

using namespace std;
long long n,k;
int t;

struct Node{
    long long num;
    bool operator<(const Node tmp)const{
            return num<tmp.num;
    }
};
int main()
{

    FILE*f1=fopen("C-small-2-attempt0.in","r");
    FILE*f2=fopen("C-small-2-attempt0.out","w");
    fscanf(f1,"%d",&t);
    //scanf("%d",&t);
    int num;
    for(int tt=1;tt<=t;tt++){
        fscanf(f1,"%I64d %I64d",&n,&k);
        //scanf("%lld %lld",&n,&k);
        priority_queue<Node>q;
        Node tmp,tmp2,tmp3;
        tmp.num=n;
        q.push(tmp);
        bool flag=false;
        for(int i=0;i<k-1;i++){
            tmp=q.top();
            q.pop();
//printf("num: %lld\n",tmp.num);
            if(tmp.num==1){
                flag=true;
                break;
            }
            else{
                tmp2.num=(tmp.num-1)/2;
                //tmp2.l=tmp.l;
                tmp3.num=(tmp.num)/2;
                //tmp3.l=tmp.l+tmp2.num+1;
                q.push(tmp2);
                q.push(tmp3);
            }
        }
        fprintf(f2,"Case #%d: ",tt);
        //printf("Case #%d: ",tt);
        if(flag){
            fprintf(f2,"0 0\n");
            //printf("0 0\n");
        }
        else{
            tmp=q.top();
            //printf("%lld %lld\n",tmp.num/2,(tmp.num-1)/2);
            fprintf(f2,"%I64d %I64d\n",tmp.num/2,(tmp.num-1)/2);
        }
    }
    fclose(f1);
    fclose(f2);
    return 0;
}
