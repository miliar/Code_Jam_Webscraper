#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#include <cmath>
#include <queue>
#include <map>
using namespace std;
int testcase,test;
struct unicorn
{
    int R, O, Y, G, B, V;
};
bool cmp (pair<string,int> v1,pair<string,int> v2)
{
    return (v1.second<v2.second);
}
map <char,string> linked;
void unicorn_stall(map <char,int>& stall, unicorn& uni)
{
    stall['O'] = uni.O;
    stall['G'] = uni.G;
    stall['V'] = uni.V;
    stall['B'] = uni.B;
    stall['R'] = uni.R;
    stall['Y'] = uni.Y;
}
void stall_unicorn(map <char,int>& stall, unicorn& uni)
{
    uni.O = stall['O'];
    uni.G = stall['G'];
    uni.V = stall['V'];
    uni.B = stall['B'];
    uni.R = stall['R'];
    uni.Y = stall['Y'];
}
void f()
{
    int  N, R, O, Y, G, B, V;
    cin >> N >> R >> O >> Y >> G >> B >> V;

    queue < pair<string,unicorn> > q;
    // 0 R 1 O 2 Y 3 G 4 B 5 V
    unicorn c; c.R = R, c.O = O, c.Y = Y, c.G = G, c.B = B, c.V = V;
    if( R > 0)
    {
        c.R --;
        q.push( make_pair("R",c) );
        c.R ++;
    }
    if (O > 0)
    {
        c.O --;
        q.push( make_pair("O",c) );
        c.O ++;
    }
    if (Y > 0)
    {
        c.Y --;
        q.push( make_pair("Y",c) );
        c.Y ++;
    }
    if (G > 0)
    {
        c.G --;
        q.push( make_pair("G",c) );
        c.G ++;
    }
    if (B > 0)
    {
        c.B --;
        q.push( make_pair("B",c) );
        c.B ++;
    }
    if (V > 0)
    {
        c.V --;
        q.push( make_pair("V",c) );
        c.V ++;
    }

    while (!q.empty())
    {
        unicorn tmp = q.front().second;
        map <char,int> stall_left;
        unicorn_stall(stall_left,tmp);
        string cur = q.front().first;
        int curlen = cur.length();
        q.pop();
        if (curlen == N)
        {
            char last = cur[curlen-1];
            string linker = linked[last];
            int len_linker = linker.length();
            for (int i = 0; i < len_linker; i++)
            {
                if (cur[0] == linker[i])
                {
                    cout<< "Case #" << test<< ": " << cur << endl;
                    return;
                }
            }
        }
        char last = cur[curlen-1];
        string linker = linked[last];
        int len_linker = linker.length();
        for (int i = 0; i < len_linker; i++)
        {
            char link_char = linker[i];
            int left = stall_left[link_char];
            if (left > 0)
            {
                map <char,int> new_stall_left;
                new_stall_left = stall_left;
                new_stall_left[link_char]--;
                unicorn newc;
                stall_unicorn(new_stall_left,newc);
                string newcur = cur + link_char;
                q.push( make_pair(newcur,newc));
            }
        }
    }
    printf("Case #%d: IMPOSSIBLE\n",test);
}
void f2()
{
    int  N, R, O, Y, G, B, V;
    cin >> N >> R >> O >> Y >> G >> B >> V;
    vector < pair<string,int> > q;
    q.push_back( make_pair("R",R) );
    q.push_back( make_pair("B",B) );
    q.push_back( make_pair("Y",Y) );
    sort(q.begin(),q.end(),cmp);
    //Case #1: RBRBRBRBRBYBYBYBYBYBYBYBYBYBYB

    string res = "";
    string three= ""; three = q[0].first + q[1].first + q[2].first;
    string two = ""; two = q[1].first + q[2].first;
    for (int i = 0; i < q[0].second; i++)
        res += q[0].first + q[1].first + q[2].first;
    q[1].second -= q[0].second;
    q[2].second -= q[0].second;
    for (int i = 0; i < q[1].second; i++)
        res += q[1].first + q[2].first;
    q[2].second -= q[1].second;
    char last = q[2].first[0];
    for (int i = 0; i < q[2].second; i++)
    {
        bool found = false;
        if (res.length() != 0)
        for (int j = 0; j < res.length()-1; j++)
        {
            if (res[j] != last && res[j+1] != last)
            {
                string tmp = res.substr(0,j+1) + last + res.substr(j+1,res.length()-j-1);
                res = tmp;
                found = true;
                break;
            }
        }
        if (!found)
        {
            printf("Case #%d: IMPOSSIBLE\n",test);
            return;
        }
    }
    cout<< "Case #" << test<< ": " << res << endl;
//    if (res.length() < N) {cout << "failed" << endl; return;}
//    for (int i = 1; i < N-1;i++ )
//    {
//        if (res[i] == res[i-1] || res[i] == res[i+1])
//            {cout << "failed" << endl; return;}
//    }
//    cout << "ok" << endl;
}
int main()
{
    linked['O'] = "B";
    linked['G'] = "R";
    linked['V'] = "Y";
    linked['B'] = "RYO";
    linked['R'] = "GBY";
    linked['Y'] = "RBV";
    freopen("B-small.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> testcase;
    for (test = 1; test <= testcase; test++)
    {
        f2();
    }
    return 0;
}
