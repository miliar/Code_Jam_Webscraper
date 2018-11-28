#include <cstdio>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>

typedef long long ll;

#define REP(i,a) for(int i=0;i<a;++i)

using namespace std;

string s;
ifstream cinf;
ofstream coutf;

string solve(string s, bool fl)
{
    //cout << " String : " << s << endl;
    int sz = s.size();
    int LS, RS;
    int st_idx=0, en_idx=0;
    bool rst_st = true;
    int maxst_idx=0, maxed_idx=0;
    
    REP(i,sz)
    {
        if(s[i]=='.')
        {
            if(rst_st)
            {
                st_idx = i;
                rst_st = false;
            }
            en_idx = i;
        }
        else
        {
            rst_st = true;
            if((en_idx-st_idx) > (maxed_idx-maxst_idx))
            {
                maxst_idx=st_idx;
                maxed_idx=en_idx;
            }
        }
    }
    //cout << " Max st : " << maxst_idx << " Max end : " << maxed_idx << endl;
    int pos = (maxst_idx+maxed_idx)/2;
    if(fl)
    {
        LS = pos-maxst_idx;
        RS = maxed_idx-pos;
        coutf << max(LS, RS) << " " << min(LS,RS) << endl;
    }
    s[pos]='o';
    //cout << " String after change : " << s << endl;
    return s;
}

void create(ll n, ll k)
{
    s = "";
    s += "o";
    REP(i,n)
    s +=".";
    s += "o";
    
    REP(j, k-1)
    s = solve(s, false);
    solve(s,true);
    //cout << " String after final change : " << s << endl;
    
    return;
}



int main() {
    int T;
    ll N, K;
    
    cinf.open("A-small.in.txt");
    
    coutf.open("A-small.out.txt");
    
    cinf >> T;
    
    for (int ri = 1; ri <= T; ++ri) {
        cinf >> N >> K;
        coutf << "Case #" << ri << ": ";
        create(N, K);
    }
    //solve("o..o...o", 2);
    //create(N, K);
    return 0;
}

