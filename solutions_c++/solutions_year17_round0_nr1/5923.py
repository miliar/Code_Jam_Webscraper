#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

int fminus(string s){
    for (int i = 0; i < s.size(); i++)
        if(s[i] == '-') return i;
    return -1;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T, k;
    string s;
    scanf("%d",&T);
    for (int t = 0; t < T; t++){
        cin >> s >> k;
        int indx = fminus(s);
        int cnt = 0;
        while(indx != -1 && indx + k <= s.size()){
            cnt++;
            for (int j = indx; j < indx + k; j++)
                s[j] = s[j] == '-' ? '+' : '-';
            indx = fminus(s);
        }
        if(indx == -1) printf("Case #%d: %d\n",t+1,cnt);
        else printf("Case #%d: IMPOSSIBLE\n",t+1);
    }
    return 0;
}
