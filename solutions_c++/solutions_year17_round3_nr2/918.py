#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

const int DAY = 1440, HALF=DAY/2;

int flag[3003];

int main() {
    //freopen("in.txt", "r", stdin);
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int cases;cin>>cases;
    for(int caseno=1;caseno<=cases;caseno++) {
        int b1,e1, b2,e2;
        int s1,s2, m1,m2;
        int x, y, ans;
        cin>>x>>y;
        if(x && y) {
            cin>>b1>>e1;
            cin>>b2>>e2;
            if(b2<=e1) {
                swap(b1,b2);
                swap(e1,e2);
            }

            s1 = e1-b1;
            s2 = e2-b2;
            m1 = b2-e1;
            m2 = DAY-(s1+s2+m1);

            ans = 2;
            goto END;
        }
        if(y)x=y;

        if(x==2) {
            cin>>b1>>e1;
            cin>>b2>>e2;
            if(b2<=e1) {
                swap(b1,b2);
                swap(e1,e2);
            }

            s1 = e1-b1;
            s2 = e2-b2;
            m1 = b2-e1;
            m2 = DAY-(s1+s2+m1);
            if(m1>=HALF || m2>=HALF) {
                ans = 2;
            }
            else {
                ans = 4;
            }
            goto END;
        }

        {
            cin>>b1>>e1;
            ans = 2;
        }

    END:
        printf("Case #%d: %d\n", caseno, ans);
    }

    return 0;
}
