#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

/*
string getMiddle(int startS,int endS,int people){
    if (startS!=endS){
        int middleS=(endS-startS)/2+startS;//+(endS-startS)%2;
        return
        if (people==1)return max(middleS-startS,endS-middleS)<<" "<<min(middleS-startS,endS-middleS);
        getMiddle(middleS,startS,people-1);
        getMiddle(endS,middleS,people-1);
    }
}


class seat {
public:
    seat left,right;
};
*/
int main()
{
    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int t;
    cin>>t;
    for (int x=1;x<t+1;x++){
        int people,limit=1,range=1,arrayLimit=1,minIndex=0,maxIndex=0,maxCounter=0;
        long long int num;
        cin>>num>>people;
        while(limit<people*2){
            range*=2;
            limit+=range;
            //cout<<"range is "<<range<<" limit "<<limit<<endl;
        }

        int levels=log2(range)+1;
        //cout<<"levels is "<<levels<<endl;
        long long int tree[levels][range];
        tree[0][0]=num;
        for (int i=1;i<levels;i++){
            for (int j=0;j<arrayLimit;j++){
                tree[i][2*j]  =(tree[i-1][j]-1)/2;
                tree[i][2*j+1]=tree[i-1][j]-1-tree[i][2*j];
            }
            arrayLimit*=2;
        }
        //cout<<"range is "<<range<<" arrayLimit is "<<arrayLimit<<endl;
        for (int i=0;i<range;i+=2){
            if (tree[levels-1][i]+tree[levels-1][i+1]>tree[levels-1][maxIndex]+tree[levels-1][maxIndex+1]){
                maxIndex=i;
                maxCounter=1;
            }
            else if (tree[levels-1][i]+tree[levels-1][i+1]==tree[levels-1][maxIndex]+tree[levels-1][maxIndex+1]){
                maxCounter++;
            }

            if (tree[levels-1][i]+tree[levels-1][i+1]<tree[levels-1][minIndex]+tree[levels-1][minIndex+1]){
                minIndex=i;
            }
        }
        people-=limit-range-range/2;
        //cout<<"level is "<<levels<<endl;
        if(people<=maxCounter)cout<<"Case #"<<x<<": "<<max(tree[levels-1][maxIndex],tree[levels-1][maxIndex+1])<<" "<<min(tree[levels-1][maxIndex],tree[levels-1][maxIndex+1])<<endl;
        else cout<<"Case #"<<x<<": "<<max(tree[levels-1][minIndex],tree[levels-1][minIndex+1])<<" "<<min(tree[levels-1][minIndex],tree[levels-1][minIndex+1])<<endl;
    }
    return 0;
}
