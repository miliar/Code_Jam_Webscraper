#include<iostream>
#include<string>
#include<vector>
#include<queue>
using namespace std;

struct range {
    long long len, l;
};

class cmp {
public:
    bool operator() (range a, range b) {
        if (a.len<b.len) {
            return true;
        }
        else if (a.len==b.len) {
            if (a.l>b.l) {
                return true;
            }
            else {
                return false;
            }
        }
        else {
            return false;
        }
    }
};

int main() {
    int T;
    cin>>T;
    long long n,k;
    for (int t=1;t<=T;t++) {
        priority_queue<range, vector<range>, cmp> heap;
        cin>>n>>k;
        range init;
        init.len=n;
        init.l=0;
        //init.r=n-1;
        heap.push(init);
        int idx = 1;
        while (idx<k) {
            range tmp = heap.top();
            //cout<<idx<<":"<<tmp.len<<" "<<tmp.l<<endl;
            heap.pop();
            range left,right;
            if (tmp.len%2==0) {
                left.len = tmp.len/2-1;
                left.l = tmp.l;
                right.len = tmp.len/2;
                right.l = tmp.l + tmp.len/2;
            }
            else {
                left.len = tmp.len/2;
                left.l = tmp.l;
                right.len = tmp.len/2;
                right.l = tmp.l + tmp.len/2+1;
            }
            heap.push(left);
            heap.push(right);
            idx++;
        }
        range res = heap.top();
        if (res.len%2==1) {
            cout<<"Case #"<<t<<": "<<res.len/2<<" "<<res.len/2<<endl;
        }
        else {
            cout<<"Case #"<<t<<": "<<res.len/2<<" "<<res.len/2-1<<endl;
        }
    }
    return 0;
}
