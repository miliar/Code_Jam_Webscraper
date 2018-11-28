#include <iostream>
#include <string>
using namespace std;
int ans(string &s, int k ) {
    int ans = 0;
    for (int i = 0; i<= s.size()-k; i++)
        if (s[i] == '-') {
            ans ++;
            for (int j = i; j<k+i; j++)
                if (s[j] =='-') s[j] = '+'; else s[j] = '-';
        }
    for (int i = s.size()-k+1; i<s.size(); i++) 
        if (s[i] =='-') return -1;
    return ans;
}
using namespace std;
int main() {
    int nn;
    cin >> nn;
    for (int i = 1 ; i <= nn; i++) {
        printf("Case #%d: ",i);
        string s;
        int k;
        cin >> s >> k;
        int q = ans(s,k);
        if (q>=0)
            printf("%d\n",q);
        else
            printf("IMPOSSIBLE\n");
    }
}
