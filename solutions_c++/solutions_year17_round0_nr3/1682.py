#include <iostream>
using namespace std;

struct EmptyStall{
    long long val, cnt;
}small, large, newSmall, newLarge;

void split(long long n, long long &small, long long &large){
    if(n % 2 == 0){
        small = (n - 1) / 2;
        large = small + 1;
    }
    else{
        small = large = (n - 1) / 2;
    }
}

int main(){
    int t;
    cin >> t;

    long long nStalls, nPeople, cntPeople;
    for(int i = 0; i < t; i ++){
        cin >> nStalls >> nPeople;
        cout << "Case #" << i + 1 << ": ";
        small.val = -1, small.cnt = 0;
        large.val = nStalls, large.cnt = 1;

        for(cntPeople = 1; ; cntPeople *= 2){
//            cout << endl << cntPeople << "--" << nPeople << ": " << small.val << ", " << small.cnt << "--" << large.val << ", " << large.cnt << endl;
            if(nPeople <= cntPeople){
                if(nPeople <= large.cnt){
                    split(large.val, small.val, large.val);
                }
                else{
                    split(small.val, small.val, large.val);
                }
                break;
            }
            nPeople -= cntPeople;
            //small & large updating
            newSmall.cnt = newLarge.cnt = 0;
            if(small.cnt > 0){
                newSmall.val = (small.val - 1) / 2;
                if(small.val % 2 == 0){
                    newSmall.cnt += small.cnt;
                    newLarge.val = newSmall.val + 1;
                    newLarge.cnt += small.cnt;
                }
                else{
                    newSmall.cnt += small.cnt * 2;
                }
            }
            if(large.cnt > 0){
                if(large.val % 2 == 0){
                    newSmall.val = (large.val - 1) / 2;
                    newSmall.cnt += large.cnt;
                    newLarge.val = newSmall.val + 1;
                    newLarge.cnt += large.cnt;
                }
                else{
                    newLarge.val = (large.val - 1) / 2;
                    newLarge.cnt += 2 * large.cnt;
                }
            }
            small = newSmall;
            large = newLarge;
        }
        cout << large.val << " " << small.val << endl;
    }
    return 0;
}

