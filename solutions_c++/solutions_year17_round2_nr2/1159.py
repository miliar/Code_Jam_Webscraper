#include <iostream>
#include <list>
#include <algorithm>
using namespace std;
struct Node
{
    int a,b;
    string s,t;
    bool operator<(const Node&obj) const{return a<obj.a;}
};
int main()
{
    ios::sync_with_stdio(false);
    int T;
    int cas=0;
    cin >> T;
    while(T--)
    {
        cout << "Case #" << ++cas << ": ";
        int n[7];
        cin >> n[0] >> n[1] >> n[6] >> n[2] >> n[4] >> n[3] >> n[5];
        bool flag=true;
        for(int i=1;i<=3;i++)
        {
            n[i]-=n[i+3];
            if(n[i]<0) cout << "IMPOSSIBLE" << endl,flag=false;
        }
        Node m[3];
        m[0]=Node{n[1],n[4],"R","RGR"};
        m[1]=Node{n[2],n[5],"Y","YVY"};
        m[2]=Node{n[3],n[6],"B","BOB"};

        if(!flag) continue;
        sort(m,m+3);
        list<string> ans;
        while(m[0].a)
        {
            m[0].a--;
            if(m[0].b)
            m[0].b--,ans.push_back(m[0].t);
            else ans.push_back(m[0].s);
            m[2].a--;
            if(m[2].b)
            m[2].b--,ans.push_back(m[2].t);
            else ans.push_back(m[2].s);
        }
        while(m[1].a&&m[2].a)
        {
            m[1].a--;
            if(m[1].b)
            m[1].b--,ans.push_back(m[1].t);
            else ans.push_back(m[1].s);
            m[2].a--;
            if(m[2].b)
            m[2].b--,ans.push_back(m[2].t);
            else ans.push_back(m[2].s);
        }
        if(m[2].a)
        {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        auto it=ans.begin();
        it++;
        while(m[1].a)
        {
            m[1].a--;

            ans.insert(it,m[1].s);
            it++;
        }
        for(auto it=ans.begin();it!=ans.end();it++)
            cout << *it;
        cout << endl;
    }
    return 0;
}

