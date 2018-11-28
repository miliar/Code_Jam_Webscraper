#include <bits/stdc++.h>
using namespace std;

const string IMP="IMPOSSIBLE";

typedef pair<int, char> pc;

string AB2(char A, char B, int N)
{
    stringstream ss;
    for(int i=0; i<N; i++)
    {
        ss << A;
        ss << B;
    }
    return ss.str();
}

string solveRYB(int R, int Y, int B)
{
    //cerr << R << ' ' << Y << ' ' << B << endl;

    int N=R+Y+B;
    int _mx=max(R, max(Y, B));
    if(2*_mx>N) return IMP;

    pc p[3]={{R, 'R'}, {Y, 'Y'}, {B, 'B'}};
    sort(p, p+3);

    stringstream ss;

    pc& u=p[2];
    pc& v=p[1];
    pc& r=p[0];

    int d=v.first-r.first;
    ss << AB2(u.second, v.second, d);
    u.first-=d;
    v.first-=d;

   // cerr << ss.str() << endl;;

    int dd=u.first/2;

    //cerr << u.second << ' ' << v.second << ' ' << r.second << endl;

    ss<<AB2(u.second, v.second, dd);
    ss<<AB2(u.second, r.second, dd);

    //cerr << ss.str() << endl;;

    u.first-=2*dd;
    v.first-=dd;
    r.first-=dd;

    if(u.first>0)
    {
        ss<<u.second;
    }

    ss<<AB2(v.second, r.second, v.first);
   // cerr << ss.str() << endl;;

    return ss.str();
}

string AB(char A, char B, int N)
{
    stringstream ss;
    ss << A;
    for(int i=0; i<N; i++)
    {
        ss << B;
        ss << A;
    }
    return ss.str();
}

int cnt(const string& s, char c)
{
    int res=0;
    for(char cc: s)
    {
        if(cc==c) res++;
    }
    return res;
}

string solve(int N, int R, int O, int Y, int G, int B, int V)
{
    //cout << N << ' ' << R << ' ' << O << ' ' << Y << ' ' << G << ' ' << B << ' ' << V << endl;

    if(B<O) return IMP;
    if(Y<V) return IMP;
    //cout << (R<G) << endl;
    if(R<G) return IMP;
    //cout << "HERE" << endl;

    int _B=B==O && B>0,
        _Y=Y==V && Y>0,
        _R=R==G && R>0;



    if(_B+_Y+_R>1) return IMP;
    if(_B+_Y+_R==1)
    {
        string ans;

        if(_B)
        {
            ans=AB2('B', 'O', B);
        }
        if(_Y)
        {
            ans=AB2('Y', 'V', Y);
        }
        if(_R)
        {
            ans=AB2('R', 'G', R);
        }

        if((int)ans.size()!=N) return IMP;
        return ans;
    }
    //else (_B+_Y+_R==0)

    int B_new=B-O;
    int Y_new=Y-V;
    int R_new=R-G;

    string s=solveRYB(R_new, Y_new, B_new);

    if(s==IMP) return IMP;
    assert((int)s.size()==B_new+R_new+Y_new);
    //cerr << "RYB SOLVE:: " << s << endl;

    bool _b=false, _y=false, _r=false;

    stringstream res;
    for(int i=0; i<(int)s.size(); i++)
    {
        if(!_b && s[i]=='B')
        {
            _b=true;
            res<<AB('B', 'O', O);
        }
        else if(!_y && s[i]=='Y')
        {
            _y=true;
            res<<AB('Y', 'V', V);
        }
        else if(!_r && s[i]=='R')
        {
            _r=true;
            res<<AB('R', 'G', G);
        }
        else res << s[i];
    }

    auto r=res.str();
    //cerr << "res::" << r << endl;

    /*
    assert((int)r.size()==N);
    assert(cnt(r, 'R')==R);
    assert(cnt(r, 'O')==O);
    assert(cnt(r, 'Y')==Y);
    assert(cnt(r, 'G')==G);
    assert(cnt(r, 'B')==B);
    assert(cnt(r, 'V')==V);
    */

    return r;
}

void check(char A, char B)
{
    if(A=='O') assert(B=='B');
    if(A=='V') assert(B=='Y');
    if(A=='G') assert(B=='R');

    assert(A!=B);

    if(A=='R') assert(B!='O');
    if(A=='R') assert(B!='V');

    if(A=='Y') assert(B!='O');
    if(A=='Y') assert(B!='G');

    if(A=='B') assert(B!='G');
    if(A=='b') assert(B!='V');
}

void check(string r, int N, int R, int O, int Y, int G, int B, int V)
{
    cerr << r << endl;;

    assert((int)r.size()==N);
    assert(cnt(r, 'R')==R);
    assert(cnt(r, 'O')==O);
    assert(cnt(r, 'Y')==Y);
    assert(cnt(r, 'G')==G);
    assert(cnt(r, 'B')==B);
    assert(cnt(r, 'V')==V);

    for(int i=0; i+1<N; i++)
    {
        check(r[i], r[i+1]);
    }
    check(r[0], r[N-1]);
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    //cout
    for(int t=1; t<=T; t++)
    {
        //int N;
        //cin >> N;
        //int result=solve(N);
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;

        string res=solve(N, R, O, Y, G, B, V);
        if(res!=IMP) check(res, N, R, O, Y, G, B, V);


        cout << "Case #" << t << ": " << res << endl;
    }
    return 0;
}
