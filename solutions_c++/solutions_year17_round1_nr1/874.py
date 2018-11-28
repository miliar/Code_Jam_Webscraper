#include <iostream>
#include <vector>
#include <string>
using namespace std;
vector<string> v;
int r,c;


void f(int i, int j, char c) {
    while(j>=0) {
        v[i][j]=c;
        j--;
    }
}

void g(int i) {
    for(int j=0;j<c;j++) {
        v[i][j]=v[i+1][j];
    }
    if(i==0 or v[i-1][0]!='?') return;
    g(i-1);
}
void h(int i) {
    for(int j=0;j<c;j++) {
        v[i][j]=v[i-1][j];
    }
    if(i==r-1 or v[i+1][0]!='?') return;
    h(i+1);
}


int main() {
    int t;
    cin >>t;
    for(int tt=1;tt<=t;tt++) {
        cin>>r>>c;

        v.clear();
        v.resize(r);
        for(int i=0;i<r;i++) {
            cin>>v[i];
        }
        cout << "Case #" << tt << ":\n";
        char cur=' ';
        for(int i=0;i<r;i++) {
            cur=' ';
            for(int j=0;j<c;j++) {
                if(v[i][j]=='?') {
                    if(cur!=' ') v[i][j]=cur;
                }
                else {
                    if(cur==' ') f(i,j,v[i][j]);
                    cur = v[i][j];
                }
            }
        }

        for(int i=0;i<r;i++) {
            if(v[i][0]=='?' and i>0 and v[i-1][0]!='?') {
                h(i);
            }
            else if(v[i][0]=='?' and i<r and v[i+1][0]!='?') {
                g(i);
            }
        }

        for(int i=0;i<r;i++) {
            cout << v[i] << "\n";
        }
    }
    return 0;
}

