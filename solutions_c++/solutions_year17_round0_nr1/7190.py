/* Bismillahir Rahmanir Rahim */

#include <bits/stdc++.h>

#define rep(i, n)	for(int i=0;i<n;i++)
#define repn(i, n)	for(int i=1;i<=n;i++)
#define set(i, n)	memset(i, n, sizeof(i))

#define pb	push_back

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

int main(){
    int tc, k, cas=1;
    string str;
    cin >> tc;
    while(tc--){
        cin >> str >> k;
        int ret = 0;
        rep(i, str.size()){
            if(i + k > str.size()) break;
            if(str[i] == '+') continue;
            ret++;
            for(int j=i;j<i+k;j++){
                if(str[j] == '-') str[j] = '+';
                else str[j] = '-';
            }
        }
        bool flag = true;
        rep(i, str.size()) if(str[i] == '-') flag = false;
        printf("Case #%d: ", cas++);
        if(flag == 0) printf("IMPOSSIBLE\n");
        else printf("%d\n", ret);
    }
	return 0;
}

