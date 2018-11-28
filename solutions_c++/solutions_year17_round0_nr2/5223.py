#include <cstdio>
#include <deque>
using namespace std;
char s[22];
bool ok(deque<int>& dq) {
    for ( int i = 0 ; i <(int)dq.size()-1 ; i++ ) 
        if ( dq[i] > dq[i+1] ) return false;
    return true;
}
void print(deque<int>& dq) {
    for ( int i = 0 ; i < (int)dq.size() ; i++ ) 
        printf("%d",dq[i]);
    puts("");
}
int main() {
    int tc;
    scanf("%d",&tc);
    for ( int _tc = 1 ; _tc <= tc ; _tc++ ) {
        printf("Case #%d: ",_tc);
        scanf("%s",s);
        deque<int> dq;
        for ( int i = 0 ; s[i] ; i++ ) 
            dq.push_back(s[i]-'0');
        while ( !ok(dq) ) {
            for ( int i = 0 ; i < (int)dq.size()-1 ; i++ ) {
                if ( dq[i] > dq[i+1] ) {
                    dq[i]--;
                    for ( int j = i+1 ; j < (int)dq.size() ; j++ ) 
                        dq[j] = 9;
                    break;
                }
            }
            if ( dq.front() == 0 ) dq.pop_front();
        }
        print(dq);
    }
    return 0;
}
