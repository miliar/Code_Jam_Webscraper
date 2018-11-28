#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define d(x) cout << #x << "=" << x << "\n"

vector <char> stable;
vector <char> ord;
int t;
int n;
int r,o,y,g,b,v;
int R,O,Y,G,B,V,N;
int maks;

bool c(char a,char bb)
{
    int aaa,bbb;
    if (a=='R')
        aaa=R;
    if (a=='Y')
        aaa=Y;
    if (a=='B')
        aaa=B;
    if (bb=='R')
        bbb=R;
    if (bb=='Y')
        bbb=Y;
    if (bb=='B')
        bbb=B;
    return aaa>bbb;
}

void up()
{
    R=r-g;
    Y=y-v;
    B=b-o;
    N=R+Y+B;
    maks=max(max(R,Y),B);
    R=r;
    Y=y;
    B=b;
    sort(ord.begin(),ord.end(),c);
   /* d(R);
    d(Y);
    d(B);*/
    R=r-g;
    Y=y-v;
    B=b-o;
    /*d(R);
    d(Y);
    d(B);
    d(ord[0]);
    if(stable.size()>0)
        d(stable.back());*/
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> t;
    ord.push_back('B');
    ord.push_back('Y');
    ord.push_back('R');
    for (int i=0;i<t;i++)
    {
        stable.resize(0);
        cin >> n >> r >> o >> y >> g >> b >> v;
        up();
        if (min(min(R,Y),B)<0 || maks>N-maks || N-maks>2*maks)
            cout << "Case #" << i+1 << ": IMPOSSIBLE\n";
        else
        {
            if(ord[0]=='R')
            {
                if (g>0)
                {
                    stable.push_back('R');
                    stable.push_back('G');
                    stable.push_back('R');
                    g--;
                    r-=2;
                }
                else
                {
                    stable.push_back('R');
                    r--;
                }
            }
            if(ord[0]=='B')
            {
                if (o>0)
                {
                    stable.push_back('B');
                    stable.push_back('O');
                    stable.push_back('B');
                    o--;
                    b-=2;
                }
                else
                {
                    stable.push_back('B');
                    b--;
                }
            }
            if(ord[0]=='Y')
            {
                if (v>0)
                {
                    stable.push_back('Y');
                    stable.push_back('V');
                    stable.push_back('Y');
                    v--;
                    y-=2;
                }
                else
                {
                    stable.push_back('Y');
                    y--;
                }
            }
            up();
            while (r+y+b+o+g+v>0)
            {
                //d(maks);
                if (max(max(r,y),b)==0)
                {
                    if (v>0)
                    {
                        v--;
                        stable.push_back('V');
                    }
                    if (g>0)
                    {
                        g--;
                        stable.push_back('G');
                    }
                    if (o>0)
                    {
                        o--;
                        stable.push_back('O');
                    }
                }
                else if (stable.back()!=ord[0])
                {
                    if(ord[0]=='R')
                    {
                        if (g>0 && stable.back()!='R')
                        {
                            stable.push_back('R');
                            stable.push_back('G');
                            stable.push_back('R');
                            g--;
                            r-=2;
                        }
                        else
                        {
                            stable.push_back('R');
                            r--;
                        }
                    }
                    if(ord[0]=='B')
                    {
                        if (o>0 && stable.back()!='B')
                        {
                            stable.push_back('B');
                            stable.push_back('O');
                            stable.push_back('B');
                            o--;
                            b-=2;
                        }
                        else
                        {
                            stable.push_back('B');
                            b--;
                        }
                    }
                    if(ord[0]=='Y')
                    {
                        if (v>0 && stable.back()!='Y')
                        {
                            stable.push_back('Y');
                            stable.push_back('V');
                            stable.push_back('Y');
                            v--;
                            y-=2;
                        }
                        else
                        {
                            stable.push_back('Y');
                            y--;
                        }
                    }
                }
                else
                {
                    if(ord[1]=='R' )
                    {
                        if (g>0 && stable.back()!='R')
                        {
                            stable.push_back('R');
                            stable.push_back('G');
                            stable.push_back('R');
                            g--;
                            r-=2;
                        }
                        else
                        {
                            stable.push_back('R');
                            r--;
                        }
                    }
                    if(ord[1]=='B')
                    {
                        if (o>0 && stable.back()!='B')
                        {
                            stable.push_back('B');
                            stable.push_back('O');
                            stable.push_back('B');
                            o--;
                            b-=2;
                        }
                        else
                        {
                            stable.push_back('B');
                            b--;
                        }
                    }
                    if(ord[1]=='Y')
                    {
                        if (v>0 && stable.back()!='Y')
                        {
                            stable.push_back('Y');
                            stable.push_back('V');
                            stable.push_back('Y');
                            v--;
                            y-=2;
                        }
                        else
                        {
                            stable.push_back('Y');
                            y--;
                        }
                    }
                }
                up();
            }
            int q=stable.size();
            if (stable[q-1]==stable[0])
                swap(stable[q-1],stable[q-2]);
            cout << "Case #" << i+1 << ": ";
            for (int j=0;j<n;j++)
            {
                cout << stable[j];
            }
            cout << "\n";
        }
    }
    return 0;
}
