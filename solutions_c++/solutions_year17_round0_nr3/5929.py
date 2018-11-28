

#include <iostream>
#include <numeric>
#include <fstream>
#include <utility>
#include <queue>
using namespace std;

pair<u_long ,u_long > maxAndMin;
void getAnswer(u_long N,u_long K){
    priority_queue<u_long > Q;
    Q.push(N);

    for(u_long i=0;i<K;++i){
        u_long tmp=Q.top();

        if(tmp%2 == 1){
            u_long gap=(tmp-1)/2;
            maxAndMin.first=gap;
            maxAndMin.second=gap;
            Q.push(gap);
            Q.push(gap);
        } else{
            u_long gap=tmp/2;
            maxAndMin.first=gap;
            maxAndMin.second=gap-1;
            Q.push(gap);
            Q.push(gap-1);
        }
        Q.pop();
//        cout<<"H"<<"    ";
    }
}

void dealMethod(u_long N,u_long K){
//    if(N<2*K){
//        maxAndMin.first=0;
//        maxAndMin.second=0;
//    }
//    else if(N==2*K){
//        maxAndMin.first=1;
//        maxAndMin.second=0;
//    }
//    else{
    getAnswer(N,K);
    //}
}

int main(int argc,char** argv){
    std::ifstream in(argv[1]);
    std::ofstream out(argv[2]);

    int T=0;
    in>>T;
    u_long N,K;


    for(int i=0;i<T;i++)
    {

        std::cout<<i<<std::endl;
        in>>N>>K;

        dealMethod(N,K);

        out<<"Case #"<<i+1<<": "<<maxAndMin.first<<" "<<maxAndMin.second<<std::endl;

    }


    return 0;


}