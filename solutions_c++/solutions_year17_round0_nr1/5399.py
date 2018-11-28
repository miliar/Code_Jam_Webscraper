#include <bits/stdc++.h>
using namespace std;
int K;
int ans;
unordered_set<string> doneSet;
void flip(string &s, int p, bool dir) {
    if(dir) {
        p+=K-1;
        p=min(p, (int)s.size()-1);
        for(int i=0; i<K; i++) {
            if(s[p-i]=='-') s[p-i]='+';
            else s[p-i]='-';
        }
    } else {
        p-=K-1;
        p=max(p, 0);
        for(int i=0; i<K; i++) {
            if(s[p+i]=='-') s[p+i]='+';
            else s[p+i]='-';
        }
    }
}
bool isdone(string &s){
    for(int i=0; i<s.size(); i++) {
        if(s[i]=='-') return false;
    }
    return true;
}

void solve(string &s, int k) {
    if(s.size()<K) {
        ans=1E9;
        return;
    }
    if(isdone(s)) {
        ans = min(ans, k);
        return;
    }
    if(doneSet.find(s) != doneSet.end()) return;
    doneSet.insert(s);
    for(int i=0; i<s.size(); i++) {
        if(s[i]=='-') {
            flip(s,i, true);
            solve(s, k+1);
            flip(s,i, true);
        }
    }
    for(int i=s.size()-1; i>=0; i--) {
        if(s[i]=='-') {
            flip(s,i, false);
            solve(s, k+1);
            flip(s,i, false);
        }
    }
}

int main(int argc, char *argv[])
{
    int Q;
    ifstream infile;
    ofstream outfile;
    infile.open("input.in");
    outfile.open("output.txt");
    infile>>Q;
    for(int i=1;i<=Q;i++) {
        string s;
        infile>>s;
        infile>>K;
        ans=1E9;
        doneSet.clear();
        solve(s, 0);
        if(ans != 1E9)
            outfile<<"Case #"<<i<<": "<<ans<<endl;
        else
            outfile<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
    }

    return 0;
}
