#include<bits/stdc++.h>

using namespace std;

int r,o,y,g,b,v;

string gr,vi,ora;

string gen ( int r , int b , int y , int st , int ed )
{
    string col = "";
    char last;
    if ( st == 1 )  col = "R",r--;
    if ( st == 2 )  col = "B",b--;
    if ( st == 3 )  col = "Y",y--;
    if ( ed == 1 )  last = 'R',r--;
    if ( ed == 2 )  last = 'B',b--;
    if ( ed == 3 )  last = 'Y',y--;
    while(r+b+y > 0)
    {
        if ( col.back() == 'R' )
        {
            if ( b > y or (b==y and ed==2) )
            {
                col+="B";
                b--;
            }
            else
            {
                col+="Y";
                y--;
            }
        }
        else if ( col.back() == 'B' )
        {
            if ( r > y or (r==y and ed==1) )
            {
                col+="R";
                r--;
            }
            else
            {
                col+="Y";
                y--;
            }
        }
        else
        {
            if ( r > b or (r==y and ed==1) )
            {
                col+="R";
                r--;
            }
            else
            {
                col+="B";
                b--;
            }
        }
    }
    if ( r==0 and b==0 and y==0 and last != col.back() )   return col+last;
    return "F";
}

void solve(int t)
{
    int n;
    cin >> n;
    cin >> r >> o >> y >> g >> b >> v;
    /*if ( o > b or g > r or v > y )
    {
        printf("Case #%d: IMPOSSIBLE\n");
        return;
    }
    gr = vi = ora = "";
    if ( o > 0 )
    {
        ora = "B";
        for ( int c=1 ; c<=o ; c++ )    ora += "OB";
        b -= o+1;
    }
    if ( g > 0 )
    {
        gr = "R";
        for ( int c=1 ; c<=g ; c++ )    gr += "GR";
        r -= g+1;
    }
    if ( v > 0 )
    {
        vi = "Y";
        for ( int c=1 ; c<=v ; c++ )    vi += "VY";
        y -= v+1;
    }
    int prio;*/
    /// color r=1 b=2 y=3
    /*for ( int c=1 ; c<=3; c++ )
    {
        for ( int d=1 ; d<=3 ; d++ )
        {
            string ge = gen(r,b,g,c,d);
            if ( ge == "F" )    continue;
            if ( c == d )
            {
                if ( )
            }
        }
    }*/
    printf("Case #%d: ",t);
    for ( int c=1 ; c<=3 ; c++ )
    {
        for ( int d=c+1 ; d<=3 ; d++ )
        {
            string ge = gen(r,b,y,c,d);
            if ( ge != "F")
            {
                cout << ge << endl;
                return;
            }
        }
    }
    printf("IMPOSSIBLE\n");
}
int main()  {
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small_out.txt","w",stdout);
    int T;
    cin >> T;
    for ( int t=1 ; t<=T ; t++ )    solve(t);
}
