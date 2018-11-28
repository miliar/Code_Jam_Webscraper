#include <bits/stdc++.h>

using namespace std;
int t,n,r,b,y,o,v,g;
string s;
string fun()
{
    s = "";
    for(int i=0; i<n; i++)
    {
        if(r == max(r,max(y,b)))
        {
            //cout<<"R";
            s += "R";
            r--;
            if(y == max(y,b) && y)
            {
                s += "Y";
                y--;
                i++;
            }
            else if(b == max(y,b) && b)
            {
                s += "B";
                b--;
                i++;
            }
        }
        else if(y == max(y,max(r,b)))
        {
            //cout<<"Y";
            s += "Y";
            y--;
            if(r == max(r,b) && r)
            {
                s += "R";
                r--;
                i++;
            }
            else if(b == max(r,b) && b)
            {
                s += "B";
                b--;
                i++;
            }
        }
        else
        {
            //cout<<"B";
            s += "B";
            b--;
            if(y == max(y,r) && y)
            {
                s += "Y";
                y--;
                i++;
            }
            else if(r == max(y,r) && r)
            {
                s += "R";
                r--;
                i++;
            }
        }
    }
    //cout<<s<<endl;
    if(s[0] == s[n-1])
    {

        if(s[2] != s[0])
        {
            swap(s[0],s[1]);
            return s;
        }

        for(int i=2; i<n-2; ++i)
        {
            if((s[i-1] != s[0]) && (s[i+1] != s[0]) && (s[i] != s[0]))
            {
                swap(s[0],s[i]);
                return s;
            }
        }
        reverse(s.begin(),s.end());
         if(s[2] != s[0])
        {
            swap(s[0],s[1]);
            return s;
        }

        for(int i=2; i<n-2; ++i)
        {
            if((s[i-1] != s[0]) && (s[i+1] != s[0]) && (s[i] != s[0]))
            {
                swap(s[0],s[i]);
                return s;
            }
        }

    }
    return s;

}

int main()
{
    ifstream cin("B-small-attempt1.in");
    ofstream cout("out");
    cin>>t;
    int tc(1);
    while(t--)
    {
        cin>>n;
        cin>> r >> o >> y >> g >> b >> v;
        if(max(b,max(y,r)) > min(b+r, min(y+r, (b+y))))
        {
            cout<<"Case #"<<tc++<<": IMPOSSIBLE"<<endl;
            continue;
        }
        cout<<"Case #"<<tc++<<": "<<fun()<<endl;
    }
    return 0;
}
