#include<bits/stdc++.h>
using namespace std;
int R, C;
char arr[5][101];
string board[51][32][32][32]; //in i col, beam at j is comming, k is vulnerable ( do not shoot on k), fill fucking f
pair<int, pair<int, int> > camefrom[51][32][32][32];
vector<string> manipulateb(string col)
{
    vector<string> x;
    if(col== "")
    {
        x.push_back("");
        return x;
    }
    else if(col[0]=='-' || col[0]=='|')
    {
        string c2;
        for(int i=1; i<col.size(); ++i) c2+=col[i];
        vector<string> x2 = manipulateb(c2);
        for(auto xv: x2)
        {
            x.push_back("-" + xv);
            x.push_back("|" + xv);
        }
    }
    else
    {
        string c2;
        for(int i=1; i<col.size(); ++i) c2+= col[i];
        vector<string> x2 = manipulateb(c2);
        for(auto xv: x2)
            x.push_back(col[0]+xv);
        
    }
    return x;
}
vector<pair<string, int> > manipulate(string col2)
{
    vector<pair<string, int> > ansr;
    vector<string> xv = manipulateb(col2);
    for(auto col: xv)
    {
        bool cover[5];
        for(int i=0; i<col.size(); ++i) cover[i] = (col[i]!='.');
        bool ff = false;
        bool flag = false;
        for(int i=0; i<col.size(); ++i)
        {
            if(col[i]=='#') ff = false;
            cover[i] |= ff;
            if(col[i]=='-' || col[i]=='|')
            {
                if(ff)
                {
                    flag = true; break;
                }
            }
            if(col[i]=='|')
                ff = true;
        }
        if(flag) continue;
        ff = false;
        for(int i=col.size()-1; i>=0; --i)
        {
            if(col[i]=='#') ff = false;
            cover[i] |= ff;
            if(col[i]=='-' || col[i]=='|')
            {
                if(ff)
                {
                    flag = true; break;
                }
            }
            if(col[i]=='|')
                ff = true;
        }
        if(flag) continue;
        int ans = 0;
        for(int i=0; i<col.size(); ++i) ans += (cover[i]) << i;
        ansr.emplace_back(col, ans);
    }
    return ansr;
}
void tmain()
{
    scanf("%d%d",&R,&C);
    for(int i=0; i<R; ++i) scanf("%s", arr[i]);
    for(int i=0; i<=C; ++i)
        for(int j=0; j<(1<<R); ++j)
            for(int k=0; k<(1<<R); ++k)
            for(int s=0; s<(1<<R); ++s)
                board[i][j][k][s] = "";
    for(int i=0; i<R; ++i) board[0][0][0][(1<<R)-1] += "#";
    
    for(int i=0; i<C; ++i)
        for(int j=0; j<(1<<R); ++ j)
        {
            for(int k=0; k<(1<<R); ++k)
            {
                for(int f=0; f<(1<<R); ++f)
                {
                    if(board[i][j][k][f]=="") continue;
                    cerr << i << " " << j << " " << k << " " << f << endl;
                    bool beam[5];
                    for(int s=0; s<R; ++s) beam[s] = j&(1<<s);
                    bool vuln[5];
                    for(int s=0; s<R; ++s) vuln[s] = k&(1<<s);
                    bool fill[5];
                    for(int s=0; s<R; ++s) fill[s] = f&(1<<s);
                    
                    string col = "";
                    for(int s=0; s<R; ++s) col += arr[s][i];
                    
                    cerr << "ERR1"<<endl;
                    vector<pair<string, int> > vcol = manipulate(col);
                    cerr << "ERR2"<<endl;
                    for(auto x: vcol)
                        cerr << x.first << " " << x.second << endl;
                    for(auto x: vcol)
                    {
                        cerr << "ERR3"<<endl;
                        bool beamt[5]; for(int s=0; s<R; ++s) beamt[s] = beam[s];
                        bool vulnt[5]; for(int s=0; s<R; ++s) vulnt[s] = vuln[s];
                        bool fillt[5]; for(int s=0; s<R; ++s) fillt[s] = fill[s] && (x.second&(1<<s));
                        bool flag = false;
                        for(int s=0; s<R; ++s)
                        {
                            if(beam[s] && (x.first[s]=='-' || x.first[s]=='|')) flag = true;
                            if(vuln[s] && (x.first[s]=='-')) flag = true;
                            fillt[s] |= beamt[s];
                            cerr<<fillt[s]<<endl;
                        }
                        cerr << "ERR4"<<endl;
                        if(flag) continue;
                        cerr << "ERR5"<<endl;
                        for(int s=0; s<R; ++s)
                        {
                            if(x.first[s]=='#')
                            {
                                beamt[s] = vulnt[s] = false;
                                cerr<<s<<fillt[s]<<endl;
                                if(!fillt[s]) flag = true;
                            }
                            if(x.first[s]=='-' || x.first[s]=='|') vulnt[s] = true;
                            if(x.first[s]=='-') beamt[s] = fillt[s] = true;
                        }
                        if(flag) continue;
                        cerr << "ERRS"<<endl;
                        int beamv = 0, vulnv = 0, fillv = 0;
                        for(int s=0; s<R; ++s) beamv += beamt[s] << s;
                        for(int s=0; s<R; ++s) vulnv += vulnt[s] << s;
                        for(int s=0; s<R; ++s) fillv += fillt[s] << s;
                        board[i+1][beamv][vulnv][fillv] = x.first;
                        camefrom[i+1][beamv][vulnv][fillv] = make_pair(j, make_pair(k, f));
                    }
                    cerr << "ERR6"<<endl;
                }
            }
        }
    
    cerr << "ERR7"<<endl;
    vector<string> ans;
    for(int j=0; j<(1<<R); ++j)
        for(int k=0; k<(1<<R); ++k)
        for(int f=(1<<R)-1; f<(1<<R); ++f)
        {
            if(board[C][j][k][f]!="")
            {
                cerr << "ERR8" << endl;
                cerr << board[C][j][k][f] << endl;
                cerr << "ERR9" << endl;
                ans.push_back(board[C][j][k][f]); 
                for(int i=C-1; i>0; --i)
                {
                    auto v =  camefrom[i+1][j][k][f];
                    j = v.first; k = v.second.first, f= v.second.second;
                    ans.push_back(board[i][j][k][f]);
                }
                puts("POSSIBLE");
                reverse(ans.begin(), ans.end());
                for(int i=0; i<R; ++i)
                {
                    for(int j=0; j<C; ++j)
                    {
                        cout << ans[j][i];
                    }
                    cout << endl;
                }
                return;
            }
        }
    puts("IMPOSSIBLE");
    return;
}

#include <sys/resource.h>
int main()
{
    const rlim_t kStackSize = 64L * 1024L * 1024L;   // min stack size = 64 Mb
    struct rlimit rl;
    int result;

    result = getrlimit(RLIMIT_STACK, &rl);
    if (result == 0)
    {
        if (rl.rlim_cur < kStackSize)
        {
            rl.rlim_cur = kStackSize;
            result = setrlimit(RLIMIT_STACK, &rl);
            if (result != 0)
            {
                fprintf(stderr, "setrlimit returned result = %d\n", result);
            }
        }
    }

    int T;
    scanf("%d",&T);
    for(int tc=1; tc<=T; ++tc)
    {
        cerr << tc << endl;
        printf("Case #%d: ", tc);
        tmain();
    }
    return 0;
}







