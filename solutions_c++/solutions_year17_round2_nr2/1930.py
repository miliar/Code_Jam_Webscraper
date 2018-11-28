#include<stdio.h>
#include<stdlib.h>
#include<fstream>
#include<iostream>
#include<string.h>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
    ifstream in;
    ofstream out;
    in.open("inputSmall.txt");
    out.open("outputSmall.txt");
    int t,cases=0;
    in>>t;
    while(t--)
    {
        cases++;
        int N,R,O,Y,G,B,V;
        in>>N>>R>>O>>Y>>G>>B>>V;
        string s = "";
        vector< pair<int,char> > v;
        v.push_back(make_pair(R,'R'));
        v.push_back(make_pair(Y,'Y'));
        v.push_back(make_pair(B,'B'));
        sort(v.begin(),v.end());
        int cnt;
        string temp1 = "";
        temp1+=v[0].second;
        temp1+=v[1].second;
        temp1+=v[2].second;
        cnt = v[0].first;
        for(int i=0;i<cnt;i++)s.append(temp1);
        string temp2 = "";
        temp2+=v[1].second;
        temp2+=v[2].second;
        cnt = v[1].first-v[0].first;
        for(int i=0;i<cnt;i++)s.append(temp2);
        string temp3 = "";
        temp3+=v[2].second;
        cnt = v[2].first-v[1].first;
        char c = v[2].second;
        for(int i=1;i<s.length() && cnt > 0;i++)
        {
            if(s[i-1] != c && s[i] != c)
            {
                s.insert(s.begin()+i,c);
                i++;
                cnt--;
            }
        }
        out<<"Case #"<<cases<<": ";
        if(cnt == 0)out<<s<<endl;
        else out<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
