#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <deque>
using namespace std;

int casenum;
deque<long long> label, num;
/*
void debug() {
    if(label.size() != num.size()) {
        cout << "size not same" << endl;
        return;
    }
    cout << "hehe" << endl;
    for(int i = 0;i < label.size();i ++) {
        cout << label.at(i) << " " << num.at(i) << endl;
    }
}
*/
int main()
{
    //freopen("C-large.in", "r", stdin);
    //freopen("out.out", "w", stdout);
    cin >> casenum;
    for(int cs = 1; cs <= casenum; cs ++) {
        long long n, k; cin >> n >> k;
        label.clear();
        num.clear();
        label.push_back(n);
        num.push_back(1);
        long long total = 0;
        long long ll, rr;
        while(true) {
            long long tt = label.front();
            long long nn = num.front();
            label.pop_front();
            num.pop_front();
            total += nn;
            if(tt % 2 == 0) {
                ll = tt / 2 - 1;
                rr = tt / 2;
            } else {
                ll = (tt - 1) / 2;
                rr = (tt - 1) / 2;
            }
            if(total >= k) {
                break;
            }
            bool do_ll = false;
            bool do_merge = false;
            if(!label.empty()) {
                long long lastl = label.back();
                long long lastn = num.back();
                if(lastl == rr) {
                    do_merge = true;
                    lastn += nn;
                    if(ll == rr) {
                        lastn += nn;
                        do_ll = true;
                    }
                    num.pop_back();
                    num.push_back(lastn);
                }
            }
            if(do_merge == false) {
                if(ll == rr) {
                    do_ll = true;
                    label.push_back(rr);
                    num.push_back(2 * nn);
                } else {
                    label.push_back(rr);
                    num.push_back(nn);
                }
            }

            if(do_ll == false) {
                label.push_back(ll);
                num.push_back(nn);
            }
            // debug();
        }
        cout << "Case #" << cs << ": ";
        cout << rr << " " << ll << endl;
    }
    return 0;
}
