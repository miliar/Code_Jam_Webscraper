/*
 * pflip.cpp
 * 
 * Created by: Ashik <ashik@KAI10>
 * Created on: Sat, 08 Apr 2017
 */


#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define mem(list, val) memset(list, (val), sizeof(list))
#define pb push_back

bool allPlus(string s)
{
    for(int i=0; i<s.size(); i++) if(s[i] != '+') return false;
    return true;
}

bool allNeg(string s)
{
    for(int i=0; i<s.size(); i++) if(s[i] != '-') return false;
    return true;
}

int firstNeg(string s)
{
    int lim = s.size()/2;
    for(int i=0; i<lim; i++){
        if(s[i] == '-') return i;
        else if(s[s.size()-i-1] == '-') return s.size()-i-1;
    }
    return lim;
}

int simpleFirstNeg(string s)
{
    if(s[0] == '-') return 0;
    if(s.back() == '-') return s.size()-1;
}

int solve(string s, int k, int ret)
{
    if(s.size() == 0 || allPlus(s)) return ret;
    if(s.size() < k) return -1;
    if(s.size() == k){
        if(allPlus(s)) return ret;
        if(allNeg(s)) return ret+1;
        return -1;
    }
    
    int start = simpleFirstNeg(s);
    if(start == 0){
        for(int i=0; i<k; i++) s[i] = (s[i] == '+')? '-': '+';
    }
    else{
        for(int i=s.size()-1, c=0; c<k; c++, i--) s[i] = (s[i] == '+')? '-': '+';
    }

    string nw = "";
    while(s.back() == '+') s.pop_back();
    for(start=0; start<s.size(); start++){
        if(s[start] == '-') break;
    }

    for(int i=start; i<s.size(); i++) nw.push_back(s[i]);
    return solve(nw, k, ret+1);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    
    int cs=0,t;
    scanf("%d", &t);
    while(t--){
        string s;
        int k;
        cin >> s >> k;

        reverse(s.begin(), s.end());
        while(s.back() == '+') s.pop_back();
        reverse(s.begin(), s.end());
        while(s.back() == '+') s.pop_back();

        int ans = solve(s, k, 0);
        if(ans == -1) printf("Case #%d: IMPOSSIBLE\n", ++cs);
        else printf("Case #%d: %d\n", ++cs, ans);
    } 
    
    
    //cout << solve("-+-+-", 4, 0) << endl;
    //cout << firstNeg("++-++") << ' ' << firstNeg("+----++") << ' ' << firstNeg("+-----") << endl;
    return 0;
}
