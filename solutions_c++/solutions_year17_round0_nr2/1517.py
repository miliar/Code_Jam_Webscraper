#include <cstdio>
#include <cstring>
using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    for(int NCASE=1; NCASE<=T; ++NCASE) {
        char num[20];
        scanf("%s", num);
        int n = strlen(num);
        for(int i=n-2; i>=0; --i) {
            if( num[i] > num[i+1] ) {
                num[i] = num[i] - 1;
                for(int j=i+1; j<n; ++j)
                    num[j] = '9';
            }
        }
        int start = 0;
        while( num[start] == '0' )
            ++start;
        printf("Case #%d: %s\n", NCASE, num+start);
    }
    return 0;
}
