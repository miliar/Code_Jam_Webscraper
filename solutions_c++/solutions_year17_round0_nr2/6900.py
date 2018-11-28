#include <bits/stdc++.h>

#define mp make_pair
#define ll long long
using namespace std;

vector<vector<int> > vv;
bool visited[100005];

string getss(int n)
{
    string s = "";
    for(int i = 0 ; i < n ; i++)
    {
        s+='+';
    }
    return s;
}

string getss2(int n)
{
    string s = "";
    for(int i = 0 ; i < n ; i++)
    {
        bool flag = rand()%2;
        if(flag ) s+='+';
        else s+='-';
    }
    return s;
}
int main()
{
    freopen("test.txt" , "r", stdin);
    freopen("test2.txt","w", stdout);
    int tt;
    cin >> tt;
    int a = 1;
    while(a<=tt)
    {
        string s ;
        cin >> s ;
        char maxx = '9';
        for(int j = s.length()-1 ; j > 0 ; j--)
        {
            if(s[j] < s[j-1])
            {
                s[j] = maxx;
                s[j-1]-=1;
                for(int c = j ; c < s.length() ;c++)
                    s[c] = '9';
            }

        }
        string t= "";
        if(s[0]!='0')
            t+=s[0];
        for(int i = 1 ; i < s.length() ; i++)
            t+=s[i];
        cout << "Case #" << a++ << ": " << t << endl;
    }
}
