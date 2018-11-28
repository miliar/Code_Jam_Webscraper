#include<bits/stdc++.h>
#define ll long long
using namespace std;
#define INF 1000000000000


string goo(char firp , int n , int r, int o , int y , int g , int b, int v)
{
    if( r  < 0 ) return "";
    if( o  < 0 ) return "";
    if( y  < 0 ) return "";
    if( g  < 0 ) return "";
    if( b  < 0 ) return "";
    if( v  < 0 ) return "";
    string ans = "";
    ans = ans + firp;
    pair < ll ,char > tbp[6];
    tbp[0].first = r;
    tbp[0].second ='R';

    tbp[1].first = o;
    tbp[1].second ='O';

    tbp[2].first = y;
    tbp[2].second ='Y';

    tbp[3].first = g;
    tbp[3].second ='G';

    tbp[4].first = b;
    tbp[4].second ='B';

    tbp[5].first = v;
    tbp[5].second ='V';
    char prev = firp;
    for(int i=1;i<n;i++)
    {
            sort(tbp , tbp + 6);

            for(int j = 5 ; j >= 0 ; j-- )
            {
                if( prev == 'O' ){
                    if(tbp[j].second != 'O' && tbp[j].second != 'R' && tbp[j].second != 'Y' )
                    {
                        tbp[j].first--;
                        ans = ans + tbp[j].second;
                        prev = tbp[j].second;
                        break;
                    }
                }

                if( prev == 'R' ){
                    if(tbp[j].second != 'O' && tbp[j].second != 'R' && tbp[j].second != 'V' )
                    {
                        tbp[j].first--;
                        ans = ans + tbp[j].second;
                        prev = tbp[j].second;
                        break;
                    }
                }

                if( prev == 'Y' ){
                    if(tbp[j].second != 'O' && tbp[j].second != 'G' && tbp[j].second != 'Y' )
                    {
                        tbp[j].first--;
                        ans = ans + tbp[j].second;
                        prev = tbp[j].second;
                        break;
                    }
                }

                if( prev == 'V' ){
                    if(tbp[j].second != 'B' && tbp[j].second != 'R' && tbp[j].second != 'V' )
                    {
                        tbp[j].first--;
                        ans = ans + tbp[j].second;
                        prev = tbp[j].second;
                       break;;
                    }
                }

                if( prev == 'G' ){
                    if(tbp[j].second != 'B' && tbp[j].second != 'G' && tbp[j].second != 'Y' )
                    {
                        tbp[j].first--;
                        ans = ans + tbp[j].second;
                        prev = tbp[j].second;
                        break;;
                    }
                }

                if( prev == 'B' ){
                    if(tbp[j].second != 'B' && tbp[j].second != 'G' && tbp[j].second != 'V' )
                    {
                        tbp[j].first--;
                        ans = ans + tbp[j].second;
                        prev = tbp[j].second;
                        break;;
                    }
                }


            }

    }
    if(ans.length() != n ) return "";
        return ans;
    }
int main()
{

    ifstream cin; cin.open("B-small-attempt1.in"); ofstream cout; cout.open("fileout.txt"); //comment while testing.
    ll t;
    cin>>t;
    for(int testcase=1;testcase<=t;testcase++)
    {
        // Solve problem
        int n; int r,g,b,v,o,y;
        cin>> n >> r >> o >> y >> g >> b >> v;
        int rc = r + o + v;
        int bc = b + v + g;
        int yc = o + y + g;
        if(rc > n/2 || bc > n/2 || yc > n/2)
        {
        cout<<"Case #"<<testcase<<": IMPOSSIBLE"<<endl;
        continue;
        }
        cout<<"Case #"<<testcase<<": ";

        if(r>0)
        if(goo('R', n , r-1, o, y, g , b , v ) != "")
        {
            cout<<goo('R', n, r-1, o, y, g , b , v ) << endl; continue;
        }

        if(b>0)
        if(goo('b', n , r, o, y, g , b-1 , v ) != ""){
            cout<<goo('B', n, r, o, y, g , b-1 , v )<< endl; continue;}

        if(g>0)
        if(goo('R', n , r, o, y, g-1 , b , v ) != ""){
            cout<<goo('G', n, r, o, y, g-1 , b , v )<< endl; continue;}

        if(o>0)
        if(goo('R', n , r, o-1, y, g , b , v ) != ""){
            cout<<goo('O', n, r, o-1, y, g , b , v )<< endl; continue;}

        if(y>0)
        if(goo('R', n , r, o, y-1, g , b , v ) != ""){
            cout<<goo('Y', n, r, o, y-1, g , b , v )<< endl; continue;}

        if(v>0)
        if(goo('R', n , r, o, y, g , b , v-1 ) != ""){
            cout<<goo('V', n, r, o, y, g , b , v-1 )<< endl; continue;
        }

    }
    return 0;
}
