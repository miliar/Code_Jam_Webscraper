#include<iostream>
#include<fstream>
#include<queue>

using namespace std;


int main(){
    fstream fin("/Users/anupsing/Documents/CP/GCJ/QF/3/inputB.in");
    fstream fout("/Users/anupsing/Documents/CP/GCJ/QF/3/outputB.txt");

     int T;
     fin>>T;
    int cases=1;
    while(T--){
        long long N,K;
        fin>>N>>K;
        priority_queue<int>q;
        q.push(N);

        long long half,tp;
        while(K--){
                 tp = q.top();
                q.pop();
                 half= tp/2;
                 tp=tp-half-1;

                tp=max(0LL,tp);
                q.push(half);
                q.push(tp);
        }

        fout<<"Case #"<<cases<<": "<<half<<" "<<tp<<endl;
        cases++;
    }
    return 0;

}
