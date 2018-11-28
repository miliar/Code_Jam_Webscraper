#include "iostream"
#include "string"
#include "queue"

using namespace std;


typedef struct node {
    int min,max,l,c,ri,le;
    bool operator< (const struct node& n1)const{
        if(min<n1.min) {
            return true;
        } else {
            if(max<n1.max) {
                return true;
            } else {
                return false;
            }
        }
    }

} node_t;

int cal_le(int n) {
    if((n%2)==1) {
        return n/2;
    } else {
        return n/2-1;
    }
}


int cal_ri(int n) {
    return n/2;
}


int main(int argc, char const *argv[]) {

    int tc;
    cin >> tc;

    for(int ti=1;ti<=tc;ti++) {

        int n,k;
        cin >> n >> k;
        node_t tmp;
        tmp.l = n;
        tmp.c = 1;

        tmp.le = cal_le(n);
        tmp.ri = cal_ri(n);

        tmp.min = min(tmp.le,tmp.ri);
        tmp.max = max(tmp.le,tmp.ri);



        priority_queue<node_t> q;
        q.push(tmp);

        while(true) {
            node_t now = q.top();
            q.pop();

            k -= now.c;

            if(k<=0) {
                cout << "Case #" << ti << ": "<< now.max <<" " << now.min << endl;
                break;
            }

            if((now.l%2)==1) {
                node_t ne;
                ne.l = now.le;
                ne.c = now.c*2;
                ne.le = cal_le(ne.l);
                ne.ri = cal_ri(ne.l);
                ne.min = min(ne.le,ne.ri);
                ne.max = max(ne.le,ne.ri);
                q.push(ne);
            } else {
                node_t ne;
                ne.l = now.le;
                ne.c = now.c;
                ne.le = cal_le(ne.l);
                ne.ri = cal_ri(ne.l);
                ne.min = min(ne.le,ne.ri);
                ne.max = max(ne.le,ne.ri);
                q.push(ne);

                ne.l = now.ri;
                ne.c = now.c;
                ne.le = cal_le(ne.l);
                ne.ri = cal_ri(ne.l);
                ne.min = min(ne.le,ne.ri);
                ne.max = max(ne.le,ne.ri);
                q.push(ne);
            }


        }


    }


    return 0;
}
