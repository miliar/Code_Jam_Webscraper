#include<bits/stdc++.h>
#define y0 asdasdasdsas
#define y1 asdsadasdasd
using namespace std;

vector<pair<int,int> > v;

int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    cin.tie(0);ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    for(int test=1;test<=T;test++)
    {
        printf("Case #%d: ",test);
        string s;
        cin >> s;
        v.clear();
        v.push_back(make_pair(s[0]-'0',1));
        for(int i=1;i<s.length();++i)
        {
            int c = s[i]-'0';
            int vlast = (int)v.size()-1;
            if(v[vlast].first == c)
                v[vlast].second++;
            else
                v.push_back(make_pair(c,1));
        }
        int q = 0;
        while(q+1<v.size() && v[q].first<v[q+1].first) q++;

        if(q+1<v.size())
        {
            v[q].second--;
            v.insert(v.begin()+q,make_pair(v[q].first-1,1));
            for(int i=q+1;i<v.size();++i)
                v[i].first=9;
        }

        string res="";
        for(int i=0;i<v.size();++i)
        {
            char c = '0' + v[i].first;
            if(res.length()==0 && c=='0')
                continue;
            for(int j=0;j<v[i].second;++j)
                res.push_back(c);
        }
        printf("%s\n",res.c_str());
    }

}

