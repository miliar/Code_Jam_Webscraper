#include<iostream>
#include<stdio.h>
#include<vector>
#include<queue>
//#include <cmath>
using namespace std;


class Slot{
public:
    long long starti=0, endi = 0, length = 0;

    Slot (long long s, long long e){
        starti = s;
        endi = e;
        length = e-s+1;
    }
};


bool operator <(const Slot& a, const Slot& b){
    return a.length == b.length ? a.starti - b.starti > 0: b.length - a.length > 0;
}

int main (){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int testcase;
    scanf("%d ", &testcase);

    for (int i = 0; i< testcase; i++){

        long long n, k;
        scanf("%lld %lld", &n, &k);
        long long pos = 0, ls = 0, rs = 0;
        priority_queue<Slot> emptyslots;
        emptyslots.push(Slot(1, n));
        for (int i = 0; i<k;i++){
            Slot s = emptyslots.top();
            //cout << "\tfound emptyslot: " << s.starti << " to " << s.endi << endl;
            emptyslots.pop();
            pos = (s.starti + s.endi)/2;
            ls = pos - s.starti;
            rs = s.endi - pos;
            if (s.endi - (pos+1) > pos -1 - s.starti){
                //even
                if (s.endi - (pos+1) >= 0) emptyslots.push(Slot(pos+1, s.endi));
                if (pos -1 - s.starti >=0) emptyslots.push(Slot(s.starti, pos-1));
                //if (s.endi - (pos+1) >=0) cout << "\t\temptyslot: " << pos+1 << " to " << s.endi << endl;
                //if (pos -1 - s.starti >=0) cout << "\t\temptyslot: " << s.starti << " to " << pos -1 << endl;
            }else{
                //odd
                if (pos -1 - s.starti >= 0) emptyslots.push(Slot(s.starti, pos-1));
                if (s.endi - (pos+1) >= 0) emptyslots.push(Slot(pos+1, s.endi));
                //if (pos -1 - s.starti >= 0) cout << "\t\temptyslot: " << s.starti << " to " << pos -1 << endl;
                //if (s.endi - (pos+1) >= 0) cout << "\t\temptyslot: " << pos+1 << " to " << s.endi << endl;
            }
            //cout << "i = " << i << ", pos: " << pos  << ", min: " << min(ls, rs) <<", rs: " << max(ls, rs)<< endl;
            //get min
            //get max
            //occupy stall, choose leftmost
        }

        printf("Case #%d: %lld %lld", i+1, max(ls, rs), min(ls, rs));

        if (i!=testcase-1)printf("\n");
    }

    return 0;
}
