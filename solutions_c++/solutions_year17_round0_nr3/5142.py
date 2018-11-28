#include<bits/stdc++.h>
using namespace std;

int  N,K;
int L[1000];
int R[1000];
int vis[1000];
vector<int>m(1000);

int main(){

    ifstream myReadFile;
    myReadFile.open("input.in");
    ofstream myfile;
    myfile.open ("output.out");
    int t;
    myReadFile>>t;
    int c=1;

    while(t--){

        myReadFile>>N>>K;
        std::priority_queue<int> Q;
        int cnt=1;
        Q.push(N);
        int l,r;
        while(cnt<=K){
            int deq=Q.top();
            Q.pop();
            if(deq==1){
                l=0;r=0;
            }else{
                l=(deq/2);
                if(deq%2==0)l--;
                r=deq-l-1;
            }
            //cout<<deq<<" "<<l<<" "<<r<<endl;

            Q.push(l);
            Q.push(r);
            cnt++;
        }
        myfile<<"Case #"<<c<<": "<<max(l,r)<<" "<<min(l,r)<<endl;

        c++;
    }
    return 0;
}
