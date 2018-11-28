#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int T;
    cin >> T;
    int R=0;
    int O=1;
    int Y=2;
    int G=3;
    int B=4;
    int V=5;
    for(int cs=1; cs<=T; cs++) {
        int N;
        cin >> N;

        printf("Case #%d: ", cs);

        vector<int> v(6);
        for(int i=0;i<6;i++) cin >> v[i];

        vector<int>::iterator it = max_element(v.begin(), v.end());
        int m = *it;
        if(m > N-m) {
            printf("IMPOSSIBLE\n");
        } else {
            vector<string> s(1002);

            int mm = it-v.begin();
            char mc[3];
            int mi[3];
            if(mm==0) {
                mc[0]='R'; mc[1]='Y'; mc[2]='B';
                mi[0]=v[R]; mi[1]=v[Y]; mi[2]=v[B];
            } else if(mm==2) {
                mc[0]='Y'; mc[1]='R'; mc[2]='B';
                mi[0]=v[Y]; mi[1]=v[R]; mi[2]=v[B];
            } else if(mm==4) {
                mc[0]='B'; mc[1]='R'; mc[2]='Y';
                mi[0]=v[B]; mi[1]=v[R]; mi[2]=v[Y];
            }

            for(int i=0;i<mi[0];i++) {
                s[i] += mc[0];
            }
            for(int i=0;i<mi[1];i++) {
                s[i] += mc[1];
            }
            for(int i=0;i<mi[2];i++) {
                s[m-1-i] += mc[2];
            }

            for(int i=0;i<m;i++) {
                printf("%s", s[i].c_str());
            }
            puts("");
        }
    }

    return 0;
}
