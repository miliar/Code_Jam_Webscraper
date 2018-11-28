#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t, k, cnt;
    string s;
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cnt = 0;
        cin >> s >> k;
        int j = 0;
        while(j < s.length()){
            if (s[j] == '+')j ++;
            else {
                if(s.length()-j < k)break;
                cnt ++;
                for (int l = 0; l < k ; l++, j++){
                    if (s[j] == '+')s[j] = '-';
                    else s[j] = '+';
                }
                j -= k-1;
            }
        }
        printf("Case #%d: ",i+1);
        if (j == s.length())printf("%d\n",cnt);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
