#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
using namespace std;
string gener(int a,int b,int c)
{
    int now=0;
    int g[3];
    char cx[3];
    g[0]=a;g[1]=b;g[2]=c;
    cx[0]='R';cx[1]='Y';cx[2]='B';
    string res="";
    if (a>=max(b,c)){now=0;}
    if (b>=max(a,c)){now=1;}
    if (c>=max(a,b)){now=2;}
    while(g[0]>0||g[1]>0||g[2]>0)
    {
        res+=cx[now];
        g[now]--;
        now++;
        now%=3;
        if (g[now]<g[(now+1)%3]){now=(now+1)%3;}
    }
    if (res[0]==res[res.length()-1]&&res.length()>1)
    {
        if (res.length()<=3){return "-1";}
        if (res[2]!=res[0]){swap(res[0],res[1]);}
        else
        if (res[res.length()-3]!=res[res.length()-1]) {swap(res[res.length()-2],res[res.length()-1]);}
    }
    return res;
}
bool good(string s)
{
    s+=s[0];
    for (int i=0;i<s.length()-1;i++)
    {
        if (s[i]==s[i+1]){cout << "badstring" << s.substr(0,s.length()-1);}
        if (s[i]=='O'&&s[i+1]=='R'){cout << "badstring" << s.substr(0,s.length()-1);exit(0);}
        if (s[i]=='O'&&s[i+1]=='Y'){cout << "badstring" << s.substr(0,s.length()-1);exit(0);}
        if (s[i]=='G'&&s[i+1]=='Y'){cout << "badstring" << s.substr(0,s.length()-1);exit(0);}
        if (s[i]=='G'&&s[i+1]=='B'){cout << "badstring" << s.substr(0,s.length()-1);exit(0);}
        if (s[i]=='V'&&s[i+1]=='B'){cout << "badstring" << s.substr(0,s.length()-1);exit(0);}
        if (s[i]=='V'&&s[i+1]=='R'){cout << "badstring" << s.substr(0,s.length()-1);exit(0);}
        if (s[i+1]=='O'&&s[i]=='R'){cout << "badstring" << s.substr(0,s.length()-1);exit(0);}
        if (s[i+1]=='O'&&s[i]=='Y'){cout << "badstring" << s.substr(0,s.length()-1);exit(0);}
        if (s[i+1]=='G'&&s[i]=='Y'){cout << "badstring" << s.substr(0,s.length()-1);exit(0);}
        if (s[i+1]=='G'&&s[i]=='B'){cout << "badstring" << s.substr(0,s.length()-1);exit(0);}
        if (s[i+1]=='V'&&s[i]=='B'){cout << "badstring" << s.substr(0,s.length()-1);exit(0);}
        if (s[i+1]=='V'&&s[i]=='R'){cout << "badstring" << s.substr(0,s.length()-1);exit(0);}
    }
    return 1;
}

int main()
{
    freopen("a","r",stdin);
    freopen("b","w",stdout);
    int t;
    cin >> t;
    int g=1;
    while(t--)
    {
        cout << "Case #" << g << ": ";
        g++;
        int r,o,y,g,b,v;
        int n;
        cin >> n;
        cin >> r >> o >> y >> g >> b >> v;
        //o=ry
        //g=yb
        //v=br
        if ((o+g+y)*2>n){cout << "IMPOSSIBLE" << endl;continue;}
        if ((o+v+r)*2>n){cout << "IMPOSSIBLE" << endl;continue;}
        if ((v+g+b)*2>n){cout << "IMPOSSIBLE" << endl;continue;}
        if (o>b){cout << "IMPOSSIBLE" << endl;continue;}
        if (g>r){cout << "IMPOSSIBLE" << endl;continue;}
        if (v>y){cout << "IMPOSSIBLE" << endl;continue;}
        if (o==b&&o>0)
        {
            if (o+b-n){cout << "IMPOSSIBLE" << endl;continue;}
            for (int i=0;i<o;i++){cout << "OB";}cout << endl;continue;
        }
        if (r==g&&r>0)
        {
            if (r+g-n){cout << "IMPOSSIBLE" << endl;continue;}
            for (int i=0;i<r;i++){cout << "RG";}cout << endl;continue;
        }
        if (v==y&&v>0)
        {
            if (v+y-n){cout << "IMPOSSIBLE" << endl;continue;}
            for (int i=0;i<v;i++){cout << "VY";}cout << endl;continue;
        }
        string res1="";
        string res2="";
        string res3="";
        if (o)
        {
            res1+="B";
            b--;
            while(o--)
            {
                res1+="OB";
                b--;
            }
        }
        if (g)
        {
            res2+="R";
            r--;
            while(g--)
            {
                res2+="GR";
                r--;
            }
        }
        if (v)
        {
            res3+="Y";
            y--;
            while(v--)
            {
                res3+="VY";
                y--;
            }
        }
string        res4=gener(r,y,b);
        if (res4=="-1"){cout << "IMPOSSIBLE" << endl;continue;}
        cout << res4 << endl;
    }
    return 0;
}
