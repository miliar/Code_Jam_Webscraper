/*
 * tidy.cpp
 * 
 * Created by: Ashik <ashik@KAI10>
 * Created on: Sat, 08 Apr 2017
 */


#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define mem(list, val) memset(list, (val), sizeof(list))
#define pb push_back

int main()
{
    freopen("B-large.in", "r", stdin);
    int t, cs = 0;
    scanf("%d", &t);
    while(t--){
        string s;
        cin >> s;
        
        for(int i=s.size()-1; i>=1; i--){
            if(s[i] >= s[i-1]) continue;
            s[i] = '9';
            s[i-1]--;
            for(int j=i+1; j<s.size(); j++) s[j] = '9';
        }

        std::reverse(s.begin(), s.end());
        while(s.back() == '0') s.pop_back();
        std::reverse(s.begin(), s.end());

        printf("Case #%d: %s\n", ++cs, s.c_str());
    } 
    return 0;
}
