#include <bits/stdc++.h>
#define int long long
#define P(x) cout << x << endl
#define D(x) P(#x << ": " << x)
#define F(i,n) for (int i=0; i<(int)(n); i++)
#define DEC(i,n) for (int i=(int)(n); --i>=0;)
#define $(s) (int)((s).size())
#define ALL(v) v.begin(), v.end()
#define V vector
#define pb push_back
using namespace std;
void MI(int &a, int v) {a = min(a,v);}
void MA(int &a, int v) {a = max(a,v);}

// a = safe color
string spec(int a, int b, string aa, string bb) {
    string s;
    if (b != a) return "";
    F(i,a) s += aa, s += bb;
    return s;
}

V<string> prepare(int a, int b, string aa, string bb) {
    if (a+b == 0) return {};
    //P("B");
    V<string> v;
    F(i,a-b) v.pb(""+aa);
    F(i,b) v.back() += bb, v.back() += aa;
    //P("C");
    return v;
}

string mixer(V<string> a[3]) {
    //P("hey");
    if ($(a[0]) < $(a[1])) swap(a[0],a[1]);
    if ($(a[0]) < $(a[2])) swap(a[0],a[2]);
    //for (string s : a[0]) D(s);
    int n = $(a[0]) + $(a[1]) + $(a[2]);
    string s = a[0].back(); a[0].pop_back();
    int last=0;
    n--;
    F(i,n) {
        int ma=0, ch=-1;
        //D(i), D(last);
        //P($(a[0])<<" "<<$(a[1])<<" "<<$(a[2]));
        F(j,3) if (last != j && $(a[j]) > ma)
            ma = $(a[j]), ch=j;
        //D(ch);
        //P("");
        if (ma) {
            s += a[ch].back();
            a[ch].pop_back();
        } else return "";
        last = ch;
    }
    //D(last);
    if (last == 0) return "";
    return s;
}

string comp(int n, int r, int o, int y, int g, int b, int v) {
    string s;
    if (y+v == n) return spec(y,v,"Y","V");
    if (r+g == n) return spec(r,g,"R","G");
    if (b+o == n) return spec(b,o,"B","O");
    //P("A");
    if ((y+v && y <= v) || (r+g && r <= g) || (b+o && b <= o)) return "";
    //return spec(y,v,"Y","V") + spec(r,g,"R","G") + spec(b,o,"B","O");
    V<string> a[]{prepare(y,v,"Y","V"), prepare(r,g,"R","G"), prepare(b,o,"B","O")};
    return mixer(a);
}

signed main() {
    int nt; cin>>nt;
    F(tt,nt) {
        int n,r,o,y,g,b,v;
        cin>>n>>r>>o>>y>>g>>b>>v;
        cout<<"Case #"<<tt+1<<": ";
        string res = comp(n,r,o,y,g,b,v);
        if (res == "") P("IMPOSSIBLE");
        else P(res);
    }
}
