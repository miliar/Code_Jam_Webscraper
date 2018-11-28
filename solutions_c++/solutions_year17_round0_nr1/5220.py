#include <iostream>
#include <vector>
#include <queue>
struct Node{
    int state;
    int fliptimes;

    Node(int _state,int _t){
        state = _state;
        fliptimes = _t;
    }
};

int len  = 0;



using namespace std;
int main() {
//    small input
    freopen("test1.txt","r",stdin);
    freopen("Asmall.out","w",stdout);
    int tt;

    cin >> tt;
    int order = 1;
    while(tt-- > 0){
//        queue<Node>Q;
        int t = 0;
        int k = 0;
        string cakes;
        cin >> cakes;
        cin >> k;
        int mask = 0;
        len = 0;
        for(int i = 0;i <k;++i){
            mask = mask * 2 + 1;
        }

        for(int i = 0; i < len; ++i){

        }
        for(auto c: cakes){
            if (c == '-'){
                t = t*2 + 1;
            }else{
                t = t*2;
            }
            len ++;
        }
        mask = mask << (len - k);

        bool hasanswer = false;
        int times = 0;
        while(1){
            if(t == 0){
                hasanswer = true;
                break;
            }
            int  first = 1 << (len - 1);
            int start = -1;
            for(int i = 0; i < len;++i){
                if(first & t){
                    start = i;
                    break;
                }
                first >>= 1;
            }
            if(start + k > len){
                break;
            }
            int tmask = mask>>start;
            t = t^tmask;
//            cout << t << endl;
            times++;
        }
        if(hasanswer){
            cout<<"Case #"<<(order++)<<": "<<times<<endl;
        }else{
            cout<<"Case #"<<(order++)<<": "<<"IMPOSSIBLE"<<endl;
        }
    }
}